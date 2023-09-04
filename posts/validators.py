from datetime import datetime, timedelta

from django.utils.timezone import now
from rest_framework import serializers


class ForbiddenWordsValidator:
    def __call__(self, value):
        forbidden_words = ['ерунда', 'глупость', 'чепуха']
        for forbidden_word in forbidden_words:
            if forbidden_word in value.lower():
                raise serializers.ValidationError("Не нужно постить ерунду, глупость и чепуху")


class BirthDayValidator:
    def __call__(self, author):
        today = datetime.date(now())
        date = datetime.strptime(str(author.birth_day), "%Y-%m-%d")
        birth_day = date.replace(year=date.year + 18).date()
        if birth_day > today:
            raise serializers.ValidationError("Вам еще нет 18 лет")
