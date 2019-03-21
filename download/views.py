from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse
from django.core.files import File
import os
from .models import FileSto
from django.core.paginator import Paginator

SAVED_FILES_DIR = r'files/'
from django.shortcuts import render

# Create your views here.
def kejian(request):
    files = FileSto.objects.filter(cata='kejian')
    files = files.order_by('time').reverse()
    paginator = Paginator(files, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'kejian.html', {'contacts': contacts})

def lunwen(request):
    files = FileSto.objects.filter(cata='lunwen')
    files = files.order_by('time').reverse()
    paginator = Paginator(files, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'lunwen.html', {'contacts': contacts})

def sheji(request):
    files = FileSto.objects.filter(cata='sheji')
    files = files.order_by('time').reverse()
    paginator = Paginator(files, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'sheji.html', {'contacts': contacts})

def download_qita(request):
    files = FileSto.objects.filter(cata='qita')
    files = files.order_by('time').reverse()
    paginator = Paginator(files, 1) # Show 10 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'download_qita.html', {'contacts': contacts})


@require_GET
def download(request, filename):
    file_pathname = os.path.join(SAVED_FILES_DIR, filename)

    with open(file_pathname, 'rb') as f:
        file = File(f)

        response = HttpResponse(file.chunks(),
                                content_type='APPLICATION/OCTET-STREAM')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Length'] = os.path.getsize(file_pathname)

    return response



from django.shortcuts import render

# Create your views here.
