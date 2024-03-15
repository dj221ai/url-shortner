from django.shortcuts import render
from .forms import ShortenedURLForm
from .models import ShortenedURL
import string, secrets

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ShortenedURLForm(request.POST)

        if form.is_valid():
            original_data = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars = ''.join(secrets.choice(random_chars_list) for _ in range(7))

            while len(ShortenedURL.objects.filter(short_url=random_chars)) != 0:
                for _ in range(7):
                    random_chars+=secrets.choice(random_chars_list)
            s=ShortenedURL(original_url=original_data, short_url=random_chars)
            s.save()
            return render(request, 'shortner/urlcreated.html', {'chars':random_chars})
    else:
        form = ShortenedURLForm()
        context = {
            'form': form
        }
        return render(request, 'shortner/index.html', context)


def links(request):
    return render(request, 'shortner/links.html')
