#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import smtplib
from email.message import EmailMessage
import gc
import threading


# In[9]:


EMAIL_ADDRESS='ENTER YOUR EMAIL'
EMAIL_PASS='ENTER ACCES KEY'
KINDLE_EMAIL='ENTER KINDLE EMAIL'
FOLDER_PATH='pdf_to_Uplode'


# In[10]:


file_names=os.listdir(FOLDER_PATH)


# In[11]:


smtp=smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()


# In[12]:


smtp.login(EMAIL_ADDRESS,EMAIL_PASS)


# In[17]:

print(file_names)
gc.enable()
def send_to_kindle():
    i=0
    
    for file in file_names:
        
        msg=EmailMessage()
        msg['Subject']=('python'+str(i))
        msg['From']=EMAIL_ADDRESS
        msg['To']=KINDLE_EMAIL
        i+=1


        
        if(os.path.getsize(FOLDER_PATH+'\\'+file)<(2.5e+7)):
            file_path=FOLDER_PATH+'\\'+file
        
            try:
                f=open(file_path,'rb')
                
            except Exception as e:
                file = open("FAIL.txt", "a") 
                file.write("\n")
                file.write('%s' %str(file))
                file.close()
                print(e)
            
                
                
            
            
            file_data=f.read()
            file_name=file
            msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)
            
            try:
                
                smtp.send_message(msg)
                
            except Exception as e:
                file = open("RECORD//FAIL.txt", "a") 
                file.write("\n")
                file.write('%s' %str(file_name))
                file.close()
                print(e)
                
            
            
            else:      
                print(file+ ' Succes')
                f.close()
                file = open("RECORD//SUCESS.txt", "a") 
                file.write("\n")
                file.write('%s' %str(file_name))
                file.close()
                os.remove(file_path)
            
            
        else:
        
            print(file+ ' Greater than 25MB')
            file = open("RECORD//FAIL.txt", "a") 
            file.write("\n")
            file.write('%s Greater than 25MB' %str(file))
            file.close()
        
    print('done')    


# In[18]:


t1 = threading.Thread(target=send_to_kindle)
t1.start()


