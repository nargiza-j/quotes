from django.db import models

# Create your models here.

STATUS_CHOICES = [('0', 'new'), ('1', 'moderated')]


class Quote(models.Model):
    content = models.TextField(max_length=1500, null=False, blank=False, verbose_name="Content")
    name = models.CharField(max_length=150, verbose_name="Name")
    email = models.EmailField(max_length=255, verbose_name="Email")
    rate = models.PositiveIntegerField(verbose_name='Rate', null=False, blank=False, default=0)
    status = models.CharField(max_length=30, default='0', null=False, blank=False, choices=STATUS_CHOICES,
                              verbose_name='Status')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    def __str__(self):
        return f"{self.content} - {self.name} - {self.rate}"

    class Meta:
        db_table = 'quotes'
        verbose_name = 'quote'
        verbose_name_plural = 'quotes'