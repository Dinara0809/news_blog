from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .forms import *
from .models import *
from .models import News, Category
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
        return render(request, 'blog/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = UserLogin()
        return render(request, '')


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'blog/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2
    mixin_prop = 'hello world'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] =self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'blog/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objedcts.get(pk=self.kwargs['category_id']))

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'])


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewForm
    template_name = 'blog/add_news.html'
    raise_exception = True
