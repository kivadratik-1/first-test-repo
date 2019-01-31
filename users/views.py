from django.shortcuts import render, redirect
from django.utils import timezone
from .models import SimpleGuest
from .forms import SimpleGuestForm

# Create your views here.
def guest_list(request):
    simple_guest = SimpleGuest.objects.order_by('-simple_guest_id')[:5]
    return render(request, 'users/guest_list.html', {'simple_guest':simple_guest})

#def guest_new(request):
#    form = SimpleGuestForm()
#    return render(request, 'users/guest_edit.html', {'form': form})

def guest_new(request):
    if request.method == "POST":
        form = SimpleGuestForm(request.POST)
        if form.is_valid():
            simple_guest = form.save(commit=False)
            simple_guest.created_date = timezone.now()
            simple_guest.save()
            return redirect('guest_list')
    else:
        form = SimpleGuestForm()
    return render(request, 'users/guest_edit.html', {'form': form})
