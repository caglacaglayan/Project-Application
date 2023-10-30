from PyPDF2.generic import NullObject
from django.shortcuts import redirect, render,HttpResponse,redirect,get_object_or_404
from .form import PdfForm
from .models import PDF
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import PyPDF2
from tika import parser

# Create your views here.

def index(request):
    return render(request, "index.html")

@login_required(login_url="user:login")
   
def dashboard(request):
    keyword = request.GET.get("keyword")

    x = request.GET.get("keyword")
    #y = x.split()
    #print(y)
    if keyword:
        bayrak = True
        result = list
        #pdfs = NullObject
        pdfs = PDF.objects.filter(content__contains = keyword,author = request.user)
        #for line in y:
            #pdfs = PDF.objects.filter(content__contains = pdfs,author = request.user)
            #result += PDF.objects.values(line)             # return ValuesQuerySet object
            #list_result = [entry for entry in result]  # converts ValuesQuerySet into Python list
            #return list_result

        return render(request,"dashboard.html",{"pdfs":pdfs})
        #return render(request,"dashboard.html",{"pdfs":pdfs})

    pdfs = PDF.objects.filter(author = request.user)
    context = {
        "pdfs":pdfs
    }

    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")

def addpdf(request):
    form = PdfForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        pdf = form.save(commit=False)
        pdf.author = request.user
        pdf.save()

        path = "./media/"+pdf.pdf_file.name
        pdfread = PyPDF2.PdfFileReader(path)
        str = ""

        parsed_pdf = parser.from_file(path)
        data = parsed_pdf['content']

        #for i in range(0,3):
            #str += pdfread.getPage(i).extractText()

        str += pdfread.getPage(2).extractText()

        pdf.content=data
        pdf.save()

        messages.success(request,"Ödev başarıyla gönderildi!")
        return redirect("pdf:dashboard")

    return render(request,"addpdf.html",{"form":form})

@login_required(login_url="user:login")

def detail(request,id):
    #pdf = PDF.objects.filter(id=id).first()
    pdf = get_object_or_404(PDF,id=id)
    return render(request,"detail.html",{"pdf":pdf})

@login_required(login_url="user:login")

def updatepdf(request,id):
    pdf = get_object_or_404(PDF, id=id)
    form = PdfForm(request.POST or None, request.FILES or None, instance=pdf)
    if form.is_valid():
        pdf = form.save(commit=False)
        pdf.author = request.user
        pdf.content = pdf.pdf_file.name
        pdf.save()

        path = "./media/"+pdf.pdf_file.name
        pdfread = PyPDF2.PdfFileReader(path)
        str = ""
        for i in range(1,3):
            str += pdfread.getPage(i).extractText()

        pdf.content=str
        pdf.save()

        messages.success(request,"Ödev başarıyla güncellendi!")
        return redirect("pdf:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")

def deletepdf(request,id):
    pdf = get_object_or_404(PDF,id=id)
    pdf.delete()

    messages.success(request, "Ödev başarıyla silindi!")
    return redirect("pdf:dashboard")

