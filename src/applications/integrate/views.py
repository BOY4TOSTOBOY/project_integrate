from django.shortcuts import render, redirect
from .models import UrlRepository, Commit, ModifiedFile
from pydriller import Repository
from .forms import UrlRepositoryForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = UrlRepositoryForm(request.POST)
        if form.is_valid():
            form.save()
            Commit.objects.all().delete()
            ModifiedFile.objects.all().delete()
            data_commit_hash = []
            data_commit_branches_name = []
            data_commit_author = []
            data_commit_url = []
            data_commit_message = []
            data_commit_stats_add_lines = []
            data_commit_stats_delete_lines = []
            data_commit_stats_count_change_lines = []
            data_commit_stats_count_change_files = []
            data_file_name = []
            data_file_full_path = []
            data_file_status = []
            data_file_stats_add_lines = []
            data_file_stats_delete_lines = []
            # reading the link to the repository from the database
            url_text = str(UrlRepository.objects.last())
            for commit in Repository(url_text).traverse_commits():
                commit_url = url_text + '/commit/' + commit.hash
                data_commit_hash.append(commit.hash)
                data_commit_branches_name.append(commit.branches)
                data_commit_author.append(commit.author.name)
                data_commit_url.append(commit_url)
                data_commit_message.append(commit.msg)
                data_commit_stats_add_lines.append(commit.insertions)
                data_commit_stats_delete_lines.append(commit.deletions)
                data_commit_stats_count_change_lines.append(commit.lines)
                data_commit_stats_count_change_files.append(commit.files)
                for mod in commit.modified_files:
                    data_file_name.append(mod.filename)
                    data_file_full_path.append(mod.new_path)
                    data_file_status.append(mod.change_type)
                    data_file_stats_add_lines.append(mod.added_lines)
                    data_file_stats_delete_lines.append(mod.deleted_lines)
                file_changes = ModifiedFile(file_name=data_file_name, file_full_path=data_file_full_path,
                                            file_status=data_file_status,
                                            file_stats_add_lines=data_file_stats_add_lines,
                                            file_stats_delete_lines=data_file_stats_delete_lines)
                file_changes.save()
            commit_information = Commit(commit_hash=data_commit_hash,
                                        commit_branches_name=data_commit_branches_name,
                                        commit_author=data_commit_author,
                                        commit_url=data_commit_url,
                                        commit_message=data_commit_message,
                                        commit_stats_add_lines=data_commit_stats_add_lines,
                                        commit_stats_delete_lines=data_commit_stats_delete_lines,
                                        commit_stats_count_change_lines=data_commit_stats_count_change_lines,
                                        commit_stats_count_change_files=data_commit_stats_count_change_files)
            commit_information.save()
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
    data_com_hash = Commit.objects.order_by('-commit_hash')[:1]
    data_com_branches_names = Commit.objects.order_by('-commit_branches_name')[:1]
    data_com_authors = Commit.objects.order_by('-commit_author')[:1]
    data_com_urls = Commit.objects.order_by('-commit_url')[:1]
    data_com_msgs = Commit.objects.order_by('-commit_message')[:1]
    data_com_sal = Commit.objects.order_by('-commit_stats_add_lines')[:1]
    data_com_sdl = Commit.objects.order_by('-commit_stats_delete_lines')[:1]
    data_com_sccl = Commit.objects.order_by('-commit_stats_count_change_lines')[:1]
    data_com_sccf = Commit.objects.order_by('-commit_stats_count_change_files')[:1]
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
