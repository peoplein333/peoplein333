
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Notice


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content']

    widgets = {
        'title': forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목'}
        ),
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
}