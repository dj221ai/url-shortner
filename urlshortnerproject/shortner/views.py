import json
import pyshorteners
from .models import ShortenedURL
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import ShortenedURLForm

# Create your views here.
def index(request):
    context = {
        'text': "create short Urls for Your Resume or projects and share with the world. it's free"
    }
    return render(request, 'shortner/index.html', context=context)



def createShortUrls(request): # sourcery skip: extract-method
    if request.method == "POST":
        form = ShortenedURLForm(request.POST)
        if form.is_valid():
            original_value = form.cleaned_data['original_url']
            short_value = pyshorteners.Shortener()
            short_value=short_value.tinyurl.short(original_value)
            s=ShortenedURL(user=request.user, original_url=original_value, short_url=short_value)
            s.save()
            return render(request, 'shortner/links.html')
    else:
        form = ShortenedURLForm()
        context = {'form': form}
        return render(request, 'shortner/create.html', context)

# all available links and redirect views
def links(request):
    url_data = ShortenedURL.objects.filter(user=request.user)
    url_data = list(url_data)
    context = {
        'datas': url_data
    }
    return render(request, 'shortner/links.html', context)

def deleteView(request, id):
    queryset=ShortenedURL.objects.filter(id=id).delete()
    return render(request, 'shortner/links.html')


