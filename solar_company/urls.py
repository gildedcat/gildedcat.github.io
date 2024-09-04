from django.contrib import admin
from django.urls import path, include
from django.apps import apps

# 确保 home 应用已正确导入
home_config = apps.get_app_config('home')
home_views = home_config.module.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('products/', include('products.urls')),
    path('projects/', include('projects.urls')),
    path('news/', include('news.urls')),
    path('contact/', include('contact.urls')),
    path('', home_views.home, name='home'),  # 将根路径指向 home 应用的视图
]
