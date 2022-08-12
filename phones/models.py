from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField(max_length=50)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=55, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)