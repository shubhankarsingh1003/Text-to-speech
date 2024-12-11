import pyttsx3

text_to_speect=pyttsx3.init()

answer = input("what do you want to say: ")
rate = text_to_speect.getProperty('rate')
print(rate)
text_to_speect.setProperty('rate', 125)

voices = text_to_speect.getProperty('voices')
print(voices)
text_to_speect.setProperty('voice', voices[0].id)

text_to_speect.say(answer)
text_to_speect.runAndWait()
