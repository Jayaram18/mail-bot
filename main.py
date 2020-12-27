import smtplib
import speech_recognition as sp
import pyttsx3
from email.message import EmailMessage

listener = sp.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sp.Microphone() as voice:
            print('listening to audio  input...')
            speech = listener.listen(voice)
            info = listener.recognize_google(speech)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {'friend 1': 'friend1@gmail.com',
              'friend 2': 'friend2@gmail.com',
              'friend 3': 'friend3@gmail.com'}


def get_email_info():
    talk('Receiver of this  email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Your email is sent')
    talk('Do you want to send another email?')
    another_mail = get_info()
    if 'yes' in another_mail:
        get_email_info()


get_email_info()