import json
import requests
import hmac

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import UrlRepository, Commit, ModifiedFile, NumberOfCommits, NumberOfFiles, WebHook
from .forms import UrlRepositoryForm

from pydriller import Repository
from ipaddress import ip_address, ip_network
from hashlib import sha1


def index(request):
    error = ''
    if request.method == 'POST':
        form = UrlRepositoryForm(request.POST)
        if form.is_valid():
            form.save()
            count_commits = 0
            count_files = 0
            Commit.objects.all().delete()
            ModifiedFile.objects.all().delete()
            NumberOfCommits.objects.all().delete()
            NumberOfFiles.objects.all().delete()
            url_text = str(UrlRepository.objects.last())
            for commit in Repository(url_text).traverse_commits():
                commit_url = url_text + '/commit/' + commit.hash
                data_commit_hash = commit.hash
                data_commit_branches_name = commit.branches
                data_commit_author = commit.author.name
                data_commit_url = commit_url
                data_commit_message = commit.msg
                data_commit_stats_add_lines = commit.insertions
                data_commit_stats_delete_lines = commit.deletions
                data_commit_stats_count_change_lines = commit.lines
                data_commit_stats_count_change_files = commit.files
                count_commits += 1
                for mod in commit.modified_files:
                    data_file_name = mod.filename
                    data_file_full_path = mod.new_path
                    data_file_status = mod.change_type
                    data_file_stats_add_lines = mod.added_lines
                    data_file_stats_delete_lines = mod.deleted_lines
                    count_files += 1
                    file_changes = ModifiedFile(file_name=data_file_name,
                                                file_full_path=data_file_full_path,
                                                file_status=data_file_status,
                                                file_stats_add_lines=data_file_stats_add_lines,
                                                file_stats_delete_lines=data_file_stats_delete_lines)
                    file_changes.save()
                commit_information = Commit(commit_hash=data_commit_hash,
                                            commit_branches_name=data_commit_branches_name,
                                            commit_author=data_commit_author, commit_url=data_commit_url,
                                            commit_message=data_commit_message,
                                            commit_stats_add_lines=data_commit_stats_add_lines,
                                            commit_stats_delete_lines=data_commit_stats_delete_lines,
                                            commit_stats_count_change_lines=data_commit_stats_count_change_lines,
                                            commit_stats_count_change_files=data_commit_stats_count_change_files)
                commit_information.save()
            total_commits = NumberOfCommits(count_iteration=count_commits)
            total_commits.save()
            total_files = NumberOfFiles(count_iteration=count_files)
            total_files.save()
            return redirect('results/')
        else:
            error = 'Данные не введены'

    form = UrlRepositoryForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'integrate/index.html', data)


def results(request):
    data_url_repo = UrlRepository.objects.order_by('-id')[:1]
    data_com_hash = Commit.objects.order_by('-commit_hash')
    data_com_branches_names = Commit.objects.order_by('-commit_branches_name')
    data_com_authors = Commit.objects.order_by('-commit_author')
    data_com_urls = Commit.objects.order_by('-commit_url')
    data_com_msgs = Commit.objects.order_by('-commit_message')
    data_com_sal = Commit.objects.order_by('-commit_stats_add_lines')
    data_com_sdl = Commit.objects.order_by('-commit_stats_delete_lines')
    data_com_sccl = Commit.objects.order_by('-commit_stats_count_change_lines')
    data_com_sccf = Commit.objects.order_by('-commit_stats_count_change_files')
    data_f_name = ModifiedFile.objects.order_by('-file_name')
    data_f_path = ModifiedFile.objects.order_by('-file_full_path')
    data_f_status = ModifiedFile.objects.order_by('-file_status')
    data_f_sal = ModifiedFile.objects.order_by('-file_stats_add_lines')
    data_f_sdl = ModifiedFile.objects.order_by('-file_stats_delete_lines')
    data = {
        'data_url_repo': data_url_repo,
        'data_com_hash': data_com_hash,
        'data_com_branches_names': data_com_branches_names,
        'data_com_authors': data_com_authors,
        'data_com_urls': data_com_urls,
        'data_com_msgs': data_com_msgs,
        'data_com_sal': data_com_sal,
        'data_com_sdl': data_com_sdl,
        'data_com_sccl': data_com_sccl,
        'data_com_sccf': data_com_sccf,
        'data_f_name': data_f_name,
        'data_f_path': data_f_path,
        'data_f_status': data_f_status,
        'data_f_sal': data_f_sal,
        'data_f_sdl': data_f_sdl
    }
    return render(request, 'integrate/results.html', data)


@require_POST  # only post requests
@csrf_exempt
def hook(request):
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')
    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    results_webhook = WebHook(information=json.loads(request.body))
    results_webhook.save()
    return HttpResponse(status=204)


def webhook_last(request):
    info = WebHook.objects.all().last()
    data = {
        'info': info
    }
    return render(request, 'integrate/webhook.html', data)
