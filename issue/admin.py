from django.contrib import admin
from issue.models import CustomUser, Epic, Comment, Ticket
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Epic)
admin.site.register(Comment)
admin.site.register(Ticket)