from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Person
from .forms import PersonForm

@login_required
def person_list(request):
    persons = Person.objects.filter(user=request.user)
    print(persons)
    return render(request, 'person/person_list.html', {'persons': persons})

@login_required
def person_detail(request, user_id):
    person = get_object_or_404(Person, user__id=user_id, user=request.user)
    return render(request, 'person/person_detail.html', {'person': person})

@login_required
def person_create(request):
    existing_data = Person.objects.filter(user=request.user).exists()
    if existing_data:
        return render(request, 'person/duplicate_error.html')


    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = request.user
            person.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'person/person_form.html', {'form': form})

@login_required
def person_edit(request, user_id):
    person = get_object_or_404(Person, user__id=user_id, user=request.user)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            
            form.save()
            return redirect('person_detail', user_id=person.user.id)
    else:
        form = PersonForm(instance=person)
    return render(request, 'person/person_form.html', {'form': form})


@login_required
def person_delete(request, user_id):
    person = get_object_or_404(Person, user__id=user_id, user=request.user)
    if request.method == "POST":
        person.delete()
        return redirect('person_list')
    return render(request, 'person/person_confirm_delete.html', {'person': person})