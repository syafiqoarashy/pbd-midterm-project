from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Sessions, Tracks, SessionsMME,SessionsSCE,SessionsAME,SessionsIT,SessionsECE,SessionsIE,SessionsSBCC,SessionsBBE,SessionsCPE,SessionsISBE

# Create your views here.
def show_sessions(request):
    session_data = Sessions.objects.all()
    tracks = Tracks.objects.all()
    MME = SessionsMME.objects.all()
    SCE = SessionsSCE.objects.all()
    AME = SessionsAME.objects.all()
    IT = SessionsIT.objects.all()
    ECE = SessionsECE.objects.all()
    IE = SessionsIE.objects.all()
    SBCC = SessionsSBCC.objects.all()
    BBE = SessionsBBE.objects.all()
    CPE = SessionsCPE.objects.all()
    ISBE = SessionsISBE.objects.all()
    context = {
        'sessions': session_data,
        'tracks': tracks,
        'MME': MME,
        'SCE': SCE,
        'AME': AME,
        'IT': IT,
        'ECE': ECE,
        'IE': IE,
        'SBCC': SBCC,
        'BBE': BBE,
        'CPE': CPE,
        'ISBE': ISBE,
    }
    return render(request, 'session.html', context)

def category(request) :
    tracks = Tracks.objects.all()
    session_data = Sessions.objects.all()
    context = {
        'tracks': tracks,
        'sessions': session_data,
    }
    return render(request, 'category.html', context)

def AME(request) :
    AME = SessionsAME.objects.all()
    context = {
        'AME': AME
    }
    return render(request, 'AME.html', context)

def BBE(request) :
    BBE = SessionsBBE.objects.all()
    context = {
        'BBE': BBE
    }
    return render(request, 'BBE.html', context)

def CPE(request) :
    CPE = SessionsCPE.objects.all()
    context = {
        'CPE': CPE
    }
    return render(request, 'CPE.html', context)

def ECE(request) :
    ECE = SessionsECE.objects.all()
    context = {
        'ECE': ECE
    }
    return render(request, 'ECE.html', context)

def IE(request) :
    IE = SessionsIE.objects.all()
    context = {
        'IE': IE
    }
    return render(request, 'IE.html', context)

def ISBE(request) :
    ISBE = SessionsISBE.objects.all()
    context = {
        'ISBE': ISBE
    }
    return render(request, 'ISBE.html', context)

def IT(request) :
    IT = SessionsIT.objects.all()
    context = {
        'IT': IT
    }
    return render(request, 'IT.html', context)

def MME(request) :
    MME = SessionsMME.objects.all()
    context = {
        'MME': MME
    }
    return render(request, 'MME.html', context)

def SBCC(request) :
    SBCC = SessionsSBCC.objects.all()
    context = {
        'SBCC': SBCC
    }
    return render(request, 'SBCC.html', context)

def SCE(request) :
    SCE = SessionsSCE.objects.all()
    context = {
        'SCE': SCE
    }
    return render(request, 'SCE.html', context)



