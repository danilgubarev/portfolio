from django.urls import path
from .views import SendMessage,CategoryDetailView, PersonalView

app_name = 'gallery'

urlpatterns = [
    path('', SendMessage.as_view(), name='sendmessage'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
    path('personal/<slug:slug>/', PersonalView.as_view(), name='personal')
]