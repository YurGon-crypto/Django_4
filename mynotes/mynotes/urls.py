from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from .views import create_or_edit_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    re_path(r'^$', RedirectView.as_view(url='/notes/', permanent=True)),
    path('create_or_edit_note/', create_or_edit_note, name='create_or_edit_note'),

]
