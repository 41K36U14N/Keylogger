# The first thing you'll neeed to do is to reduce the security in your google email, since google will not allow your python application for security reasons. 
# its recommended that you make a whole new email account, if your going to be testing this out - for educational purposes.

import smtplib, ssl  # Servers that will help yu connect to your email, you'll nedd to insatall them with pip install 

def sendEmail (message) : 
  smtp_server = "smtp.gmail.com"
  port = 587
  sender_email = "testemailaccount@gmail.com"  #Make your own Gmail
  password = "enter your password"
  reciver_email = "testemailaccount@gmail.com"

  context = ssl.create_default_context()

  try :
    server = smtplib.SMTP(smtp_server ,port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendemail(sender_email, receiver_email, message)
    
  except Exception as e:
    print(e)
  
  except Exception as e:
    print(e)
    
  finally:
    server.quit()
