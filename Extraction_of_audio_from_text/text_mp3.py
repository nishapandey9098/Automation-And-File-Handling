import pyttsx3

# If you receive errors such as No module names win32com.client,
# No module named win32, or No module named win32api, you will need to aditionally  

class TextToSpeech:
    engine: pyttsx3.Engine
    
    def __init__(self, voice, rate: int, volume: float):
        self.engine  = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]
    
        for i, voice in enumerate(voices[0]):
            print(f'{i+1} {voice.name} {voice.age} {voice.languages[0]} ({voice.gender}) [{voice.id}]')
            
    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text)
        print('I am speaking...')
    
        if save: 
            self.engine.save_to_file(text, file_name)
        
        self.engine.runAndWait()
#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0

if __name__ == '__main__':
    tts = TextToSpeech('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0', 200, 1.0)
    #tts.list_available_voices()
    tts.text_to_speech('Hey mom, I just wanted to tell you how much you mean to me. You make my days brighter and my heart so much happier. I feel so lucky to have you in my life, and I love you endlessly.')
    
            
