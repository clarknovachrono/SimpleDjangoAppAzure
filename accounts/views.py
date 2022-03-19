from django.shortcuts import render

# Create your views here.
from accounts.models import Personal


def index(request):
    my_personal_info = Personal.objects.get(id=1)
    context = {'my_personal_info': my_personal_info}
    return render(request, 'accounts/index.html', context)