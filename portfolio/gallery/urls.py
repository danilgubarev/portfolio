from django.urls import path
from .views import SendMessage,CategoryDetailView

app_name = 'gallery'

urlpatterns = [
    
    path('', SendMessage.as_view(), name='sendmessage'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category')
]