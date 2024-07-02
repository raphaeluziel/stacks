from django.shortcuts import render, redirect, get_object_or_404

from .models import Cilt
from .forms import CiltForm

def home(request, user_id):

    ciltler = get_object_or_404(Cilt, user__id=user_id)

    if request.method == 'POST':
        form = CiltForm(request.POST, instance=ciltler)
        if form.is_valid():
            form.save()
            return redirect('cilt_detay', user_id=user_id)
    else:
        form = CiltForm(instance=ciltler)
    return render(request, 'home/home.html', {'form': form})

