from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]  # noqa: RUF012
        labels = {"text": ""}  # noqa: RUF012
