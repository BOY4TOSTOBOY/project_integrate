from django.db import models


class UrlRepository(models.Model):
    # full path to the repository
    url_text = models.TextField('URL адрес репозитория', max_length=255)

    def __str__(self):
        return self.url_text

    class Meta:
        verbose_name = 'URL адреса'
        verbose_name_plural = 'Список URL адресов'


class WebHook(models.Model):
    information = models.TextField('Данные вебхука', blank=True, null=True)

    def __str__(self):
        return self.information

    class Meta:
        verbose_name = 'Данные'
        verbose_name_plural = 'WebHooks Information'


class Commit(models.Model):
    url_txt = models.ForeignKey(UrlRepository, verbose_name='Принадлежит репозиторию', on_delete=models.CASCADE,
                                blank=True, null=True)
    # hash
    commit_hash = models.TextField('Hash', blank=True, null=True)
    # branches that contain the commit
    commit_branches_name = models.TextField('Имя ветки/веток', blank=True, null=True)
    # commit author
    commit_author = models.TextField('Автор', blank=True, null=True)
    # full commit url
    commit_url = models.TextField('Полный url адресс коммита', blank=True, null=True)
    # commit message
    commit_message = models.TextField('Сообщение коммита', blank=True, null=True)
    # total number of rows added
    commit_stats_add_lines = models.TextField('Количество добавленных строк', blank=True, null=True)
    # total number of deleted rows
    commit_stats_delete_lines = models.TextField('Количество удаленных строк', blank=True, null=True)
    # total number of added + deleted rows
    commit_stats_count_change_lines = models.TextField('Общее количество изменений', blank=True, null=True)
    # total number of modified files
    commit_stats_count_change_files = models.TextField('Общее количество измененных файлов', blank=True, null=True)

    def __str__(self):
        return str(self.commit_hash)

    class Meta:
        verbose_name = 'GitHub - данные о коммитах'
        verbose_name_plural = 'GitHub - данные о коммитах'

    def get_absolute_url(self):
        return self.id


class ModifiedFile(models.Model):
    commit_hash = models.ForeignKey(Commit, verbose_name='Принадлежат коммиту', on_delete=models.CASCADE, blank=True,
                                    null=True)
    # name of the modified file
    file_name = models.TextField('Имя файла', blank=True, null=True)
    # full path to the file
    file_full_path = models.TextField('Полный путь', blank=True, null=True)
    # file change status
    file_status = models.TextField('Статус', blank=True, null=True)
    # total number of rows added
    file_stats_add_lines = models.TextField('Количество добавленных строк', blank=True, null=True)
    # total number of deleted rows
    file_stats_delete_lines = models.TextField('Количество удаленных строк', blank=True, null=True)

    def __str__(self):
        return str(self.file_name)

    class Meta:
        verbose_name = 'GitHub - изменения'
        verbose_name_plural = 'GitHub - модифицированные файлы'

    def get_absolute_url(self):
        return self.id


class NumberOfCommits(models.Model):
    count_iteration = models.IntegerField('Количество коммитов', blank=True)

    def __str__(self):
        return str(self.count_iteration)

    class Meta:
        verbose_name = 'Количество коммитов в бд'
        verbose_name_plural = 'Number Commits'


class NumberOfFiles(models.Model):
    count_iteration = models.IntegerField('Количество файлов', blank=True)

    def __str__(self):
        return str(self.count_iteration)

    class Meta:
        verbose_name = 'Количество файлов в бд'
        verbose_name_plural = 'Number Files'
