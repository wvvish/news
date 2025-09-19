from django.db import models
from django.conf import settings

class NewsPreference(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='news_preferences'
    )
    
    # Категории новостей
    politics = models.BooleanField(default=True, verbose_name='Политика')
    economy = models.BooleanField(default=True, verbose_name='Экономика')
    technology = models.BooleanField(default=True, verbose_name='Технологии')
    sports = models.BooleanField(default=False, verbose_name='Спорт')
    entertainment = models.BooleanField(default=False, verbose_name='Развлечения')
    science = models.BooleanField(default=True, verbose_name='Наука')
    health = models.BooleanField(default=True, verbose_name='Здоровье')
    
    # Источники новостей
    rbc = models.BooleanField(default=True, verbose_name='РБК')
    kommersant = models.BooleanField(default=True, verbose_name='Коммерсант')
    vedomosti = models.BooleanField(default=False, verbose_name='Ведомости')
    tass = models.BooleanField(default=True, verbose_name='ТАСС')
    ria = models.BooleanField(default=True, verbose_name='РИА Новости')
    lenta = models.BooleanField(default=False, verbose_name='Лента.ру')
    gazeta = models.BooleanField(default=False, verbose_name='Газета.ру')
    
    # Дополнительные настройки
    email_notifications = models.BooleanField(default=True, verbose_name='Email уведомления')
    push_notifications = models.BooleanField(default=False, verbose_name='Push уведомления')
    update_frequency = models.CharField(
        max_length=20,
        choices=[
            ('realtime', 'В реальном времени'),
            ('hourly', 'Каждый час'),
            ('daily', 'Раз в день'),
        ],
        default='hourly',
        verbose_name='Частота обновлений'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Настройки новостей для {self.user.username}"
    
    def get_selected_categories(self):
        """Возвращает список выбранных категорий"""
        categories = []
        for category_key, category_name in settings.NEWS_CATEGORIES:
            if getattr(self, category_key, False):
                categories.append(category_name)
        return categories
    
    def get_selected_sources(self):
        """Возвращает список выбранных источников"""
        sources = []
        for source_key, source_name in settings.NEWS_SOURCES:
            if getattr(self, source_key, False):
                sources.append(source_name)
        return sources

# Примерные новости для демонстрации
SAMPLE_NEWS = [
    {
        'title': 'Новые меры экономической поддержки бизнеса',
        'category': 'economy',
        'source': 'rbc',
        'content': 'Правительство анонсировало новые программы поддержки малого и среднего бизнеса...',
        'published_at': '2024-01-15 10:30:00'
    },
    {
        'title': 'Прорыв в области искусственного интеллекта',
        'category': 'technology',
        'source': 'kommersant',
        'content': 'Ученые представили новую модель ИИ, способную решать сложные задачи...',
        'published_at': '2024-01-15 09:15:00'
    },
    {
        'title': 'Изменения в налоговом законодательстве',
        'category': 'politics',
        'source': 'vedomosti',
        'content': 'Госдума рассматривает поправки в налоговый кодекс...',
        'published_at': '2024-01-14 16:45:00'
    },
    {
        'title': 'Новое исследование в области медицины',
        'category': 'health',
        'source': 'ria',
        'content': 'Ученые обнаружили новый метод лечения хронических заболеваний...',
        'published_at': '2024-01-14 14:20:00'
    },
    {
        'title': 'Спортивные достижения российских атлетов',
        'category': 'sports',
        'source': 'tass',
        'content': 'Российские спортсмены показали выдающиеся результаты на международных соревнованиях...',
        'published_at': '2024-01-14 12:30:00'
    }
]