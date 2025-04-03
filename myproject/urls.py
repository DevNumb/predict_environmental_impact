from django.contrib import admin
from django.urls import path
from myapp.views import upload_excel
from myapp import views  # Import your views here
urlpatterns = [
    path('admin/', admin.site.urls),
        path("upload/",upload_excel, name="upload_excel"), # this will show upload page in the home page
]


