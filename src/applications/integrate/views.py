from django.shortcuts import render
from .models import UrlRepository, Commit, ModifiedFile
from pydriller import Repository


def index(request):
    if request.method == "POST":
        # writing the url to the database
        current_url = UrlRepository()
        current_url.url_text = request.POST.get("url_text")
        current_url.save()

        # writing all data to the database
        for commit in Repository(current_url).traverse_commits():
            commit_url = current_url + '/commit/' + commit.hash
            # hash
            current_hash = Commit(commit_hash=commit.hash)
            current_hash.save()
            # branches that contain the commit
            current_branches = Commit(commit_branches_name=commit.branches)
            current_branches.save()
            # commit author
            current_author = Commit(commit_author=commit.author.name)
            current_author.save()
            # full commit url
            current_commit_url = Commit(commit_url=commit_url)
            current_commit_url.save()
            # commit message
            current_message = Commit(commit_message=commit.msg)
            current_message.save()
            # total number of rows added
            current_stats_add_lines = Commit(commit_stats_add_lines=commit.insertions)
            current_stats_add_lines.save()
            # total number of deleted rows
            current_stats_delete_lines = Commit(commit_stats_delete_lines=commit.deletions)
            current_stats_delete_lines.save()
            # total number of added + deleted rows
            current_stats_count_change_lines = Commit(commit_stats_count_change_lines=commit.lines)
            current_stats_count_change_lines.save()
            # total number of modified files
            current_stats_count_change_files = Commit(commit_stats_count_change_files=commit.files)
            current_stats_count_change_files.save()
            for m in commit.modified_files:
                # name of the modified file
                current_file_name = ModifiedFile(file_name=m.filename)
                current_file_name.save()
                # full path to the file
                current_file_full_path = ModifiedFile(file_full_path=m.new_path)
                current_file_full_path.save()
                # file change status
                current_file_status = ModifiedFile(file_status=m.change_type)
                current_file_status.save()
                # total number of rows added
                current_file_stats_add_lines = ModifiedFile(file_stats_add_lines=m.added_lines)
                current_file_stats_add_lines.save()
                # total number of deleted rows
                current_file_stats_delete_lines = ModifiedFile(file_stats_delete_lines=m.deleted_lines)
                current_file_stats_delete_lines.save()
    return render(request, 'integrate/index.html')


def results(request):
    current_url = UrlRepository.objects.all()
    commit_information = Commit.objects.all()
    file_information = ModifiedFile.objects.all()
    return render(request, 'integrate/results.html')
