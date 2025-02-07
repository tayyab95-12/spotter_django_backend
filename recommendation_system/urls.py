from django.urls import path
from .views import FavoritesView

urlpatterns = [
    # Other endpoints
    path('favorites/', FavoritesView.as_view(), name='favorites'),
]
