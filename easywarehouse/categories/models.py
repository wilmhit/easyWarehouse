from django.db import models
from django.urls import reverse


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Category(name={self.name})"

    def get_absolute_url(self):
        return reverse("categories-details", kwargs={"pk": self.id})

    class Meta:
        db_table = "categories"
