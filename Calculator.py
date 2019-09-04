from tkinter import *
import math
op=["",""]
sign=""
hist=""
i=0
window=Tk()
window.title("Scientific Calculator")
l1=Label(text="SCIENTIFIC CALCULATOR")
l1.grid(row=0,columnspan=10)
t2=Text(window,height=1,width=49)
t2.grid(row=1,columnspan=9)
t1=Text(window,height=1,width=49)
t1.grid(row=2,column=0,columnspan=9)
t1.config(state=DISABLED)
t2.config(state=DISABLED)
def Number(number):
    if (number==1):
        t1.config(state=NORMAL)
        t1.insert(END,"1")
        charproc("1")
        t1.config(state=DISABLED)
    elif (number==2):
        t1.config(state=NORMAL)
        t1.insert(END,"2")
        charproc("2")
        t1.config(state=DISABLED)
    elif (number==3):
        t1.config(state=NORMAL)
        t1.insert(END,"3")
        charproc("3")
        t1.config(state=DISABLED)
    elif (number==4):
        t1.config(state=NORMAL)
        t1.insert(END,"4")
        charproc("4")
        t1.config(state=DISABLED)
    elif (number==5):
        t1.config(state=NORMAL)
        t1.insert(END,"5")
        charproc("5")
        t1.config(state=DISABLED)
    elif (number==6):
        t1.config(state=NORMAL)
        t1.insert(END,"6")
        charproc("6")
        t1.config(state=DISABLED)
    elif (number==7):
        t1.config(state=NORMAL)
        t1.insert(END,"7")
        charproc("7")
        t1.config(state=DISABLED)
    elif (number==8):
        t1.config(state=NORMAL)
        t1.insert(END,"8")
        charproc("8")
        t1.config(state=DISABLED)
    elif (number==9):
        t1.config(state=NORMAL)
        t1.insert(END,"9")
        charproc("9")
        t1.config(state=DISABLED)
    elif (number==0):
        t1.config(state=NORMAL)
        t1.insert(END,"0")
        charproc("0")
        t1.config(state=DISABLED)
    elif (number=="dec"):
        t1.config(state=NORMAL)
        t1.insert(END,".")
        charproc("dec")
        t1.config(state=DISABLED)
    elif (number=="+"):
        t1.config(state=NORMAL)
        t1.insert(END,"+")
        charproc("+")
        t1.config(state=DISABLED)
    elif (number=="-"):
        t1.config(state=NORMAL)
        t1.insert(END,"-")
        charproc("-")
        t1.config(state=DISABLED)
    elif (number=="x"):
        t1.config(state=NORMAL)
        t1.insert(END,"x")
        charproc("x")
        t1.config(state=DISABLED)
    elif (number=="/"):
        t1.config(state=NORMAL)
        t1.insert(END,"/")
        charproc("/")
        t1.config(state=DISABLED)
    elif (number=="="):
        charproc("=")
    elif (number=="clr"):
        t1.config(state=NORMAL)
        t2.config(state=NORMAL)
        t1.delete(1.0,END)
        t2.delete(1.0,END)
        charproc("clr")
        t1.config(state=DISABLED)
        t2.config(state=DISABLED)
    elif (number=="del"):
        charproc("del")

def charproc(ch):
    global i
    global op
    global sign
    global hist
    if ch in ["+","-","x","/","="]:
        if (ch!="="):
            sign+=ch
        if (len(sign)>1 or ch=="="):
            if (ch!="="):
                t2.config(state=NORMAL)
                t2.insert(END,hist+str(op[1]))
                t2.config(state=DISABLED)
            if (sign[0]=="+"):
                op[0]=float(op[0])+float(op[1])
            elif (sign[0]=="-"):
                op[0]=float(op[0])-float(op[1])
            elif (sign[0]=="x"):
                op[0]=float(op[0])*float(op[1])
            elif (sign[0]=="/"):
                op[0]=float(op[0])/float(op[1])
            i=1
            if (ch=="="):
                ch=""
            hist=ch
            op[1]=""
            t1.config(state=NORMAL)
            t1.delete(1.0,END)
            t1.insert(END,str(op[0])+ch)
            t1.config(state=DISABLED)
            sign=ch
        else :
            i=1
            hist=str(op[0])+ch
    elif (ch.isdigit()==TRUE):
        op[i]+=ch
    elif (ch=="dec"):
        op[i]+="."
    elif (ch=="sin"):
        op[i]=math.sin(float(op[i]))
        Otherfunc("sin",i,hist,op[i])
    elif (ch=="cos"):
        op[i]=math.cos(float(op[i]))
        Otherfunc("cos",i,hist,op[i])
    elif (ch=="tan"):
        op[i]=math.tan(float(op[i]))
        Otherfunc("tan",i,hist,op[i])
    elif (ch=="exp"):
        op[i]=math.exp(float(op[i]))
        Otherfunc("exp",i,hist,op[i])
    elif (ch=="divx"):
        op[i]=1/float(op[i])
        Otherfunc("divx",i,hist,op[i])
    elif (ch=="pi"):
        op[i]=3.14159
        Otherfunc("pi",i,hist,op[i])
    elif (ch=="log"):
        op[i]=math.log10(float(op[i]))
        Otherfunc("exp",i,hist,op[i])
    elif (ch=="fact"):
        op[i]=math.factorial(float(op[i]))
        Otherfunc("exp",i,hist,op[i])
    elif (ch=="sqrt"):
        op[i]=math.sqrt(float(op[i]))
        Otherfunc("exp",i,hist,op[i])
    elif (ch=="clr"):
        op[0]=""
        op[1]=""
        sign=""
        i=0
        hist=""
    elif (ch=="del"):
        if (t1.get("1.end-1c").isdigit()==TRUE):
            op[i]=op[i][0:len(op[i])-1]
            print(op[i])
            t1.config(state=NORMAL)
            t1.delete("1.end-1c")
            t1.config(state=DISABLED)
        elif t1.get("1.end -1c") in ["+","-","x","/"]:
            sign=sign[0:len(sign)-1]
            t1.config(state=NORMAL)
            t1.delete("1.end-1c")
            t1.config(state=DISABLED)
def Otherfunc(f,i,s,h):
    if (i==0):
        t1.config(state=NORMAL)
        t1.delete(1.0,END)
        t1.insert(END,h)
        t1.config(state=DISABLED)
    if (i==1):
        t1.config(state=NORMAL)
        t1.delete(1.0,END)
        t1.insert(END,s+str(h))
        t1.config(state=DISABLED)
def Basu():
    t1.config(state=NORMAL)
    t2.config(state=NORMAL)
    t2.insert(END,"Crafted by")
    t1.insert(END,"Arnab Basu")
    t1.config(state=DISABLED)
    t2.config(state=DISABLED)
bclr=Button(window,text="CLR",width=5,height=1,command=lambda:Number("clr"))
bclr.grid(row=1,column=9)
bdel=Button(window,text="DEL",width=5,height=1,command=lambda:Number("del"))
bdel.grid(row=2,column=9)
b1=Button(window,text="1",width=5,height=2,command=lambda:Number(1))
b1.grid(row=3,column=6)
b2=Button(window,text="2",width=5,height=2,command=lambda:Number(2))
b2.grid(row=3,column=7)
b3=Button(window,text="3",width=5,height=2,command=lambda:Number(3))
b3.grid(row=3,column=8)
b4=Button(window,text="4",width=5,height=2,command=lambda:Number(4))
b4.grid(row=4,column=6)
b5=Button(window,text="5",width=5,height=2,command=lambda:Number(5))
b5.grid(row=4,column=7)
b6=Button(window,text="6",width=5,height=2,command=lambda:Number(6))
b6.grid(row=4,column=8)
b7=Button(window,text="7",width=5,height=2,command=lambda:Number(7))
b7.grid(row=5,column=6)
b8=Button(window,text="8",width=5,height=2,command=lambda:Number(8))
b8.grid(row=5,column=7)
b9=Button(window,text="9",width=5,height=2,command=lambda:Number(9))
b9.grid(row=5,column=8)
bdec=Button(window,text=".",width=5,height=2,command=lambda:Number("dec"))
bdec.grid(row=6,column=6)
b0=Button(window,text="0",width=5,height=2,command=lambda:Number(0))
b0.grid(row=6,column=7)
beq=Button(window,text="=",width=5,height=2,command=lambda:Number("="))
beq.grid(row=6,column=8)
badd=Button(window,text="+",width=5,height=2,command=lambda:Number("+"))
badd.grid(row=3,column=9)
bsub=Button(window,text="-",width=5,height=2,command=lambda:Number("-"))
bsub.grid(row=4,column=9)
bmul=Button(window,text="x",width=5,height=2,command=lambda:Number("x"))
bmul.grid(row=5,column=9)
bdiv=Button(window,text="/",width=5,height=2,command=lambda:Number("/"))
bdiv.grid(row=6,column=9)

bpow=Button(window,text="x^y",width=5,height=2)
bpow.grid(row=3,column=0)
bsin=Button(window,text="sin",width=5,height=2,command=lambda:charproc("sin"))
bsin.grid(row=4,column=0)
bisin=Button(window,text="inv(sin)",width=5,height=2)
bisin.grid(row=5,column=0)
b=Button(window,text="",width=5,height=2,command=Basu)
b.grid(row=6,column=0)

bsqrt=Button(window,text="root(x)",width=5,height=2,command=lambda:charproc("sqrt"))
bsqrt.grid(row=3,column=1)
bcos=Button(window,text="cos",width=5,height=2,command=lambda:charproc("cos"))
bcos.grid(row=4,column=1)
bicos=Button(window,text="inv(cos)",width=5,height=2)
bicos.grid(row=5,column=1)
bpi=Button(window,text="pi",width=5,height=2,command=lambda:charproc("pi"))
bpi.grid(row=6,column=1)

blog=Button(window,text="log(x)",width=5,height=2,command=lambda:charproc("log"))
blog.grid(row=3,column=2)
btan=Button(window,text="tan",width=5,height=2,command=lambda:charproc("tan"))
btan.grid(row=4,column=2)
bitan=Button(window,text="inv(tan)",width=5,height=2)
bitan.grid(row=5,column=2)
bneg=Button(window,text="-ve",width=5,height=2)
bneg.grid(row=6,column=2)

bexp=Button(window,text="e^x",width=5,height=2,command=lambda: charproc("exp"))
bexp.grid(row=3,column=3)
bdivx=Button(window,text="1/x",width=5,height=2,command=lambda:charproc("divx"))
bdivx.grid(row=4,column=3)
bfact=Button(window,text="x !",width=5,height=2,command=lambda:charproc("fact"))
bfact.grid(row=5,column=3)
bmod=Button(window,text="%",width=5,height=2)
bmod.grid(row=6,column=3)

l2=Label(text="          ")
l2.grid(row=3,column=4,rowspan=4,columnspan=1)
l2=Label(text="          ")
l2.grid(row=3,column=5,rowspan=4,columnspan=1)
window.mainloop()
