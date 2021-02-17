from django.contrib import admin

# Register your models here.
from abanerd.models import Provider, CEUCredit, CSVFile, CEUMediaType, CEUCreditType, CEUImageFile

admin.site.register(Provider)
admin.site.register(CEUCredit)
admin.site.register(CSVFile)
admin.site.register(CEUMediaType)
admin.site.register(CEUCreditType)
admin.site.register(CEUImageFile)



