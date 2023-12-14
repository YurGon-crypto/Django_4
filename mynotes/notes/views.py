from django.shortcuts import redirect
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render



def my_view(request):
    return render(request, 'home.html')

@login_required
def view_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)


class YourNoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class YourNoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

def home(request):
    notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})




def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    return render(request, 'notes/delete_note.html', {'note': note})