from pydriller import Repository
a = []
url_text = 'https://github.com/BOY4TOSTOBOY/OprosnikDjango'
for commit in Repository(url_text).traverse_commits():
    commit_url = url_text + '/commit/' + commit.hash
    print('Hash: {}; '
          'содержится в ветках: {}; '
          'автор: {}; '
          'URL-адрес: {}; '
          'сообщение: {}; '
          'количество добавленных строк {};'
          'количество удаленных строк: {};'
          'общее количество добавленных + удаленных строк {};'
          'общее количество файлов, измененных при фиксации'
          .format(commit.hash,
                  commit.branches,
                  commit.author.name,
                  commit_url,
                  commit.msg,
                  commit.insertions,
                  commit.deletions,
                  commit.lines,
                  commit.files)
          )
    for m in commit.modified_files:
        print(
            ' Изменен файл: {};'
            ' полный путь до файла: {};'
            ' статус изменения: {};'
            ' количество добавленных строк: {};'
            ' количество удаленных строк: {};'
            .format(m.filename,
                    m.new_path,
                    m.change_type,
                    m.added_lines,
                    m.deleted_lines)
            )
