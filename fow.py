from tkinter import *
import wikipedia
def get_me():
    entryvalue=textbox.get()
    answer=wikipedia.summary(entryvalue)
    try:
        text.delete('1.0',END)
    except:
        pass
    text.insert(INSERT,answer)
root = Tk()
root.title('New Window')
root.geometry('500x700')
topframe=Frame(root,height=150)
textbox=Entry(topframe)
textbox.grid(row=0,column=0)
btn=Button(topframe,text='Search',command=get_me)
btn.grid(row=0,column=1)
topframe.pack(side=TOP)
bottomframe=Frame(root)
scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill=Y)
text=Text(bottomframe,yscrollcommand=scroll.set,wrap=WORD)
scroll.config(command=text.yview)
text.pack(side=TOP)
bottomframe.pack(side=TOP)
root.mainloop()