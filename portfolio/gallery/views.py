from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .models import Album, Category, Info, Experience, AboutMe, AlbumPhoto
from .forms import EmailForm

from decouple import config
import os

def index(request):
    albums = Album.objects.filter(category__type_of_content='photo').order_by('-id')[:3]
    context = {
        'category' : Category.objects.all(),
        'albums' : albums,
        'experience' : Experience.objects.first(),
        'info': Info.objects.first(),
        'aboutme': AboutMe.objects.first(),
        'form' : EmailForm()
    }
    return render(request, 'gallery/index.html', context)

class PersonalView(TemplateView):
    template_name = 'gallery/personal.html'

    def get_context_data(self,slug, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album"] = Album.objects.get(slug=slug)
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['albums'] = category.categories.prefetch_related('photos')
        return context



class SendMessage(FormView):
    template_name = 'gallery/index.html'
    form_class = EmailForm
    success_url = '/'

    def form_valid(self, form):

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        message_from_user = form.cleaned_data['message']

        theme_id = form.cleaned_data['theme_message']
        category = Category.objects.get(id=theme_id)
        theme_name = category.name

        message = f"""
                    Нове повідомленя, від {name}

                    Тема повідомлення: {theme_name}                    

                    Повідомлення:
                    " {message_from_user} " 

                    Контакти замовника:

                    Номер телефону: {phone_number}
                    Email: {email}

                    """

        send_mail(
            f'Замовлення',
            message,
            config('EMAIL_HOST_USER'),
            [config('EMAIL_ADMIN')],
            fail_silently=False
        )
        return super().form_valid(form)
        

    def form_invalid(self, form):
        messages.error(self.request, 'We have a little error in the form -_-')
        return super().form_invalid(form)