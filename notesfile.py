from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def open_file():
    file_path = filedialog.askopenfilename(title= "File Change", filetypes=(('Text docs (*.txt)', '*.txt'), ('All types', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='UTF-8').read())

def notes_close():
    ask = messagebox.askokcancel('Exit', 'Do you want to close notes?')
    if ask:
        root.destroy()

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Text docs (*.txt)', '*.txt'), ('All types', '*.*')))
    f = open(file_path, 'w', encoding='UTF-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()        

root = Tk()
root.title("NoteBook") # name
root.geometry("600x300") # size
text = Text(root,width=400,height=400)#параметры самого теста при печати
text.pack() 
menu_bar=Menu(root) # менюбар
file_menu = Menu(menu_bar, tearoff=0) # тянет информацию из меню бара

file_menu.add_command(label="OPEN",command=open_file) # создание нового файла
file_menu.add_command(label ="SAVE",command=save_file) # открытие файла
file_menu.add_command(label ="CLOSE",command=notes_close)# сохранить как
root.config(menu=file_menu)
root.config(menu=menu_bar)

menu_bar.add_cascade(label ="File",menu = file_menu) # button File in menuBar
root.config(menu=menu_bar)
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text, bg='white', fg='black', padx=15, pady=15, wrap=WORD, insertbackground="grey", width=15)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop() # основное окно
