from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Category, Main
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_log, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_log(request, user)
            return redirect('users')
        else:
            back_page = request.META.get('HTTP_REFERER')
            return HttpResponse(back_page)
    else:
        data = {
            'title': 'Login',
            'form': AuthenticationForm()
        }
        return render(request, 'menu/sign-in/login.html', data)


@login_required(login_url='login')
def users(request):
    return render(request, 'menu/sign-in/users.html')


def user_log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        back_page = request.META.get('HTTP_REFERER')
        return HttpResponse(back_page)


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            back_page = request.META.get('HTTP_REFERER')
            messages.success(request, 'Successfully registered')
            return redirect(back_page)

        else:
            back_page = request.META.get('HTTP_REFERER')
            return HttpResponse(back_page)
    else:
        data = {
            'title': 'Sign-up',
            'form': UserCreationForm()
        }
        return render(request, 'menu/sign-in/sign-up.html', data)


def index(request):
    data = {
        'title': 'Homepage',
        # 'BlogData': Blog.objects.filter(status=1),
        'BlogData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'index.html', data)




def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if subject and message and email:
            try:
                send_mail(subject, message, email, ['pbudhathoki349@gmail.com'])
                messages.success(request, 'Message has been sent')
                return redirect('contact')
            except BadHeaderError:
                return HttpResponseRedirect('/contact/thanks')
    else:
        data = {
            'title': 'Contact'
        }
        return render(request, 'contact.html', data)


class BlogListData(generic.ListView):
    model = Blog
    template_name = 'generic.html'
    context_object_name = 'BlogData'

    def get_queryset(self):
        return Blog.objects.all()


class BlogDetailsViews(generic.DetailView):
    model = Blog
    template_name = 'generic-details.html'
    context_object_name = 'BlogDetails'

    def get_queryset(self):
        return Blog.objects.all()


class DeleteBlog(generic.DeleteView):
    model = Blog
    template_name = 'delete.html'
    context_object_name = 'BlogData'

    def get_queryset(self):
        return Blog.objects.all()

    def get_success_url(self):
        return reverse('generic')


class UpdateBlog(generic.UpdateView):
    model = Blog
    template_name = 'edit.html'
    fields = ['created_at', 'title', 'status', 'image', 'description']


def about(request):
    data = {
        'title': 'About the BBC'
    }
    return render(request, 'about.html', data)


def terms_of_use(request):
    data = {
        'title': 'Terms of Use'
    }
    return render(request, 'terms_of_use.html', data)


def privacy_policy(request):
    data = {
        'title': 'Privacy Policy'
    }
    return render(request, 'privacy-policy.html', data)


def cookies(request):
    data = {
        'title': 'Cookies'
    }
    return render(request, 'cookies.html', data)


def BBC_news(request):
    data = {
        'title': 'News',
        'NewsData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-news.html', data)


def BBC_sports(request):
    data = {
        'title': 'Sport',
        'SportsData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-sports.html', data)


def BBC_reel(request):
    data = {
        'title': 'Reel',
        'ReelData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-reel.html', data)


def BBC_worklife(request):
    data = {
        'title': 'Worklife',
        'WorklifeData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-worklife.html', data)


def BBC_travel(request):
    data = {
        'title': 'Travel',
        'TravelData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-travel.html', data)


def BBC_future(request):
    data = {
        'title': 'Future',
        'FutureData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-future.html', data)


def BBC_culture(request):
    data = {
        'title': 'Culture',
        'CultureData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-culture.html', data)


def BBC_music(request):
    data = {
        'title': 'Music',
        'MusicData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-music.html', data)


def BBC_tv(request):
    data = {
        'title': 'TV',
        'TvData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-tv.html', data)


def BBC_weather(request):
    data = {
        'title': 'Weather',
        'WeatherData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-weather.html', data)


def BBC_sound(request):
    data = {
        'title': 'Sound',
        'SoundData': Category.objects.prefetch_related('main_set').all()
    }
    return render(request, 'menu/BBC-sound.html', data)


def Ad_choices(request):
    data = {
        'title': 'Ad Choices'
    }
    return render(request, 'Ad-choices.html', data)


def parental_guidance(request):
    data = {
        'title': 'Parental Controls'
    }
    return render(request, 'parental-guidance.html', data)


def more_parental_guidance(request):
    data = {
        'title': 'Parental Guidance'
    }
    return render(request, 'more-parental-guidance.html', data)


def newsletter(request):
    data = {
        'title': 'Newsletter'
    }
    return render(request, 'newsletter.html', data)


def detail(request, slug):
    subM = Main.objects.get(slug=slug)
    subM.page_visit += 1
    subM.save()
    data = {
        'title': 'Details',
        'BlogDetails': Main.objects.filter(slug=slug)
    }
    return render(request, 'detail.html', data)
