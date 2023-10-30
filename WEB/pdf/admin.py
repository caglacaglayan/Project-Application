from django.contrib import admin

from .models import PDF

# Register your models here.

@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):

    list_display = ["title","author","pdf_file","created_date"]

    list_display_links = ["title","author","created_date"]

    search_fields = ["content"]

    list_filter = ["author"]
    class Meta:
        model = PDF

