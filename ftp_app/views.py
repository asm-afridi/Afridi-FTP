from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.http import FileResponse, Http404

# Correct path to uploads directory
UPLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)
FTP_DIR = os.path.join(settings.MEDIA_ROOT, 'ftp')
os.makedirs(FTP_DIR, exist_ok=True)

def file_list(request):
    files = []
    for filename in os.listdir(UPLOAD_DIR):
        file_path = os.path.join(UPLOAD_DIR, filename)
        if os.path.isfile(file_path):
            files.append({
                'name': filename,
                'url': settings.MEDIA_URL + 'uploads/' + filename
            })
    for filename in os.listdir(FTP_DIR):
        file_path = os.path.join(FTP_DIR, filename)
        if os.path.isfile(file_path):
            files.append({
                'name': filename,
                'url': settings.MEDIA_URL + 'ftp/' + filename
            })
    return render(request, 'ftp_app/file_list.html', {'files': files})


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage(location=UPLOAD_DIR)
        fs.save(file.name, file)
        return redirect('file_list')
    return render(request, 'ftp_app/upload.html')

def download_file(request, filename):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=False, filename=filename)
    else:
        raise Http404("File not found")