import aiofiles
from django.shortcuts import render

from .forms import UploadFileForm


async def handle_uploaded_file(file):
    """awaitable function to upload a file and put it in media folder"""
    async with aiofiles.open(f"media/{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            await destination.write(chunk)


async def upload(request):
    # Pass the `request.FILES` and `request.POST` to the form
    # and also pass the file to `handle_uploaded_file` function
    #
    # You should render the `upload.html` template with the
    # proper context
    if request.method == 'GET':
        form = UploadFileForm()
        return render(request, 'upload.html', {'form':form})

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            await handle_uploaded_file(request.FILES['file'])
            context = {'form':form, 'success':True}
            return render(request, 'upload.html', context)

