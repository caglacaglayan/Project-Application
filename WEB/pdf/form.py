from django import forms
from .models import PDF

class PdfForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ["title", "pdf_file", "content"]
         

        