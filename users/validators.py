import re

from django.core.exceptions import ValidationError


def validate_password_format(password):
    match = re.search(r'\d', password)
    if not match:
        raise ValidationError('Пароль должен содержать цифры')

    if len(password) < 8:
        raise ValidationError('Пароль должен содержать не меньше 8 символов')


def validate_email_format(user_email):
    emails = ['@yandex.ru', '@ya.ru', '@mail.ru']
    for email in emails:
        if user_email.endswith(email):
            return True

    raise ValidationError('Поддерживается только Яндекс и Мэйл')
