from django.shortcuts import render

# Create your views here.
def guest_list(request):
    return render(request, 'users/guest_list.html', {})
