from django.conf import settings
from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ListContainer(NameMixin):
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pass


class ListItem(NameMixin):
    parent = models.ForeignKey('ListContainer', on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
