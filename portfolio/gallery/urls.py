from django.urls import path
from .views import SendMessage,CategoryDetailView, PersonalView

app_name = 'gallery'

urlpatterns = [
    
    path('', SendMessage.as_view(), name='sendmessage'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('personal/<int:id>/', PersonalView.as_view(), name='personal')
]