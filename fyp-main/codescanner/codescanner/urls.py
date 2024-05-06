from django.contrib import admin
from django.urls import path, include
from users import views as user_views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.register, name='users-register'),
    path('login/', user_views.loginForm, name='users-login' ),
    path('logout/', user_views.logoutUser, name='users-logout' ),
    path('dashboard/', user_views.dashboard, name='users-dashboard'),
    path('profile/', user_views.profile, name="users-profile"), 
    path('scan/', user_views.scan, name="users-scan"), 
    path('', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('github/login', user_views.github_login, name="users-github"),
    path('github/callback/', user_views.github_callback, name='github_callback'),
    path('repository/', user_views.github_repositories, name="repos"),
    path('uploads/', user_views.upload_files, name="uploads"),

] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)