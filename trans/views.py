from django.shortcuts import render, redirect
import googletrans
from gtts import gTTS
# Create your views here.

def filename():
    from random import randint
    st = ""
    for i in range(6):
        st += chr(randint(97,122))
    return st



def index(request):
    b = request.GET.get("bf",'')

    context = {
            "ndict" : googletrans.LANGUAGES,
            "fr" : "ko",
            "to" : "en",
            "fn" : "f",
            "b" : "b"
        }
    if b:
        f = request.GET.get("fr","")
        t = request.GET.get("to","")
        tr = googletrans.Translator()
        result = tr.translate(b,src=f,dest=t)
        context.update({
            "af" : result.text,
            "bf" : b,
            "fr" : f,
            "to" : t,
        })
    return render(request,"trans/index.html",context)



