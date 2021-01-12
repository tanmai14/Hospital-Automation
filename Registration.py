from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import re
global window,windowPD,windowMR,windowAD
global p_p_noE,p_e_idE
def multiple_registration():
    def mul_register():
        messagebox.showinfo('Information',"All Patients are Registered Succesfully")
    windowMR=Tk()
    windowMR.configure(bg='#ff8484')
    windowMR.resizable(0,0)
    windowMR.geometry('880x460+220+260')
    mr1F=Frame(windowMR,bg='#ff8484')
    p_p_noMRL=Label(mr1F,text='       Patients Phone Number:\t   ',font=("Ariel",16),bg='#ff8484')
    p_p_noMRL.pack(side='left')    
    p_e_idMRL=Label(mr1F,text='Patients Email ID:\t            ',font=("Ariel",16),bg='#ff8484')
    p_e_idMRL.pack(side='left')   
    c_d_nameMRL=Label(mr1F,text='Consulting Doctor Name:',font=("Ariel",16),bg='#ff8484')
    c_d_nameMRL.pack(side='left')
    mr1F.pack(fill='x')
    spaceF=Frame(windowMR,bg='#ff8484')
    spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
    spaceF.pack()
    p_p_noMRE=[1,2,3,4,5,6]
    p_e_idMRE=[1,2,3,4,5,6]
    c_d_nameMRE=[1,2,3,4,5,6]
    for i in range(6):
        mr2F=Frame(windowMR,bg='#ff8484')
        spaceL=Label(mr2F,text=i+1,bg='#ff8484',font=("Ariel",20)).pack(side='left')
        spaceL=Label(mr2F,text='. ',bg='#ff8484',font=("Ariel",20)).pack(side='left')
        p_p_noMRE[i]=Entry(mr2F,width=20,font=("Ariel",18))
        p_p_noMRE[i].pack(side='left')
        spaceL=Label(mr2F,text=' ',bg='#ff8484').pack(side='left')
        p_e_idMRE[i]=Entry(mr2F,width=20,font=("Ariel",18))
        p_e_idMRE[i].pack(side='left')
        spaceL=Label(mr2F,text=' ',bg='#ff8484').pack(side='left')
        c_d_nameMRE[i]=Entry(mr2F,width=20,font=("Ariel",18))
        c_d_nameMRE[i].pack(side='left')
        mr2F.pack(fill='x')
        spaceF=Frame(windowMR,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
    regMRF=Frame(windowMR,bg='#ff8484')
    regMRB=Button(regMRF,text='REGISTER',borderwidth=4,font=("Ariel",18),command=mul_register)
    regMRB.pack()
    regMRF.pack(fill='x')
    windowMR.mainloop()
    pass
def p_all_doctors():
    windowAD=Tk()
    windowAD.configure(bg='#ff8484')
    windowAD.geometry('+220+250')
    windowAD.resizable(0,0)
    ad1F=Frame(windowAD,bg='#ff8484')
    d_nameADL=Label(ad1F,text='      Doctor Name:\t\t',font=("Ariel",18),bg='#ff8484')
    d_nameADL.pack(side='left')    
    departADL=Label(ad1F,text='Department:\t         ',font=("Ariel",18),bg='#ff8484')
    departADL.pack(side='left')
    no_pADL=Label(ad1F,text='      Number of Patients:',font=("Ariel",18),bg='#ff8484')
    no_pADL.pack(side='left')
    ad1F.pack(fill='x')
    spaceF=Frame(windowAD,bg='#ff8484')
    spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
    spaceF.pack()
    d_nameADL=[1,2,3,4,5,6]
    departADL=[1,2,3,4,5,6]
    no_pADL=[1,2,3,4,5,6]
    for i in range(6):
        ad2F=Frame(windowAD,bg='#ff8484')
        spaceL=Label(ad2F,text=i+1,bg='#ff8484',font=("Ariel",20)).pack(side='left')
        spaceL=Label(ad2F,text='. ',bg='#ff8484',font=("Ariel",20)).pack(side='left')
        d_nameADL[i]=Label(ad2F,text='',width=20,font=("Ariel",18))
        d_nameADL[i].pack(side='left')
        spaceL=Label(ad2F,text=' ',bg='#ff8484').pack(side='left')
        departADL[i]=Label(ad2F,text='',width=20,font=("Ariel",18))
        departADL[i].pack(side='left')
        spaceL=Label(ad2F,text=' :',bg='#ff8484',font=("Ariel",20)).pack(side='left')
        no_pADL[i]=Label(ad2F,text='',width=20,font=("Ariel",18))
        no_pADL[i].pack(side='left')
        spaceL=Label(ad2F,text=' ',bg='#ff8484').pack(side='left')
        ad2F.pack(fill='x')
        spaceF=Frame(windowAD,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
    windowAD.mainloop()
    pass
def total_reg_today():
    def clear_par_DL(Event=0):
        t_reg_toDL.config(text='')
    t_reg_toDL=Label(t_reg_toDF,text='{} Registrations'.format('6'),font=("Ariel",18),bg='#ff8484')
    t_reg_toDL.pack(side='left')
    t_reg_toDL.bind('<Button-1>',clear_par_DL)
def p_at_doctor():
    def submit_pd(Event=0):
        no_PDL.config(text='{} Patients'.format('6'))
    windowPD=Tk()
    windowPD.configure(bg='#ff8484')
    windowPD.geometry('+450+335')
    windowPD.resizable(0,0)
    spaceF=Frame(windowPD,bg='#ff8484')
    spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
    spaceF.pack()
    d_namePDF=Frame(windowPD,bg='#ff8484')
    d_namePDL=Label(d_namePDF,text=' Doctor Name :',font=("Ariel",20),bg='#ff8484')
    d_namePDL.pack(side='left')
    d_namePDE=Entry(d_namePDF,width=20,font=("Ariel",18))
    d_namePDE.bind('<Return>',submit_pd)
    d_namePDE.pack(side='left')    
    spaceL=Label(d_namePDF,text=' ',font=("Ariel",20),bg='#ff8484')
    spaceL.pack(side='left')
    d_namePDF.pack(fill='x')
    spaceF=Frame(windowPD,bg='#ff8484')
    spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
    spaceF.pack()
    subPDF=Frame(windowPD,bg='#ff8484')
    subPDB=Button(subPDF,text='SUBMIT',borderwidth=4,font=("Ariel",14),command=submit_pd)
    subPDB.pack()
    subPDF.pack(fill='x')
    no_PDF=Frame(windowPD,bg='#ff8484')
    no_PDL=Label(no_PDF,text='',font=("Ariel",20),bg='#ff8484')
    no_PDL.pack()
    no_PDF.pack(fill='x')
    windowPD.mainloop()
def register():
    p_p_no=p_p_noE.get()
    p_e_id=p_e_idE.get()
    if len(p_p_no)==10:
        try:
            int(p_p_no)
            if(re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',p_e_id)):
                messagebox.showinfo('Information',"Patient Registered Succesfully")
            else:
               messagebox.showinfo('Information',"Need Valid Gmail")
        except:
            messagebox.showinfo('Information',"Entered Phone Number is not Valid")
    else:
        messagebox.showinfo('Information',"Entered Phone Number is not a Valid Indian Phone Number")
def close():
    window.destroy()
window=Tk()
window.configure(bg='#ff8484')
window.resizable(0,0)
window.wm_attributes('-fullscreen','true')
t_reg_toDF=Frame(window,bg='#ff8484')
t_reg_toDB=Button(t_reg_toDF,text='Total Number Registrations for Today',borderwidth=4,font=("Ariel",16),command=total_reg_today)
t_reg_toDB.pack(side='left')
t_reg_toDF.pack(fill='x')
for i in range(2):
    spaceF=Frame(window,bg='#ff8484')
    spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
    spaceF.pack()
p_p_noF=Frame(window,bg='#ff8484')
p_p_noL=Label(p_p_noF,text='\t\t\tPatients Phone Number  :',font=("Ariel",20),bg='#ff8484')
p_p_noL.pack(side='left')
p_p_noE=Entry(p_p_noF,width=20,font=("Ariel",18))
p_p_noE.pack(side='left')
p_p_noF.pack(fill='x')
spaceF=Frame(window,bg='#ff8484')
spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
spaceF.pack()
p_e_idF=Frame(window,bg='#ff8484')
p_e_idL=Label(p_e_idF,text='\t\t\tPatients Email ID\t        :',font=("Ariel",20),bg='#ff8484')
p_e_idL.pack(side='left')
p_e_idE=Entry(p_e_idF,width=20,font=("Ariel",18))
p_e_idE.pack(side='left')
p_e_idF.pack(fill='x')
spaceF=Frame(window,bg='#ff8484')
spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
spaceF.pack()
c_d_nameF=Frame(window,bg='#ff8484')
c_d_nameL=Label(c_d_nameF,text='\t\t\tConsulting Doctor Name :',font=("Ariel",20),bg='#ff8484')
c_d_nameL.pack(side='left')
c_d_nameE=Entry(c_d_nameF,width=20,font=("Ariel",18))
c_d_nameE.pack(side='left')
c_d_nameF.pack(fill='x')
spaceF=Frame(window,bg='#ff8484')
spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
spaceF.pack()
regF=Frame(window,bg='#ff8484')
regB=Button(regF,text='Register',font=("Ariel",18),borderwidth=4,command=register)
regB.pack()
regF.pack(fill='x')
spaceF=Frame(window,bg='#ff8484')
spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
spaceF.pack()
mul_regF=Frame(window,bg='#ff8484')
mul_regB=Button(mul_regF,text='Multiple Registration',borderwidth=4,font=("Ariel",18),command=multiple_registration)
mul_regB.pack()
mul_regF.pack(fill='x')
no_of_p_DF=Frame(window,bg='#ff8484')
spaceF=Frame(window,bg='#ff8484')
spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
spaceF.pack()
no_of_p_DB=Button(no_of_p_DF,text='Number of Patients at Particular Doctor',borderwidth=4,font=("Ariel",18),command=p_at_doctor)
no_of_p_DB.pack()
no_of_p_DF.pack(fill='x')
no_of_p_par_DF=Frame(window,bg='#ff8484')
spaceF=Frame(window,bg='#ff8484')
spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
spaceF.pack()
no_of_p_par_DB=Button(no_of_p_par_DF,text='Number of Patients at all Doctors',borderwidth=4,font=("Ariel",18),command=p_all_doctors)
no_of_p_par_DB.pack()
no_of_p_par_DF.pack(fill='x')
spaceF=Frame(window,bg='#ff8484')
spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
spaceF.pack(side='bottom')
closeF=Frame(window,bg='#ff8484')
closeB=Button(closeF,text='Close',font=("Ariel",18),borderwidth=4,command=close)
closeB.pack()
closeF.pack(side='bottom',fill='x')
window.mainloop()
#window.geometry('700x650+200+2')