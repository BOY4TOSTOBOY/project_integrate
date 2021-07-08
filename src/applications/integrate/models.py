from django.db import models


class UrlRepository(models.Model):
    # full path to the repository
    url_text = models.TextField('URL адрес репозитория', max_length=255)

    def __str__(self):
        return self.url_text

    class Meta:
        verbose_name = 'URL адреса'
        verbose_name_plural = 'Список URL адресов'


class Commit(models.Model):
    # hash
    commit_hash = models.TextField('Hash', blank=True)
    # branches that contain the commit
    commit_branches_name = models.TextField('Имя ветки/веток', blank=True)
    # commit author
    commit_author = models.TextField('Автор', blank=True)
    # full commit url
    commit_url = models.TextField('Полный url адресс коммита', blank=True)
    # commit message
    commit_message = models.TextField('Сообщение коммита', blank=True)
    # total number of rows added
    commit_stats_add_lines = models.TextField('Количество добавленных строк', blank=True)
    # total number of deleted rows
    commit_stats_delete_lines = models.TextField('Количество удаленных строк', blank=True)
    # total number of added + deleted rows
    commit_stats_count_change_lines = models.TextField('Общее количество изменений', blank=True)
    # total number of modified files
    commit_stats_count_change_files = models.TextField('Общее количество измененных файлов', blank=True)

    def __str__(self):
        return self.commit_message

    class Meta:
        verbose_name = 'Информация о коммитах'
        verbose_name_plural = 'Данные о коммитах'

    def get_absolute_url(self):
        return self.id


class ModifiedFile(models.Model):
    # name of the modified file
    file_name = models.TextField('Имя файла', blank=True)
    # full path to the file
    file_full_path = models.TextField('Полный путь', blank=True)
    # file change status
    file_status = models.TextField('Статус', blank=True)
    # total number of rows added
    file_stats_add_lines = models.TextField('Количество добавленных строк', blank=True)
    # total number of deleted rows
    file_stats_delete_lines = models.TextField('Количество удаленных строк', blank=True)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = 'Список изменений для каждого коммита'
        verbose_name_plural = 'Список изменений'

    def get_absolute_url(self):
        return self.id
