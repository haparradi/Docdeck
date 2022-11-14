from django.apps import AppConfig


class LoginappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LoginApp'
    
    def ready(self):
        import LoginApp.signals
