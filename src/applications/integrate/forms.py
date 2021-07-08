from .models import UrlRepository, Commit, ModifiedFile
from django.forms import ModelForm, TextInput


class UrlRepositoryForm(ModelForm):
    class Meta:
        model = UrlRepository
        fields = ['url_text']

        widgets = {
            "url_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the repository URL'
            })
        }


class CommitForm(ModelForm):
    class Meta:
        model = Commit
        fields = ['commit_hash', 'commit_branches_name', 'commit_author', 'commit_url', 'commit_message',
                  'commit_stats_add_lines', 'commit_stats_delete_lines', 'commit_stats_count_change_lines',
                  'commit_stats_count_change_files']


class ModifiedFileForm(ModelForm):
    class Meta:
        model = ModifiedFile
        fields = ['file_name', 'file_full_path', 'file_status',
                  'file_stats_add_lines', 'file_stats_delete_lines']
