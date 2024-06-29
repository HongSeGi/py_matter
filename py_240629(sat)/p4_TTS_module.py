import pyttsx3
#pip install pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 150) #속도를 150으로 설정(기본값 200)
    engine.setProperty('volume', 0.9) #볼륨을 0.9로 설정(기본값 1.0)
    voices = engine.getProperty('voices') #음성 설정
    engine.setProperty('voice', voices[1].id) # 음성을 두번째음성으로 설정(기본값은 voices[0].id)

    #입력 텍스트를 음성으로 변환
    engine.say(text)
    engine.runAndWait()

def say_hello():
    str_v = "If you're nothing without this suit, then you shouldn't have it." #한국어 말할수있게하려면 설정값만바꾸면된다고 하셨다.
    return str_v

# text_to_speech(say_hello()) > main파일로 옮김.