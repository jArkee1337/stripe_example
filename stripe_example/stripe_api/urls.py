from django.urls import path, include
from .views import *

urlpatterns = [
    path("buy/<int:pk>", CreateCheckoutSession.as_view(), name='checkout'),
    path("item/<int:pk>", ItemView.as_view()),
    path("success/", SuccessView.as_view()),
    path("cancel/", CancelView.as_view()),

]
