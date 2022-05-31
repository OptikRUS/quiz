from django import forms
from django.core.exceptions import ValidationError


class QuestionForm(forms.Form):
    choices = forms.MultipleChoiceField(label='', required=False, widget=forms.CheckboxSelectMultiple)
    instance = {}

    def is_valid(self):
        if len(self.data) == 1:
            return False
        else:
            return True

    def clean(self):
        if len(self.data) == 1:
            raise ValidationError("Вы не выбрали ответ")

    def user_answer_instance(self):
        self.instance.update(self.data)

    def clean_instance(self):
        self.instance.clear()
