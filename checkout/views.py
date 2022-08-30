from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LcIJvIQDXjp8otbGZdOBifdz7sUeNxwfMkjkzndAxjjxOi5LZc9fsD9Uu5wSqBwd9OFIg35Zvr0APR2hg7e877X00LSVa7j7O',
        'client_secret': 'test client secret key'
    }

    return render(request, template, context)
