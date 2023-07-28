import datetime
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

# Find  current year
today = datetime.date.today()
year = today.strftime("%Y")

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'technology'
        verbose_name_plural = 'technologies'

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='static/media/img/', blank=True)
    description = models.TextField(max_length=400, db_index=True)
    tech_stack = ArrayField(models.CharField(max_length=20, blank=True), default=list)
    libraries = ArrayField(models.CharField(max_length=20, blank=True), default=list)
    date_start = models.DateField()
    year = models.IntegerField(default=year, null=True)
    github_url = models.CharField(max_length=300, null=True, default='', blank=True)
    live_url = models.CharField(max_length=300, null=True, default='', blank=True)
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (('id'),)
        index_together = (('id'), ('slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('', args=[self.id, self.slug])

