from django.contrib import admin
from .models import UrlRepository, Commit, ModifiedFile

admin.site.register(UrlRepository)
admin.site.register(Commit)
admin.site.register(ModifiedFile)
