from django.db import models


class UrlRepository(models.Model):
    # full path to the repository
    url_text = models.CharField(max_length=255,
                                help_text='Введите url адрес репозитория, к примеру: '
                                          'https://github.com/BOY4TOSTOBOY/OprosnikDjango',
                                blank=False)

    def __str__(self):
        return '{}'.format(self.url_text)


class Commit(models.Model):
    # hash
    commit_hash = models.CharField(max_length=50, blank=True)
    # branches that contain the commit
    commit_branches_name = models.CharField(max_length=255, blank=True)
    # commit author
    commit_author = models.CharField(max_length=30, blank=True)
    # full commit url
    commit_url = models.CharField(max_length=255, blank=True)
    # commit message
    commit_message = models.TextField(blank=True)
    # total number of rows added
    commit_stats_add_lines = models.CharField(max_length=20, blank=True)
    # total number of deleted rows
    commit_stats_delete_lines = models.CharField(max_length=20, blank=True)
    # total number of added + deleted rows
    commit_stats_count_change_lines = models.CharField(max_length=20, blank=True)
    # total number of modified files
    commit_stats_count_change_files = models.CharField(max_length=20, blank=True)

    def get_hash(self):
        hash_current = Commit.objects.values_list('commit_hash')
        return hash_current


class ModifiedFile(models.Model):
    # name of the modified file
    file_name = models.CharField(max_length=40, blank=True)
    # full path to the file
    file_full_path = models.CharField(max_length=255, blank=True)
    # file change status
    file_status = models.CharField(max_length=25, blank=True)
    # total number of rows added
    file_stats_add_lines = models.CharField(max_length=20, blank=True)
    # total number of deleted rows
    file_stats_delete_lines = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '{}'.format(self.file_name)
