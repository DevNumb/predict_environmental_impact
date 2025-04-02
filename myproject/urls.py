from django.contrib import admin
from django.urls import path
from myapp.views import home
from myapp.views import upload_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), 
        path("upload/",upload_excel, name="upload_excel"), # This will show "Hello, Django!" on the homepage
]


