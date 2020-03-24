from django.shortcuts import render
import pytesseract
from PIL import Image
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        image = request.FILES['image']
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
        output = pytesseract.image_to_string(image, lang='eng')
        return render(request, 'testapp/home.html')
    return render(request, 'testapp/home.html')