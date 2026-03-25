from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import IndexView
from root import settings
from app.views import ContactView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
