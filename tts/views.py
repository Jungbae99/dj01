from django.shortcuts import render, redirect
from gtts import gTTS


# Create your views here.
def filename():
  from random import randint
  st = ""
  for i in range(6):
    st += chr(randint(97,122))
  return st


def index(request):
  context = {}
  if request.method=="POST":
    r=request.POST.get("tread")
    tts=gTTS(text=r, lang="ko")
    fn = filename()
    tts.save(f"media/tts/{fn}.mp3")
    context.update({
      "fn":fn,
      "r": r
    })    
  return render(request, 'tts/index.html', context)

