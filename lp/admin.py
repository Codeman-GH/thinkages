from django.contrib import admin
from .models import LeaveReply

# Register your models here.



class LeaveReplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment', 'date_posted' ]


admin.site.register(LeaveReply, LeaveReplyAdmin)
