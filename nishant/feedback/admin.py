from django.contrib import admin

# Register your models here.
from .models import Feedback,contact,subscription

admin.site.register(Feedback)
admin.site.register(contact)
admin.site.register(subscription)