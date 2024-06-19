import tkinter as tk
from tkinter import filedialog

def open_file():
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath,'r',encoding='utf-8') as phb:
            for line in phb:
                line = ''.join(line.split())
                if line!='':
                        record = dict(zip(fields, line.split(','))) 	
                        phone_book.append(record)
    # Add items to the listbox
    for i in phone_book:  
        listbox.insert(tk.END, '   '.join(i.values()))	
    return phone_book


window = tk.Tk()
phone_book=[]
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')  
menu = tk.Menu(window)  
new_item = tk.Menu(menu)  
new_item.add_command(label='Открыть',command=open_file)  
menu.add_cascade(label='Файл', menu=new_item)  
window.config(menu=menu)  
listbox = tk.Listbox(window)
listbox.pack(anchor=tk.NW, fill=tk.BOTH, padx=5, pady=5)





window.mainloop()

