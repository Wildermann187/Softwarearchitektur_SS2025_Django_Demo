from django.contrib import admin
from .models import LogMessage
from .models import Author
from myproject.myapp.models import Author

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)

# Register your models here.
admin.site.register(LogMessage)