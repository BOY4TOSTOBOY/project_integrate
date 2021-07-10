from django.contrib import admin
from .models import UrlRepository, Commit, ModifiedFile, NumberOfCommits, NumberOfFiles

admin.site.register(UrlRepository)
admin.site.register(Commit)
admin.site.register(ModifiedFile)
admin.site.register(NumberOfCommits)
admin.site.register(NumberOfFiles)
