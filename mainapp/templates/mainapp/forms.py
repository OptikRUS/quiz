from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import RadioSelect, CheckboxInput
from django.conf import settings

from mainapp.models import Answer, Question

CHOICES = [
    ('ON', 'OFF'),
]


# class QuestionForm(forms.Form):
#     checkbox = forms.BooleanField(required=False)
#     # print(ckeckboxes)
#
#     # Agree = forms.BooleanField(required=False, disabled=False,
#     #                            widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
#     #                            help_text="I accept the terms in the License Agreement",
#     #                            error_messages={'required': 'Please check the box'})
#     class Meta:
#         model = Answer
#         fields = '__all__'


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    # def clean(self):
    #     data = super(QuestionForm, self).clean()
    #     # print(data.items())
    #
    # class Meta:
    #     model = Answer
    #     fields = ['is_right']
    #     widgets = {
    #         'is_anything_required': CheckboxInput(attrs={'class': 'required checkbox form-control'}),
    #     }


class QuestionForm(forms.Form):

    def is_valid(self):
        if len(self.data) == 1:
            return False
        else:
            return True

    def clean(self):
        if len(self.data) == 1:
            raise ValidationError("Нужно выбрать выбрать хотя бы один вариант ответа")



