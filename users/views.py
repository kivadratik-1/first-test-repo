from django.shortcuts import render
from .models import SimpleGuest

# Create your views here.
def guest_list(request):
    simple_guest = SimpleGuest.objects.order_by('-simple_guest_id')[:5]
    return render(request, 'users/guest_list.html', {'simple_guest':simple_guest})
