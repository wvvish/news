from django import forms
from django.conf import settings
from .models import NewsPreference

class NewsPreferenceForm(forms.ModelForm):
    class Meta:
        model = NewsPreference
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at']
        widgets = {
            'update_frequency': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Настраиваем поля категорий
        for category_key, category_name in settings.NEWS_CATEGORIES:
            self.fields[category_key].widget.attrs.update({
                'class': 'form-check-input',
                'role': 'switch'
            })
            self.fields[category_key].label = category_name
        
        # Настраиваем поля источников
        for source_key, source_name in settings.NEWS_SOURCES:
            self.fields[source_key].widget.attrs.update({
                'class': 'form-check-input',
                'role': 'switch'
            })
            self.fields[source_key].label = source_name
        
        # Настраиваем остальные поля
        self.fields['email_notifications'].widget.attrs.update({
            'class': 'form-check-input',
            'role': 'switch'
        })
        self.fields['push_notifications'].widget.attrs.update({
            'class': 'form-check-input',
            'role': 'switch'
        })