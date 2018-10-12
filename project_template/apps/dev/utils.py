from django.utils.crypto import get_random_string



def get_random_secret_key():
    """
    This function was copied from the Django Git repo,
    and is how secret keys are generated internally in Django 2.0

    Return a 50 character random string usable as a SECRET_KEY setting value.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)
