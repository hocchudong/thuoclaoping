from django import forms
from check.models import Alert


class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['email_alert', 'telegram_id', 'webhook']
