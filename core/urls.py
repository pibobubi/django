from django.urls import path, include
from .views import HomeView, AboutView
from django.conf import settings
from django.conf.urls.static import static

from user import views as user_view

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', user_view.LoginView.as_view(), name='login'),
    path('register/', user_view.RegisterView.as_view(), name='register'),
    path('register/complete/', user_view.RegisterComplete.as_view(), name='register_complete'),
    path('profile/', user_view.EditProfileView.as_view(), name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)