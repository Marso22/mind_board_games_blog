from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_signed_up)
def show_registration_success(request, user, **kwargs):
    print("Signal triggered!")  # Add this line
#    messages.success(request, "Registration successful! Welcome to Mind Board Games Blog.")