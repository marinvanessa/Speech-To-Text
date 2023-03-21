import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone(device_index=2) as source:
    print("Recording started.")
    audio_text = r.listen(source)
    print("Message was recorded with success.")

    try:
        my_text = r.recognize_google(audio_text, language="ro-RO")
        print("The message is: " + r.recognize_google(audio_text, language="ro-RO"))

    except Exception as e:
        print("Message could not be recorded because of the following error: " + str(e))
