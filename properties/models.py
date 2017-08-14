from django.db import models
from django.utils import text


# Create your models here.
class Solution(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)
    file = models.FileField(upload_to='properties/solutions')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = text.slugify(self.name)

        super(Solution, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                   update_fields=update_fields)
