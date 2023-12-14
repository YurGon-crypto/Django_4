from django.shortcuts import render


def create_or_edit_note(request):
    return render(request, 'create_or_edit_note.html')
