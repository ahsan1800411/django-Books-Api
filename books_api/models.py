from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    number_of_pages = models.IntegerField();
    quantity = models.IntegerField()
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
