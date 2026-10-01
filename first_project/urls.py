
from django.contrib import admin 
from django.urls import path,include
from first_project import views
from django.conf import settings
from django.conf.urls.static import static

# Django admin header customozation 
admin.site.site_header = 'Login to Programmer Mafruda'
admin.site.site_title = "Welcome to Mafruda' Dashboard"
admin.site.index_title = 'Welcome to this Portal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
    path('certificate', views.certificate, name='certificate')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
