import random
import re
import tkinter as tk
import tkinter.messagebox

window=tk.Tk()
window.title("HANGMAN in Python")
window.geometry("750x750")
window.configure(bg='black')

title=tk.PhotoImage(file="titlee.png")
titleLabel=tk.Label(window,image=title)
title.image=title
titleLabel.pack()

space1=tk.Label(window,text='',bg='black')
space1.pack()

attempts=7
choices=tk.IntVar()
choices.set(attempts-1)

chosen_word=''
word_status=[]
guessed_letters=[]
rguess=tk.StringVar()
rguess.set('Remaining Attempts:'+str(choices.get()))

image_paths=['hang.png','6.png','5.png','4.png','3.png','2.png','1.png','title.png']
img=tk.PhotoImage(file=image_paths[attempts])
imgLabel=tk.Label(window,image=img)
img.image=img
imgLabel.pack()

def fill_word(chosen_word,word_status):
    pre=random.randrange(1,3)
    for i in range(pre):
        pos=random.randrange(0,len(chosen_word))
        word_status[pos]=chosen_word[pos]
    
def guess(entry,guessLabel,wordLabel):
    global guessed_letters
    global chosen_word
    global word_status
    global attempts
    global rguess
    global choices
    
    aguess='Already Guessed! You have already guessed:'
    wguess='Incorrect guess!'

    x=entry.get()
    if (x.isalpha()!=1):
        tk.messagebox.showinfo(message='Please enter a letter')
        entry.delete(0,'end')
        return
    x=x.lower()
    
    if x in guessed_letters:
        aguess=aguess+','.join(guessed_letters)+' letters'
        tk.messagebox.showinfo(message=aguess)
        entry.delete(0,'end')
        return
    
    guessed_letters.append(x)
    occurences=[]
    occurence=re.finditer(x,chosen_word)
    for i in occurence:
        occurences.append(i.start())
    if(len(occurences)==0):
        
        attempts-=1
        choices.set(attempts)
        tk.messagebox.showinfo(message=wguess)
        rguess.set('Remaining attempts:'+str(choices.get()))
        entry.delete(0,'end')
    else:
        for posi in occurences:
            word_status[posi]=chosen_word[posi]
        entry.delete(0,'end')
        wordLabel.configure(text=' '.join(word_status))
        
    guessLabel.configure(text=rguess.get())
    guessLabel.text=rguess.get()
         
    imaget=tk.PhotoImage(file=image_paths[choices.get()])
    imgLabel.configure(image=imaget)
    imgLabel.image=imaget

    if attempts==0:
        word='Oops! You lost this time, word was '+chosen_word
        tk.messagebox.showinfo(message=word)
        window.destroy()
    elif(chosen_word==''.join(word_status)):
        win='Yippe! You won'
        tk.messagebox.showinfo(message=win)
        window.destroy()
    else:
        return
    
        
        
def start(wlist):
    global window
    global chosen_word
    global word_status
    global attempts
    global play
    global quitb
    global space2
    global image_paths
    
    attempts-=1
    file=open(wlist)
    words=file.read().split('\n')
    totalw=len(words)
    chosen_word=words[random.randrange(0,totalw)]
    word_status=['_' for i in range(len(chosen_word))]
    fill_word(chosen_word,word_status)
    space3=tk.Label(window,text='',bg='black')
    space3.pack()

    imaget=tk.PhotoImage(file=image_paths[attempts])
    imgLabel.configure(image=imaget)
    imgLabel.image=imaget
    
    play.pack_forget()
    quitb.pack_forget()
    space2.pack_forget()
    get_status=' '.join(word_status)
    wordLabel=tk.Label(window,text=get_status,font=('TimesNewRoman','30'),bd=5,bg='white')
    wordLabel.pack()

    guessLabel=tk.Label(window,text=rguess.get(),font=('TimesNewRoman','20'),fg='white',bg='black')
    guessLabel.pack()
    
    
    get_status=' '.join(word_status)
    wordLabel.configure(text=get_status)
        
    spacen=tk.Label(window,text='',bg='black')
    spacen.pack()

    entryLabel=tk.Label(window,text='Guess here',font=('TimesNewRoman','20'),fg='white',bg='black')
    entryLabel.pack()
    entry=tk.Entry(window,font='TimesNewRoman')
    entry.pack()

    spacex=tk.Label(window,text='',bg='black')
    spacex.pack()

    guessb=tk.Button(window,text='Submit',font=('TimesNewRoman','20'),command= lambda:guess(entry,guessLabel,wordLabel))
    guessb.pack()
                    
def quitg():
    window.destroy()
    
    
space2=tk.Label(window,text='',bg='black')
space2.pack()

play=tk.Button(window,text='PLAY',width=20,height=2,font='Elephant',bd=5,bg='white',command=lambda:start('words.txt'))
play.pack()
quitb=tk.Button(window,text='QUIT',width=20,height=2,font='Elephant',bd=5,bg='white',command=lambda:quitg())
quitb.pack()




