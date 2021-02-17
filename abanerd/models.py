import uuid
from django.db import models
from django.contrib.auth import get_user_model

from autoslug import AutoSlugField
from stdimage import StdImageField

User = get_user_model()

class Provider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=250, null=True, blank=True)
    slug = AutoSlugField(null=True, default=None, unique=True, unique_with=('created', 'modified', 'url'),
                         populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class CEUMediaType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    slug = AutoSlugField(null=True, default=None, unique=True, unique_with=('name'), populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class CEUCreditType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    slug = AutoSlugField(null=True, default=None, unique=True, unique_with=('name'), populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class CEUImageFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    filename = models.TextField(max_length=256, default='none', unique=False)
    image_url = models.CharField(max_length=512, null=True, default=None, unique=True)
    image = StdImageField(upload_to='ceu-image', blank=True, variations={
        'preview': (100, 100),
        'grid': (328, 320, True),
        'modal': (315, 367),
        'large': (600, 400),
    }, delete_orphans=True)

    def __str__(self):
        return self.filename

class CEUCredit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True)
    title = models.CharField(max_length=1024, unique=True)
    description = models.TextField()
    url = models.URLField(max_length=2048)
    image = models.ForeignKey(CEUImageFile, on_delete=models.PROTECT, related_name='ceu_image', blank=True, null=True)
    image_url = models.CharField(max_length=512, null=False, blank=True, default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    credits = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    media = models.ForeignKey(CEUMediaType, on_delete=models.PROTECT, related_name='ceu_media_type')
    type = models.ForeignKey(CEUCreditType, on_delete=models.PROTECT, related_name='ceu_credit_type')
    event_date = models.DateTimeField(blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT, related_name='ceu_provider')
    is_featured = models.BooleanField(default=False)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='title',
                         unique_with=('provider', 'title',))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        unique_together = ('provider', 'title',)

class CSVFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='csv-data-upload-files/')

    def __str__(self):
        return self.provider.name

class CEUSubmission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=250)
    slug = AutoSlugField(null=True, default=None, unique=True, unique_with=('created', 'modified', 'url'),
                         populate_from='name')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
