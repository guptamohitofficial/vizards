from django.db import models

# Create your models here.

class Card(models.Model):

    bname = models.CharField(max_length=50)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'