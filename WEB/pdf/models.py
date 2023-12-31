from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class PDF(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    pdf_file = models.FileField(verbose_name="PDF dosyası")
    content = RichTextField(blank=True,null=True,verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulduğu Tarih")
    
    def __str__(self):
        return self.title



