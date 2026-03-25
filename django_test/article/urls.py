from django.urls import path

from .views import CardsView, IndexView, CardView

urlpatterns = [
    path('', IndexView.as_view(), name='card_create'),
    path('cards/', CardsView.as_view(), name='cards'),
    path('cards/<int:card_id>', CardView.as_view())
]