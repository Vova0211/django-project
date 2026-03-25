from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Card
from .forms import CreateCardForm

class CardView(View):
    def get(self, request, *args, **kwargs):
        card = get_object_or_404(Card, id=kwargs['card_id'])
        # card = Card.objects.get(id=id)
        return render(
            request,
            'card.html',
            context={
                'card': card
            }
        )

class CardsView(View):
    def get(self, request, *args, **kwargs):
        cards = Card.objects.all()
        return render(
            request,
            'cards.html',
            context={
                'cards': cards
            }
        )

class IndexView(View):
    def post(self, request, *args, **kwargs):
        form = CreateCardForm(request.POST)
        if form.is_valid():
            title, body, price = form.cleaned_data['title'], form.cleaned_data['body'], form.cleaned_data['price']
            Card.objects.create(title=title, body=body, price=price)
        return redirect('card_create')

    def get(self, request, *args, **kwargs):
        form = CreateCardForm()  # Создаем экземпляр нашей формы
        return render(
            request, "index.html", {"form": form}
        )