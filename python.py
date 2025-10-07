
import pyttsx3

engine = pyttsx3.init()
text = "Hello, World!"
engine.save_to_file(text, 'hello.wav')
engine.runAndWait()
   

