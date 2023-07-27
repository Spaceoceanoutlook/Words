from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=100, verbose_name='Слова')

    objects = models.Manager()

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'


class Save(models.Model):
    long_word = models.CharField(max_length=100, verbose_name='Слово')
    player_points = models.IntegerField(verbose_name='Очки игрока')
    comp_points = models.IntegerField(verbose_name='Очки компьютера')

    objects = models.Manager()

    def __str__(self):
        return self.long_word

    class Meta:
        verbose_name = 'История игры'
        verbose_name_plural = 'История игр'

