import os
from django.shortcuts import redirect
import stripe
from django.views import View
from django.views.generic import TemplateView
from dotenv import load_dotenv
from stripe_api.models import Item

load_dotenv()

stripe.api_key = os.environ.get("STRIPE_KEY")


class CreateCheckoutSession(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )

        return redirect(session.url, code=303)


class ItemView(TemplateView):
    template_name = 'Checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Item.objects.get(id=self.kwargs['pk'])
        return context


class SuccessView(TemplateView):
    template_name = 'Success.html'


class CancelView(TemplateView):
    template_name = 'Cancel.html'
