import random
from gtts import *
from playsound import *
n=random.randint(10,99)
print(n)
x=int(input("Enetr any number between 10 to 99"))
print(x)
if n==x:
    print("You are Winner")
    tts = gTTS("You are Winner")
    tts.save('winner.mp3')
    playsound('winner.mp3')
else:
    print("You Are Looser")
    tts = gTTS("You are Looser")
    tts.save('Looser.mp3')
    playsound('Looser.mp3')