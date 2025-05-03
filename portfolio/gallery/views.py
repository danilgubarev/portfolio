from django.contrib import auth, messages
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Album, Category, Info, Experience, AlbumPhoto, AboutMe
from .forms import EmailForm
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView


def index(request):
    context = {
        'category' : Category.objects.all(),
        'albums' : Album.objects.all()[0:6],
        'experience' : Experience.objects.first(),
        'info': Info.objects.first(),
        'aboutme': AboutMe.objects.first(),
        'form' : EmailForm()
    }
    return render(request, 'gallery/index.html', context)



class CategoryDetailView(DetailView):
    model = Category
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['albums'] = category.categories.all()
        return context



class SendMessage(FormView):
    template_name = 'gallery/index.html'
    form_class = EmailForm
    success_url = '/'

    def form_valid(self, form):

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        theme_message = form.cleaned_data['theme_message']
        message_from_user = form.cleaned_data['message']

        message = f"""
                    Нове повідомленя, від {name}

                    Тема повідомлення: {theme_message}                    

                    Повідомлення:
                    {message_from_user} 

                    Данні замовника:

                    Номер телефону: {phone_number}
                    Емейл: {email}

                    """

        send_mail(
            f'hello ааа',
            message,
            'shop97826@gmail.com',
            [''],
            fail_silently=False
        )
        return super().form_valid(form)
        

    def form_invalid(self, form):
        messages.error(self.request, 'you dodik')
        return super().form_invalid(form)
    