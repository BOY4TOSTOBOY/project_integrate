from django.db import models


class UrlRepository(models.Model):
    # full path to the repository
    url_text = models.CharField('URL адрес репозитория', max_length=255,
                                help_text='Введите url адрес репозитория, к примеру: '
                                          'https://github.com/BOY4TOSTOBOY/OprosnikDjango',)

    def __str__(self):
        return self.url_text

    class Meta:
        verbose_name = 'URL адрес'
        verbose_name_plural = 'Список URL адресов'


class Commit(models.Model):
    # hash
    commit_hash = models.CharField('Hash', max_length=50, blank=True)
    # branches that contain the commit
    commit_branches_name = models.CharField('Имя ветки/веток', max_length=255, blank=True)
    # commit author
    commit_author = models.CharField('Автор', max_length=30, blank=True)
    # full commit url
    commit_url = models.CharField('Полный url адресс коммита', max_length=255, blank=True)
    # commit message
    commit_message = models.TextField('Сообщение коммита', blank=True)
    # total number of rows added
    commit_stats_add_lines = models.CharField('Количество добавленных строк', max_length=20, blank=True)
    # total number of deleted rows
    commit_stats_delete_lines = models.CharField('Количество удаленных строк', max_length=20, blank=True)
    # total number of added + deleted rows
    commit_stats_count_change_lines = models.CharField('Общее количество изменений', max_length=20, blank=True)
    # total number of modified files
    commit_stats_count_change_files = models.CharField('Общее количество измененных файлов', max_length=20, blank=True)

    def __str__(self):
        return self.commit_hash

    class Meta:
        verbose_name = 'Информация о коммитах'
        verbose_name_plural = 'Данные о коммитах'


class ModifiedFile(models.Model):
    # name of the modified file
    file_name = models.CharField('Имя файла', max_length=40, blank=True)
    # full path to the file
    file_full_path = models.CharField('Полный путь', max_length=255, blank=True)
    # file change status
    file_status = models.CharField('Статус', max_length=25, blank=True)
    # total number of rows added
    file_stats_add_lines = models.CharField('Количество добавленных строк', max_length=20, blank=True)
    # total number of deleted rows
    file_stats_delete_lines = models.CharField('Количество удаленных строк', max_length=20, blank=True)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = 'Список изменений'
        verbose_name_plural = 'Список изменений'
