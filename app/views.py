from django.shortcuts import render
from .models import *
# Create your views here.

def home_page(request):
    objects = Profile.objects.all()
    detals = Detals.objects.all()
    skills = Skills.objects.all()
    languages = Languages.objects.all()
    workexperince = WorkExperince.objects.all()
    educations = Educations.objects.all()
    footers = Footer.objects.all()
    icons = Icons.objects.all()

    context = {
        'objects':objects,
        'detals':detals,
        'skills':skills,
        'languages':languages,
        'workexperince':workexperince,
        'educations':educations,
        'footers':footers,
        'icons':icons
    }

    return render(request, 'index.html', context)