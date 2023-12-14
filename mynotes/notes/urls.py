from django.urls import path
from .views import YourNoteListCreateAPIView, YourNoteDetailAPIView, home, delete_note
from django.contrib.auth.views import LoginView, LogoutView
from .views import my_view


urlpatterns = [
    path('api/notes/', YourNoteListCreateAPIView.as_view(), name='note-list'),
    path('api/notes/<int:pk>/', YourNoteDetailAPIView.as_view(), name='note-detail'),
    path('', home, name='home'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my_endpoint/', my_view, name='my_endpoint'),
]

