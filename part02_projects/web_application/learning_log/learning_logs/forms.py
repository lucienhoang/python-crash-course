from django import forms

from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}
        widgets = {
            "text": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Python, Guitar, Japanese...",
                }
            )
        }


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]  # noqa: RUF012
        labels = {"text": ""}
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Write your thoughts here...",
                }
            )
        }
