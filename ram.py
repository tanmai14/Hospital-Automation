from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from selenium import webdriver
from time import sleep
from tkinter import filedialog
import speech_recognition as sr
import os
#import autoit
from googletrans import Translator
import pyperclip#To copy the text text present in clipboard
#import cv2 
import numpy as np
from pyglet import *
import multiprocessing
#Recquries pyaudio
check=0
lan='en-IN'
ddw=open('doctor_details.txt').read().split('$')
path=ddw[4]
ax=ddw[5]
p_name=[]
weight=''
gender=''
age=''
p_no=[]
prob=[]
medi=[]
name=''
problem=''
list1=''
with open("Welcome.txt",'w') as file0:
  file0.write('0')
def speech1():
  global sprs,ax
  ax=1
  sprs.destroy()
  messagebox.showinfo("Information","Google Speech Recogintion Activated")
  save_doctor_d()
def speech2():
  global sprs,ax
  ax=0
  sprs.destroy()
  messagebox.showinfo("Information","Web Based Speech Recognition Activated")
  save_doctor_d()
def pdf():
  preview_pdfB.config(state='active')
  send_pdfB.config(state='active')
  merge_pdfB.config(state='active')
  print_pdfB.config(state='active')
  mail_pdfB.config(state='active')
  if (entry3.get()=='' or entry0.get()=='' or pn_p_e.get()=='' or p_a_e.get()=='' or pn_w_e.get()=='' or Text1.get('1.0')==''or Text2.get('1.0')==''):
     messagebox.showerror('Error','Please fill all the details')
     return
  global h,d,path
  c=0
  try:
      global h,d
      d=open('doctor_details.txt').read()
      h=open('hospital_details.txt').read()
  except FileNotFoundError:
      c=1
      messagebox.showinfo('Information',"You didn't Fill either Doctor Details or Hospital Details or both. Please fill them by clicking on Reset doctor Details and Reset Hospital details")
  if c==0:
      pdf = FPDF() 
      pdf.add_page() 
      pdf.set_font("Arial",'B', size = 18)
      h=h.split('$')
      pdf.cell(200, 10, txt =h[0].upper(),ln = 1, align = 'C')
      pdf.set_font('Arial',size=12)
      l=h[1].split('\n')
      for i in l:
          pdf.cell(200,5, txt =i,ln =1, align = 'C')
      pdf.set_font("Arial",size=16)
      d=d.split('$')
      pdf.cell(200,10,txt="Doctor's name:  "+d[0]+'\t\t\t\t\t\t\t\t\t'+"Phone number:  "+d[1],ln=2)
          #pdf.cell(200,10,txt="Phone number:  "+x[1],ln=2)
      pdf.cell(200,10,txt="Pateint's name:  "+entry3.get()+'\t\t\t\t\t\t\t\t\t'+"Gender:  "+entry0.get(),ln=3)
          #pdf.cell(200,10,txt="Gender:  "+entry0.get(),ln=5)
      pdf.cell(200,10,txt="Patient Phone number: "+pn_p_e.get()+'\t\t\t\t\t\t\t\t\t'+"Age: "+p_a_e.get(),ln=1)
      pdf.set_font("Arial",size=16)
      probl=Text1.get('1.0',END).split('\n')
      pdf.cell(200,10,txt="PROBLEM:",ln=1)
      pdf.set_font("Arial",size=12)
      for i in range(0,len(probl)):
          pdf.cell(200,5,txt=str(i+1)+"."+probl[i],ln=1)
      pdf.cell(200,2,txt='',ln=1)
      pdf.set_font("Arial",size=16)
      pdf.cell(200,10,txt="MEDICATION:",ln=6)
      pdf.set_font("Arial",size=12)
      tablets=Text2.get('1.0',END).split('\n')
      for i in range(0,len(tablets)):
          pdf.cell(200,5,txt=str(i+1)+"."+tablets[i],ln=i+7)
      if path=='':
         messagebox.showerror('Error','Add Signature')
      else:
         pdf.image(path)
         try:
            pdf.output(entry3.get()+".pdf")
            messagebox.showinfo('Information','PDF had been saved successfully')
         except OSError:
            messagebox.showerror('Error','PDF not created Due to some error retry by typing Patient full name')
def lab_request():
    pdf1=FPDF()
    pdf1.add_page()
    pdf1.set_font('Arial',size=16)
    pdf1.cell(200,10,txt="Patient Details :",ln=1)
    pdf1.cell(200,10,txt="Patient Name : {}".format(entry3.get()),ln=1)
    pdf1.cell(200,10,txt="Phone Number : {}".format(pn_p_e.get()),ln=1)
    pdf1.cell(200,10,txt="Age          : {}".format(p_a_e.get()),ln=1)
    pdf1.cell(200,10,txt="Weight       : {}".format(pn_w_e.get()),ln=1)
    pdf1.cell(200,10,txt="Gender       : {}".format(entry0.get()),ln=1)
    pdf1.output("pat_details.pdf")
def merge():
    pass
def printing():
    pass
def mailpdf():
    '''sender_email="harshassv.13@gmail.com"
    rec_email="harshassv.13@gmail.com"
    password=input(str("please enter ur password"))
    message="530045registration.s3.ap-south-1.amazonaws.com/8374094118.pdf"
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,password)
    print("login success")
    server.sendmail(sender_email,rec_email,message)
    print("email has been sent")'''
def mic_gif():
   print('hi')
   pic=image.load_animation('mic.gif')
   picsprite=sprite.Sprite(pic)
   w=picsprite.width
   h=picsprite.height
   print(w,h)
   win=window.Window(w,h,"chat bot",style='borderless')
   #win.set_location(1230,600)
   gl.glClearColor(128,128,128,1)
   @win.event
   def on_mouse_press(x, y, button, modifiers):
       if button==window.mouse.LEFT:
           win.close()
   @win.event
   def on_draw():
       win.clear()
       picsprite.draw()
   app.run()
def initial_video():
   cap = cv2.VideoCapture('final.mp4') 
   # Check if camera opened successfully 
   if (cap.isOpened()== False):  
     print("Error opening video  file")      
   # Read until video is completed 
   while(cap.isOpened()): 
     # Capture frame-by-frame 
     ret, frame = cap.read() 
     if ret == True: 
       # Display the resulting frame
       cv2.moveWindow('Frame',240,30)
       cv2.imshow('Frame', frame) 
       # Press Q on keyboard to  exit 
       if cv2.waitKey(25) & 0xFF == ord('q'): 
         break
     # Break the loop 
     else:  
       break
   # When everything done, release  
   # the video capture object 
   cap.release() 
   # Closes all the frames 
   cv2.destroyAllWindows() 
def web():
   global text_1
   try:
     text_d=''
     messagebox.showinfo('Information','1.You need to click stop once you close the web page \n2.click on allow once the web page opens ,copy the text(by selecting the text if it is not highlited with blue,right click on the text and click on copy)and close the window')
     driver = webdriver.Chrome()
     driver.get('https://www.google.com/intl/en/chrome/demos/speech.html')
     driver.find_element_by_xpath('//*[@id="start_img"]').click()
     while True:
         try:
             text_1=text_d
             text_d=driver.find_element_by_class_name("final").text
         except:
           if text_1!='':
             text_1=text_1.lower().split()
             break
   except:
     return
   print(text_1)
   filling()
def speech_reg():
   global sprs
   sprs=Toplevel()
   sprs.title('Speech Recognition Softwares')
   sprs.geometry('252x50+376+80')
   sprs.resizable(0,0)
   b_1=Button(sprs,text="Google speech Recognition Software",command=speech1,width=36)
   b_1.pack()
   b_2=Button(sprs,text="Web page Speech Recognition(Recommended)",command=speech2)#web)
   b_2.pack()
def clear():
   global entry3,entry0,pn_p_e,p_a_e,pn_w_e,Text1,Text2,TextA,TextT
   if not (entry3.get()=='' and entry0.get()=='' and pn_p_e.get()=='' and p_a_e.get()=='' and pn_w_e.get()=='' and Text1.get('1.0')=='' and Text2.get('1.0')==''):
       c=messagebox.askquestion('Conformation','Do you Want to clear all the fields')
       if c=='yes':
          entry3.delete(0,END)
          entry0.delete(0,END)
          pn_p_e.delete(0,END)
          p_a_e.delete(0,END)
          pn_w_e.delete(0,END)
          Text1.delete('1.0',END)
          Text2.delete('1.0',END)
def checking():
  if check > 0 :
    if not (entry3.get()=='' and entry0.get()=='' and pn_p_e.get()=='' and p_a_e.get()=='' and pn_w_e.get()=='' and Text1.get('1.0')=='' and Text2.get('1.0')==''):
      c=messagebox.askquestion('Conformation','Do you Want to Create new Prescription')
      if c=='no':
        return
      else:
        sleep(0.5)
        clear()
        return
def make_changes():
  global sprs,check,take
  '''try:
    with open("Welcome.txt",'r') as file3:
      take=file3.read()
  except:
    with open("Welcome.txt",'+w') as file4:
      take=file4.read()
  if int(take)==0:
    web()
  else:
    lan='en-IN'
    r=sr.Recognizer()
    mic=sr.Microphone()
    #print(sr.Microphone.list_microphone_names())
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('Listening......')
        audio = r.listen(source)
        text6=r.recognize_google(audio,language=lan)
        text6=text6.split()'''
  def qwerty():
    global advice,tests
    adv=[]
    test=[]
    text6=['name','Vamsi','age','20','gender','male','advice','eat','food','regularly','number','74853923879','weight','45','problem','headache','next','blood','cancer','next','fever','medicine','trfdrs','Dolo 650','colpal','tests','malaria']
    k=0
    while(k<len(text6)):
      if(k!=len(text6)-1 and ((text6[k]=='and' and text6[k+1]=='change') or text6[k]=='change' or text6[k]=='to')):
        text6.remove(text6[k])
        #print(len(text6))
        k=k-1
      k=k+1
    for k in range(len(text6)):
      if(text6[k]=='name'):
        entry3.delete(0,END)
        i=k+1
        while((i!=len(text6)) and (text6[i]!="gender" and text6[i]!="number" and text6[i]!="advice" and text6[i]!="tests" and text6[i]!="problem" and text6[i]!="cause" and text6[i]!="medicine" and text6[i]!='phone' and text6[i]!='age' and text6[i]!='weight' and text6[i]!='medication')):
          entry3.insert(END,str(text6[i])+" ")
          i=i+1
      elif(text6[k]=="gender"):
        entry0.delete(0,END)
        entry0.insert(END,str(text6[k+1])+" ")
      elif(text6[k]=="number"):
        pn_p_e.delete(0,END)
        pn_p_e.insert(END,str(text6[k+1])+" ")
      elif (text6[k]=='age'):
        p_a_e.delete(0,END)
        p_a_e.insert(END,str(text6[k+1])+" ")
      elif(text6[k]=='weight'):
        pn_w_e.delete(0,END)
        pn_w_e.insert(END,str(text6[k+1])+" ")
      elif(text6[k]=="problem" or text6[k]=="cause"):
        Text1.delete('1.0',END)
        i=k+1
        prob=[]
        while((i!=len(text6)) and (text6[i]!="gender" and text6[i]!="name" and text6[i]!="advice" and text6[i]!="tests" and text6[i]!="number" and text6[i]!="medicine" and text6[i]!='medication' and text6[i]!='phone' and text6[i]!='age' and text6[i]!='weight')):
          prob.append(text6[i])
          problem=' '.join(prob)
          problem='\n'.join(problem.split(' next '))
          #Text1.insert(END,str(text6[i])+" ")
          i=i+1
        Text1.insert(END,problem)
      elif(text6[k]=="advice"):
        TextA.delete('1.0',END)
        i=k+1
        advice=[]
        while((i!=len(text6)) and (text6[i]!="gender" and text6[i]!="name" and text6[i]!="problem" and text6[i]!="tests" and text6[i]!="cause" and text6[i]!="number" and text6[i]!="medicine" and text6[i]!='medication' and text6[i]!='phone' and text6[i]!='age' and text6[i]!='weight')):
          adv.append(text6[i])
          advice=' '.join(adv)
          advice='\n'.join(advice.split(' next '))
          #Text1.insert(END,str(text6[i])+" ")
          i=i+1
        TextA.insert(END,advice)
      elif(text6[k]=="tests"):
        TextT.delete('1.0',END)
        i=k+1
        tests=[]
        while((i!=len(text6)) and (text6[i]!="gender" and text6[i]!="name" and text6[i]!="problem" and text6[i]!="advice" and text6[i]!="cause" and text6[i]!="number" and text6[i]!="medicine" and text6[i]!='medication' and text6[i]!='phone' and text6[i]!='age' and text6[i]!='weight')):
          test.append(text6[i])
          tests=' '.join(test)
          tests='\n'.join(tests.split(' next '))
          #Text1.insert(END,str(text6[i])+" ")
          i=i+1
        TextT.insert(END,tests)
      elif(text6[k]=="medicine" or text6[k]=='medication'):
         Text2.delete('1.0',END)
         i=k+1
         medi=[]
         while((i!=len(text6)) and (text6[i]!="gender" and text6[i]!="name" and text6[i]!="advice" and text6[i]!="tests" and text6[i]!="problem" and text6[i]!="cause" and text6[i]!="number" and text6[i]!='phone' and text6[i]!='age' and text6[i]!='weight')):
           medi.append(text6[i])
           i=i+1
         i=0
         tablets1=[]
         while len(medi)!=0:
           for j in range(len(medi)):
             if(medi[j]=='tablet' or medi[j]=='strips' or medi[j]=='strip' or medi[j]=='tablets' or medi[j]=='capsules' or medi[j]=='capsule'):
               i=j
               break
           if i+1<len(medi) and medi[i+1]=='morning':
             i=i+1
           if i+1<len(medi) and medi[i+1]=='afternoon':
             i=i+1
           if i+1<len(medi) and medi[i+1]=='evening':
             i=i+1
           tablets1.append(' '.join(medi[:i+1]))
           medi=medi[i+1:]
         list12='\n'.join(tablets1)
         Text2.insert(END,list12)
  qwerty()
def open_pdf():
   try:
      path_pdf=entry3.get()+'.pdf'
      os.startfile(path_pdf)
   except:
      messagebox.showerror('Error','No prescription Found')
def add_sign():
   global path
   window.filename=filedialog.askopenfilename()
   path=os.path.join(os.getcwd(),window.filename)
   save_doctor_d()
   if path!='':
      x=path[(path.rfind('/'))+1:]
      messagebox.showinfo('Information',x+' is selected')
def s_e():
   lan='en-IN'
def s_h():
   lan='hi-IN'
def s_te():
   lan='te-IN'
def s_ta():
   lan='ta-IN'
def s_mal():
   lan='ml-IN'
def s_mar():
   lan='mr-IN'
def s_g():
   lan='gu-IN'
def s_k():
   lan='kn-IN'
def s_b():
   lan='bn-IN'
def s_u():
   lan='ur-IN'
def t_e():
   pass
def t_h():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='hi').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='hi').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='hi').text+')')
   L6.config(text='Gender'+'('+translator.translate('Gender',dest='hi').text+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='hi').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='hi').text+')')
   L7.config(text='Problem'+'('+translator.translate('Problem',dest='hi').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='hi').text+')')
def t_te():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='te').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='te').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='te').text+')')
   L6.config(text='Gender'+'('+'లింగము'+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='te').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='te').text+' చేయండి'+')')
   L7.config(text='Problem'+'('+translator.translate('Problem',dest='te').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='te').text+')')
def t_ta():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='ta').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='ta').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='ta').text+')')
   L6.config(text='Gender'+'('+translator.translate('Gender',dest='ta').text+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='ta').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='ta').text+')')
   L7.config(text='Problem'+'('+translator.translate('Problem',dest='ta').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='ta').text+')')
def t_mal():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='ml').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='ml').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='ml').text+')')
   L6.config(text='Gender'+'('+translator.translate('Gender',dest='ml').text+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='ml').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='ml').text+')')
   L7.config(text='Problem'+'('+translator.translate('Problem',dest='ml').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='ml').text+')')
def t_mar():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='mr').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='mr').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='mr').text+')')
   L6.config(text='Gender'+'('+translator.translate('Gender',dest='mr').text+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='mr').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='mr').text+')')
   L7.config(text='Problem'+'('+translator.translate('Problem',dest='mr').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='mr').text+')')
def t_g():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='gu').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='gu').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='gu').text+')')
   L6.config(text='Gender'+'('+translator.translate('Gender',dest='gu').text+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='gu').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='gu').text+')')
   L7.config(text='Problem'+'('+translator.translate('Problem',dest='gu').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='gu').text+')')
def t_k():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='kn').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='kn').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='kn').text+')')
   L6.config(text='Gender'+'('+translator.translate('Gender',dest='kn').text+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='kn').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='kn').text+')')
   L7.config(text='Problem'+'('+translator.translate('Problem',dest='kn').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='kn').text+')')
def t_b():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='bn').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='bn').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='bn').text+')')
   L6.config(text='Gender'+'('+translator.translate('Gender',dest='bn').text+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='bn').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='bn').text+')')
   L7.config(text='Problem'+'('+translator.translate('Problem',dest='bn').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='bn').text+')')
def t_u():
   global p_a,pn_p,pn_w,L6,L5,L4,L7,L8
   translator = Translator()
   p_a.config(text='age'+'('+translator.translate('age',dest='ur').text+')')
   pn_p.config(text='Phone Number'+'('+translator.translate('PhoneNumber',dest='ur').text+')')
   pn_w.config(text='Weight'+'('+translator.translate('weight',dest='ur').text+')')
   L6.config(text='Gender'+'('+translator.translate('Gender',dest='ur').text+')')
   L5.config(text='Name'+'('+translator.translate('Name',dest='ur').text+')')
   L4.config(text="Enter Patient's Details"+'('+translator.translate('Enter Patient Details',dest='ur').text+')')
   L7.config(text='Problemf'+'('+translator.translate('Problem',dest='ur').text+')')
   L8.config(text='Medication'+'('+translator.translate('Medication',dest='ur').text+')')
def filling():
   global lan,p_name,weight,gender,age,p_no,prob,medi,name,problem,advice,tests,list1,entry3,entry0,pn_p_e,p_a_e,pn_w_e,Text1,Text2,check,TextA,TextT
   editB.config(state='active')
   text=text_1
   print(text)
   clearB.config(state='active')
   create_pdfB.config(state='active')
   lab_requestB.config(state='active')
   p_name=[]
   weight=''
   gender=''
   age=''
   p_no=[]
   prob=[]
   medi=[]
   name=''
   problem=''
   list1=''
   adv=[]
   test=[]
   advice=''
   tests=''
   #text=['name','Ram','age','20','gender','male','number','1234567891','weight','50','problem','headache','next','blood','cancer','medicine','trfdrs','Dolo 650']
   o=0
   while o<len(text):
      if(text[o]=="name"):
          o=o+1
          while((o!=len(text)) and (text[o]!="gender" and text[o]!="advice" and text[o]!="tests" and text[o]!="number" and text[o]!="problem" and text[o]!="cause" and text[o]!="medicine" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
               p_name.append(text[o])
               print(p_name)
               o=o+1
      elif(text[o]=="gender"):
               gender=text[o+1]
               o=o+2
      elif(text[o]=="number"):
            o=o+1
            #p_no.append(text[k+1])
            while((o!=len(text)) and (text[o]!="gender" and text[o]!="advice" and text[o]!="tests" and text[o]!="name" and text[o]!="medicine" and text[o]!="problem" and text[o]!="cause" and text[o]!="medication" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
               p_no.append(text[o])
               o=o+1;
      elif (text[o]=='age'):
          age=text[o+1]
          o=o+2
      elif(text[o]=='weight'):
          weight=text[o+1]
          o=o+2
      elif(text[o]=="problem" or text[o]=="cause"):
            o=o+1
            while((o!=len(text)) and (text[o]!="gender" and text[o]!="advice" and text[o]!="tests" and text[o]!="name" and text[o]!="number" and text[o]!="medicine" and text[o]!="medication" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
               prob.append(text[o])
               o=o+1
      elif(text[o]=="medicine" or text[o]=='medication'):
            o=o+1
            while((o!=len(text)) and (text[o]!="gender" and text[o]!="advice" and text[o]!="tests" and text[o]!="name" and text[o]!="problem" and text[o]!="cause" and text[o]!="number" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
              medi.append(text[o])
              o=o+1
      elif(text[o]=="advice"):
          o=o+1
          while((o!=len(text)) and (text[o]!="gender" and text[o]!="medication" and text[o]!="tests" and text[o]!="medicine" and text[o]!="name" and text[o]!="problem" and text[o]!="cause" and text[o]!="number" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
              adv.append(text[o])
              o=o+1
      elif(text[o]=="tests"):
          o=o+1
          while((o!=len(text)) and (text[o]!="gender" and text[o]!="medication" and text[o]!="advice" and text[o]!="medicine" and text[o]!="name" and text[o]!="problem" and text[o]!="cause" and text[o]!="number" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
              test.append(text[o])
              o=o+1
      else:
          o=o+1
   prob=list(prob)
   name=' '.join(p_name)
   p_no=''.join(p_no)
   problem=' '.join(prob)
   problem='\n'.join(problem.split(' next '))
   i=0
   advice=' '.join(adv)
   advice='\n'.join(advice.split(' next '))
   tests=' '.join(test)
   tests='\n'.join(tests.split(' next '))
   tablets=[]
   while len(medi)!=0:
       for j in range(len(medi)):
           if(medi[j]=='tablet' or medi[j]=='strips' or medi[j]=='strip' or medi[j]=='tablets' or medi[j]=='capsules' or medi[j]=='capsule'):
               i=j
               break
       #i=text.index('tablets')
       if i+1<len(medi) and medi[i+1]=='morning':
           i=i+1
       if i+1<len(medi) and medi[i+1]=='afternoon':
           i=i+1
       if i+1<len(medi) and medi[i+1]=='evening':
           i=i+1
       tablets.append(' '.join(medi[:i+1]))
       medi=medi[i+1:]
   list1='\n'.join(tablets)
   entry3.insert(END,name)
   entry0.insert(END,gender)
   pn_p_e.insert(END,p_no)
   p_a_e.insert(END,age)
   pn_w_e.insert(END,weight)
   Text1.insert(END,problem)
   Text2.insert(END,list1)
   TextA.insert(END,advice)
   TextT.insert(END,tests)
def speak():
  global ax
  #print(ax)
  if ax=='0' :
    #print('web')
    web()
  else:
    pass
#text=['name','xyz','def','problem','fever','and','cold','phone','number','970','19','26783','age','18','weight','26','medicine','dolo','650','MG','4','tablets','morning','evening','saradon','5','tablets','afternoon']
p_name=[]
weight=''
gender=''
age=''
p_no=[]
prob=[]
medi=[]
name=''
problem=''
list1=''
advice=''
tests=''
'''def on_click(event):
    entry.delete(0,END)
    send_b.configure(state='active')
    entry.configure(fg='black')
    entry.unbind('<Button-1>')
def on_focus(event)
#    if entry.get()!='':
    send_b.configure(state='active')'''
'''def user_Q():
    f2=Frame(window,bg='#4dff88',borderwidth=10)
    query=entry.get()
    entry.delete(0,END)
    label=Label(f2,text=query).pack(side='right')
    f2.pack(side=TOP,fill='x')
    f3=Frame(window,borderwidth=10)
    lpic=Label(f3,image=pic).pack(side='left')
    l=Label(f3,text='How can I help you ?').pack(side='left')
    f3.pack(side=TOP,fill='x')
'''
      #pdf.output(entry3.get()+".pdf")
#entry.insert(0,"Enter Your Query Here")
#entry.bind('<Button-1>',on_click)
#entry.bind('<FocusIn>',on_focus)
'''voiceicon=PhotoImage(file='microphone.png')
sendicon=PhotoImage(file='send.png')
send_b=Button(f1,image=sendicon,command=user_Q,state=DISABLED)
send_b.pack(side='left')
speech_b=Button(f1,image=voiceicon)
speech_b.pack(side='left')'''
def send_wapps():
   '''driver = webdriver.Chrome()
   driver.get('https://web.whatsapp.com/')

   name = entry3.get()
   filepath = 'D:\\'+entry3.get()+'.pdf'
   user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
   user.click()

   attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
   attachment_box.click()

   doc_box = driver.find_element_by_xpath(
       '//input[@accept="*"]')
   doc_box.send_keys(filepath)

   sleep(3)

   send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
   send_button.click()'''
   print(entry3.get())
   driver = webdriver.Chrome()
   driver.get('https://web.whatsapp.com/')
   x=input()
   name =entry3.get()
   filepath =os.getcwd()+'\\'+entry3.get()+'.pdf'
   sleep(7)
   try:
      user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
      user.click()
      print('ok')
      sleep(2)
      attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
      attachment_box.click()
      doc_box = driver.find_element_by_xpath('//input[@accept="*"]')
      doc_box.send_keys(filepath)
      print('harsha')
      sleep(7)
      send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
      send_button.click()
   except :
      driver.close()
      #driver.set_window_position(0, 0)
      #driver.set_window_size(0,0)
      messagebox.showerror('Error','Due to some reasons Whatsapp is not responding')
def destory_window():
     window_np.destroy()
def destroy_fw1():
  global f_window
  f_window.destroy()
def first_window(event=0):
   global f_window,window_np
   if type(window_np)!=type(2):
     window_np.destroy()
   def get_h():
       global window_h,d_hdw,E2_pn,E_eid,entry1_h,E_eid
       def save_hospital_d():
         global window_h,d_hdw
         d_hdw=entry1_h.get()+'$'+text_h.get('1.0',END)+'$'+E_eid.get()+'$'+E2_pn.get()
         hd=open('hospital_details.txt','+w')
         hd.write(d_hdw)
         hd.close()
         window_h.destroy()
         messagebox.showinfo("Information","Details are Saved Successfully")
       window_h=Toplevel()
       window_h.config(bg='#ff8484')
       window_h.title("Enter hospital's details")
       f11=Frame(window_h)
       f11.configure(background='#ff8484')
       L1_h=Label(f11,bg='#ff8484',text="Hospital's Name:",font=("Ariel",14))
       L1_h.pack(side='left')
       entry1_h=Entry(f11,borderwidth=3,width=35)
       entry1_h.pack(side='left')
       f11.pack(fill='x')
       f11_1=Frame(window_h,bg='#ff8484')
       L1_eid=Label(f11_1,text="              Email-id:",font=('Arial',14),bg='#ff8484')
       L1_eid.pack(side='left')
       E_eid=Entry(f11_1,borderwidth=3,width=35)
       E_eid.pack(side='left')
       f11_1.pack(fill='x')
       f11_2=Frame(window_h,bg='#ff8484')
       L2_pn=Label(f11_2,text="  Phone Number:",font=('Arial',14),bg='#ff8484')
       L2_pn.pack(side='left')
       E2_pn=Entry(f11_2,borderwidth=3,width=35)
       E2_pn.pack(side='left')
       f11_2.pack()
       f12=Frame(window_h)
       f12.configure(background='#ff8484')
       L2_h=Label(f12,bg='#ff8484',text="             Address:",font=("Ariel",14))
       L2_h.pack(side='left')
       text_h=Text(f12,borderwidth=3,width=26,height=6)
       text_h.pack(side='left')
       f12.pack(fill='x')
       f13=Frame(window_h)
       f13.configure(background='#ff8484')
       b1_h=Button(f13,text='save',command=save_hospital_d)
       b1_h.pack(side='top')
       f13.pack(fill='x')
       try:
           hdw=open('hospital_details.txt').read().split('$')
           entry1_h.insert(0,hdw[0])
           text_h.insert('1.0',hdw[1])
           E_eid.insert(0,hdw[2])
           E2_pn.insert(0,hdw[3])
       except FileNotFoundError:
           pass
       window_h.mainloop()
   def get_d():
       global window_d,entry1_d,entry2_d,spec_e,dept_e,ax,ddw
       global save_doctor_d
       def save_doctor_d(EVENT=0):
         global window_d,path
         x=entry1_d.get()+'$'+entry2_d.get()+'$'+spec_e.get()+'$'+dept_e.get()+'$'+path+'$'+str(ax)
         hd=open('doctor_details.txt','+w')
         hd.write(x)
         hd.close()
         window_d.destroy()
         messagebox.showinfo("Information","Details are saved Successfully")
       window_d=Toplevel()
       window_d.title("Enter Doctor's details")
       f11=Frame(window_d)
       f11.config(background='#ff8484')
       L1_h=Label(f11,bg='#ff8484',text="Doctor's Name:",font=("Ariel",14))
       L1_h.pack(side='left')
       entry1_d=Entry(f11,borderwidth=3,width=35)
       entry1_d.pack(side='left')
       f11.pack(fill='x')
       f12=Frame(window_d)
       f12.config(background='#ff8484')
       L2_h=Label(f12,bg='#ff8484',text="Phone number:",font=("Ariel",14))
       L2_h.pack(side='left')
       entry2_d=Entry(f12,borderwidth=3,width=35)
       entry2_d.pack(side='left')
       f12.pack(fill='x')
       f12_1=Frame(window_d,bg='#ff8484')
       spec=Label(f12_1,bg='#ff8484',text="Specilization    :",font=('Arial',14))
       spec.pack(side='left')
       spec_e=Entry(f12_1,borderwidth=3,width=35)
       spec_e.pack(side='left')
       f12_1.pack(fill='x')
       f12_2=Frame(window_d,bg='#ff8484')
       dept=Label(f12_2,text="Department     :",bg="#ff8484",font=('Arial',14))
       dept.pack(side='left')
       dept_e=Entry(f12_2,borderwidth=3,width=35)
       dept_e.bind('<Return>',save_doctor_d)
       dept_e.pack(side='left')
       f12_2.pack(fill='x')
       q0=Frame(window_d)
       q0.configure(bg='#ff8484')
       q0.pack(fill='x')
       f13=Frame(window_d)
       f13.configure(background='#ff8484')
       speechrecogB2=Button(f13,text="Select Speech recognition software",command=speech_reg)
       speechrecogB2.pack(side='left')
       f13.pack(fill='x')
       q0=Frame(window_d)
       q0.configure(bg='#ff8484')
       q0.pack(fill='x')
       f14=Frame(window_d,background='#ff8484')
       b0_h=Button(f14,text='Add Signature',command=add_sign)
       b0_h.pack(side='left')
       f14.pack(fill='x')
       q0=Frame(window_d)
       q0.configure(bg='#ff8484')
       q0.pack(fill='x')
       f15=Frame(window_d,background='#ff8484')
       b1_h=Button(f15,text='save',command=save_doctor_d)
       b1_h.pack(side='top')
       f15.pack(fill='x')
       entry1_d.insert(0,ddw[0])
       entry2_d.insert(0,ddw[1])
       spec_e.insert(0,ddw[2])
       dept_e.insert(0,ddw[3])
       window_d.mainloop()
   def rp():
     bl_rc_l.config(text='{} Patients'.format(6))
   def tpft():
     bl_c_l.config(text='            \t{} Patients'.format(6))
   def clear_rp(event=0):
     bl_rc_l.config(text='')
   def clear_tp(event=0):
     bl_c_l.config(text='                           ')
   global first_check
   f_window=Tk()
   f_window.configure(bg='#ff8484')
   f_window.geometry('700x650+200+2')
   #f_window.resizable(0,0)
   f_window.title('Voice Prescription')
   f_window.wm_attributes('-fullscreen','true')
   '''f0=Frame(f_window,bg='#ff8484')
   total_count=Label(f0,text="Total Count of patients : ",font=("Ariel",17),bg='#ff8484').pack(side='left')
   total_count_num=Label(f0,text="0",font=("Ariel",14),bg='#ff8484')
   total_count_num.pack(side='left')
   empt=Label(f0,text="   ",bg='#ff8484').pack(side='left')
   rem_count=Label(f0,text="Remaining Patients : ",font=("Ariel",17),bg='#ff8484').pack(side='left')
   rem_count_num=Label(f0,text="0",font=("Ariel",14),bg='#ff8484')
   rem_count_num.pack(side='left')
   f0.pack(fill='x')'''
   f0=Frame(f_window,bg='#ff8484')
   l_w=Label(f0,text='',bg='#ff8484').pack()
   f0.pack(fill='x')
   f1=Frame(f_window)
   f2=Frame(f_window,bg='#ff8484')
   f1.configure(background='#ff8484')
   b4=Button(f1,text="Reset Doctor's Details",borderwidth=4,command=get_d,font=("Ariel",14))
   b4.pack(side='right')
   wl_4=Label(f1,text="  ",bg='#ff8484').pack(side='right')
   b0=Button(f1,text="Reset Hospital's Details",borderwidth=4,command=get_h,font=("Ariel",14))
   b0.pack(side='right')
   b1_c=Button(f1,text='Total Count of Patients For Today',font=('Arial',14),borderwidth=4,command=tpft)
   b1_c.pack(side='left')
   bl_c_l=Label(f2,text='\t          ',bg='#ff8484',font=('Arial',16))
   bl_c_l.bind('<Button-1>',clear_tp)
   bl_c_l.pack(side='left')
   wl_4=Label(f1,text="  ",bg='#ff8484').pack(side='left')
   l_w=Label(f2,text='\t\t\t          ',bg='#ff8484').pack(side='left')
   b1_rc=Button(f1,text='Remaining Patients',font=('Arial',14),borderwidth=4,command=rp)
   b1_rc.pack(side='left')
   bl_rc_l=Label(f2,text='',bg='#ff8484',font=('Arial',16))
   bl_rc_l.bind('<Button-1>',clear_rp)
   bl_rc_l.pack(side='left')
   f1.pack(side='top',fill='x')
   f2.pack(fill='x')
   frame1=Frame(f_window,bg='#ff8484')
   frame1.config(width=350,height=250)
   frame1.pack(side='top',fill='both')
   b_l=Button(f_window,text='New Patient',width=15,command=new_patient,font=("Ariel",14))
   first_check=1
   b_l.pack(side='top')
   frame2=Frame(f_window,bg='#ff8484')
   frame2.pack(side='top',fill='both')
   l=Label(f_window,text=' ',bg='#ff8484')
   l.pack(side='top',fill='x')
   frame3=Frame(f_window,bg='#ff8484')
   frame3.pack(side='top',fill='both')
   b_2=Button(frame3,text='Old Patient',width=15,font=("Ariel",14),command=old_patient)
   b_2.pack()
   frame_empty=Frame(f_window,bg='#ff8484')
   lbl_emt=Label(frame_empty,bg='#ff8484').pack(fill='x')
   frame_empty.pack()
   fclose=Frame(f_window,bg='#ff8484')
   btn_cls=Button(fclose,text='Exit',command=destroy_fw1,font=("Ariel",14))
   btn_cls.pack()
   fclose.pack()
   f_window.mainloop()
def old_patient():
    def old_window(event=0):
      window_old.destroy()
      first_window()
    def getdetails():
        global name,gender,p_no,age,weight
        name='harsha'
        gender='male'
        p_no='7986410713'
        age='19'
        weight='70'
        window_old.destroy()
        new_patient()
    def clear(event=0):
        phone_e.delete(0,END)
        phone_e.config(fg='black')
        phone_e.unbind('<Button-1>')
    global first_check
    f_window.destroy()
    window_old=Tk()
    window_old.configure(bg='#ff8484')
    window_old.resizable(0,0)
    window_old.wm_attributes('-fullscreen','true')
    window_old.title('Old Patient Portal')
    f_back=Frame(window_old,bg='#ff8484')
    back_image=PhotoImage(file="Back_Arrow.png")
    back_label=Label(f_back,image=back_image,bg='#ff8484')
    back_label.pack(side='left')
    back_label.bind('<Button-1>',old_window)
    f_back.pack(fill='x')
    frame_w=Frame(window_old,bg='#ff8484')
    label_w=Label(frame_w,bg='#ff8484',text='').pack()
    frame_w.pack()
    frame_info=Frame(window_old,bg='#ff8484')
    label_pn=Label(frame_info,text='Phone Number : ',bg='#ff8484',font=('Arial',20))
    label_pn.pack(side='left')
    phone_e=Entry(frame_info,font=('Arial',20),fg='#D3D3D3')
    phone_e.insert(0,'Ex: 7986410563')
    phone_e.bind('<Button-1>',clear)
    phone_e.pack(side='left')
    first_check=0
    label_w=Label(frame_info,text='               ',bg='#ff8484').pack(side='left')
    button=Button(frame_info,text='Get Details',font=('Monaco',13),command=getdetails)
    button.pack(side='left')
    frame_info.pack(fill='x')
    window_old.mainloop()
def new_patient():
   global first_check
   def rp_np():
     bl_rc_l.config(text='{} Patients'.format(6))
   def tpft_np():
     bl_c_l.config(text='            \t{} Patients'.format(6))
   def clear_rp(event=0):
     bl_rc_l.config(text='')
   def clear_tp(event=0):
     bl_c_l.config(text='                           ')
   def destory_window_np():
     window_np.destroy()
   if first_check==1:
     f_window.destroy()
     first=0
   global window_np,lan,p_name,weight,gender,advice,tests,age,p_no,prob,medi,name,problem,list1,entry3,entry0,pn_p_e,p_a_e,pn_w_e,Text1,Text2,TextA,TextT,text,p_a,pn_p,pn_w,L6,L5,L4,L7,L8,mail_pdfB,clearB,editB,lab_requestB,create_pdfB,print_pdfB,preview_pdfB,send_pdfB,merge_pdfB
   window_np=Tk()
   window_np.configure(bg='#ff8484')
   window_np.geometry('700x650+200+2')
   window_np.resizable(0,0)
   window_np.wm_attributes('-fullscreen','true')
   window_np.title('Prescription')
   f_back=Frame(window_np,bg='#ff8484')
   back_image=PhotoImage(file="Back_Arrow.png")
   back_label=Label(f_back,image=back_image,bg='#ff8484')
   back_label.pack(side='left')
   back_label.bind('<Button-1>',first_window)
   f_back.pack(fill='x')
   f1=Frame(window_np,bg='#ff8484')
   f2=Frame(window_np,bg='#ff8484')
   b1_c=Button(f1,text='Total Count of Patients For Today',font=('Arial',14),borderwidth=4,command=tpft_np)
   b1_c.pack(side='left')
   bl_c_l=Label(f2,text='\t          ',bg='#ff8484',font=('Arial',16))
   bl_c_l.bind('<Button-1>',clear_tp)
   bl_c_l.pack(side='left')
   wl_4=Label(f1,text="  ",bg='#ff8484').pack(side='left')
   l_w=Label(f2,text='\t\t\t          ',bg='#ff8484').pack(side='left')
   b1_rc=Button(f1,text='Remaining Patients',font=('Arial',14),borderwidth=4,command=rp_np)
   b1_rc.pack(side='left')
   bl_rc_l=Label(f2,text='',bg='#ff8484',font=('Arial',16))
   bl_rc_l.bind('<Button-1>',clear_rp)
   bl_rc_l.pack(side='left')
   speechrecogB1=Button(f1,text="Select Speech recognition software",borderwidth=4,command=speech_reg,font=("Ariel",14))
   speechrecogB1.pack(side='right')
   f1.pack(side='top',fill='x')
   f2.pack(fill='x')
   menubar=Menu(window_np)
   set_speech=Menu(menubar,tearoff=0)
   languages=['Bengali','Gujarati','Kannada','Malayalam','Marathi','Tamil','Telugu','Urdu']
   set_speech.add_command(label='English',command=s_e)
   set_speech.add_command(label='Hindi',command=s_h)
   set_speech.add_command(label='Telugu',command=s_te)
   set_speech.add_command(label='Tamil',command=s_ta)
   set_speech.add_command(label='Kanada',command=s_k)
   set_speech.add_command(label='Malayalam',command=s_mal)
   set_speech.add_command(label='Marathi',command=s_mar)
   set_speech.add_command(label='Bengali',command=s_b)
   set_speech.add_command(label='Gujarati',command=s_g)
   set_speech.add_command(label='Urdu',command=s_u)
   menubar.add_cascade(label='Speech_language',menu=set_speech)
   set_text=Menu(menubar,tearoff=0)
   set_text.add_command(label='English',command=t_e)
   set_text.add_command(label='Hindi',command=t_h)
   set_text.add_command(label='Telugu',command=t_te)
   set_text.add_command(label='Tamil',command=t_ta)
   set_text.add_command(label='Kanada',command=t_k)
   set_text.add_command(label='Malayalam',command=t_mal)
   set_text.add_command(label='Marathi',command=t_mar)
   set_text.add_command(label='Bengali',command=t_b)
   set_text.add_command(label='Gujarati',command=t_g)
   set_text.add_command(label='Urdu',command=t_u)
   menubar.add_cascade(label='Text_language',menu=set_text)
   window_np.config(menu=menubar)
   new_pf2=Frame(window_np)
   new_pf2.configure(background='#ff8484')
   L4=Label(new_pf2,bg='#ff8484',text="Enter Patient's detials:",font=("Ariel",16))
   L4.pack(side='left')
   previous_p=Button(new_pf2,text='Previous Prescription',font=('Ariel',13),borderwidth=4)
   previous_p.pack(side='right')
   l_w=Label(new_pf2,text='       ',bg='#ff8484').pack(side='right')
   lab_report=Button(new_pf2,text="Lab Report",font=('Ariel',13),borderwidth=4)
   lab_report.pack(side='right')
   new_pf2.pack(side=TOP,fill='x')
   new_pf3=Frame(window_np)
   new_pf3.configure(background='#ff8484')
   L5=Label(new_pf3,bg='#ff8484',text="Name:",font=("Ariel",14))
   L5.pack(side='left')
   entry3=Entry(new_pf3,borderwidth=3,width=38)
   entry3.insert(END,name)
   entry3.pack(side='left')
   L6=Label(new_pf3,bg='#ff8484',text="Gender:             ",font=("Ariel",14))
   L6.pack(side='left')
   entry0=Entry(new_pf3,borderwidth=3,width=20)
   entry0.insert(END,gender)
   entry0.pack(side='left')
   new_pf3.pack(fill='x')
   '''w_f4=Frame(window_np)
   w_f4.config(bg='#ff8484')
   w_l_f4=Label(w_f4,text=' ',bg='#ff8484').pack()
   w_f4.pack(fill='x')'''
   f4_1=Frame(window_np)
   f4_1.config(bg='#ff8484')
   pn_p=Label(f4_1,text='Phone Number:    ',font=("Ariel",14),bg='#ff8484')
   pn_p.pack(side='left')
   pn_p_e=Entry(f4_1,borderwidth=3,width=22)
   pn_p_e.pack(side='left')
   pn_p_e.insert(0,p_no)
   p_a=Label(f4_1,text='      Age:            ',font=("Ariel",14),bg='#ff8484')
   p_a.pack(side='left')
   p_a_e=Entry(f4_1,borderwidth=3,width=20)
   p_a_e.pack(side='left')
   p_a_e.insert(0,age)
   f4_1.pack(fill='x')
   f4_2=Frame(window_np)
   f4_2.config(bg='#ff8484')
   pn_w=Label(f4_2,text='Weight:                 ',font=("Ariel",14),bg='#ff8484')
   pn_w.pack(side='left')
   pn_w_e=Entry(f4_2,borderwidth=3,width=20)
   pn_w_e.pack(side='left')
   pn_w_e.insert(0,weight)
   f4_2.pack(fill='x')
   f5=Frame(window_np)
   f5.configure(background='#ff8484')
   L7=Label(f5,bg='#ff8484',text="Problem:",font=("Ariel",16))
   L7.pack(side='left')
   L7=Label(f5,bg='#ff8484',text='\t\t\t\t\t\t\t\t\t\t\t        ')
   L7.pack(side='right')
   L7=Label(f5,bg='#ff8484',text="Advice:",font=("Ariel",16))
   L7.pack(side='right')
   f5.pack(fill='x')
   f6=Frame(window_np)
   f6.configure(background='#ff8484')
   Text1=Text(f6,borderwidth=3,height=6,width=62)
   Text1.insert(END,problem)
   Text1.pack(side='left')
   TextA=Text(f6,borderwidth=3,height=6,width=50)
   TextA.insert(END,advice)
   TextA.pack(side='top')
   f6.pack(fill='x')
   f7=Frame(window_np)
   f7.configure(background='#ff8484')
   L8=Label(f7,bg='#ff8484',text="Medication:",font=("Ariel",16))
   L8.pack(side='left')
   L7=Label(f7,bg='#ff8484',text='\t\t\t\t\t\t\t\t\t\t\t\t')
   L7.pack(side='right')
   L7=Label(f7,bg='#ff8484',text="Tests:",font=("Ariel",16))
   L7.pack(side='right')
   f7.pack(fill='x')
   f8=Frame(window_np)
   f8.configure(background='#ff8484')
   Text2=Text(f8,borderwidth=3,height=10,width=62)
   Text2.insert(END,list1)
   Text2.pack(side='left')
   TextT=Text(f8,borderwidth=3,height=10,width=50)
   TextT.insert(END,problem)
   TextT.pack(side='top')
   f8.pack(fill='x')
   f9=Frame(window_np)
   f9.configure(background='#ff8484')
   L9=Label(f9,bg='#ff8484')
   L9.pack()
   f9.pack(fill='x')
   f10=Frame(window_np)
   f10.configure(background='#ff8484')
   b1=Button(f10,text='START',command=speak,font=("Ariel",14))
   b1.pack(side='left')
   '''wl_1=Label(f10,text="  ",bg='#ff8484').pack(side='left')
   b1=Button(f10,text='Stop',command=web_c).pack(side='left')'''
   wl_1=Label(f10,text="  ",bg='#ff8484')
   wl_1.pack(side='left')
   editB=Button(f10,text='Edit with Speech',command=make_changes,state='disabled',font=("Ariel",14))
   editB.pack(side='left')
   wl_2=Label(f10,text="  ",bg='#ff8484')
   wl_2.pack(side='left')
   clearB=Button(f10,text='CLEAR',command=clear,font=("Ariel",14),state='disabled')
   clearB.pack(side='left')
   l_w=Label(f10,text='\t\t\t\t\t\t\t  ',bg='#ff8484')
   l_w.pack(side='right')
   lab_requestB=Button(f10,text='Request to Lab',command=lab_request,font=("Ariel",14))
   lab_requestB.pack(side='right')
   f10.pack(fill='x')
   path=''
   f21_w=Frame(window_np)
   f21_w.config(bg='#ff8484')
   l_f21w=Label(f21_w,text=' ',bg='#ff8484').pack()
   f21_w.pack(fill='x')
   f21=Frame(window_np)
   f21.configure(background='#ff8484')
   create_pdfB=Button(f21,text="CREATE PDF",command=pdf,font=("Ariel",14))
   create_pdfB.pack(side='left')
   l6_1=Label(f21,text=' ',bg='#ff8484')
   l6_1.pack(side='left')
   preview_pdfB=Button(f21,text='Preview pdf',command=open_pdf,font=("Ariel",14),state='disabled')
   preview_pdfB.pack(side='left')
   l6_1=Label(f21,text=' ',bg='#ff8484')
   l6_1.pack(side='left')
   send_pdfB=Button(f21,text='Send pdf via Whatsapp',command=send_wapps,font=("Ariel",14),state='disabled')
   send_pdfB.pack(side='left')
   f21.pack(fill='x')
   f33_w=Frame(window_np,bg='#ff8484')
   l_f33_w=Label(f33_w,text=' ',bg='#ff8484')
   l_f33_w.pack()
   f33_w.pack(fill='x')
   f33=Frame(window_np,bg='#ff8484')
   merge_pdfB=Button(f33,text="Merge PDF",font=("Ariel",14),state='disabled')
   merge_pdfB.pack(side='left')
   l7_1=Label(f33,text=' ',bg='#ff8484')
   l7_1.pack(side='left')
   print_pdfB=Button(f33,text='Print PDF',command=printing,font=("Ariel",14),state='disabled')
   print_pdfB.pack(side='left')
   l7_1=Label(f33,text=' ',bg='#ff8484')
   l7_1.pack(side='left')
   mail_pdfB=Button(f33,text='Send PDF By Mail',command=mailpdf,font=("Ariel",14),state='disabled')
   mail_pdfB.pack(side='left')
   f33.pack(fill='x')
   closeB=Button(f33,text='Close',command=destory_window_np,font=("Ariel",14))
   closeB.pack()
   #messagebox.showinfo('Information','when you are speaking about problem please say the keyword next after every problem\nEX:- Problem cough next cold next fever')
   window_np.mainloop()
window_np=0
#initial_video()
first_window()
