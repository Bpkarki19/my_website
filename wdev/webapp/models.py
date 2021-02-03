from django.db import models

class Homepage(models.Model):
    text = models.CharField(max_length=200, default= 0)
    footer_text = models.CharField(max_length=200, default= 0)

    def __str__(self):
        return self.text

class Cards(models.Model):
    card_image = models.ImageField()
    card_title = models.CharField(max_length=50)
    card_text = models.CharField(max_length=500)

    def __str__(self):
        return self.card_text
