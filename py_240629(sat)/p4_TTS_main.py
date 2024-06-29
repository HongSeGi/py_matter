import p4_TTS_module as tts

tts.text_to_speech(tts.say_hello())

# >뭔가 오류나는데 뭔진모르겠음 일단 넘어가고 다시체크해보기로한다.

# >> 해결.
# 원인 : 불러올 모듈의 이름이 숫자로 시작해서 문제였던듯. 알파벳으로시작해야 오류안나는듯.