from django.urls import path
from .views import (
    IndexView, ManifestoView, PressView,
)

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('manifesto', ManifestoView.as_view(), name='manifesto'),
    path('press', PressView.as_view(), name='press'),
]

