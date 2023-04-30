from tkinter import *
from backend_clone import *

# CRIANDO TELA 
window = Tk()
window.title("AGREGADOR DE NOTÍCIAS")
window.config(background="grey25")
window.config(padx=20, pady=20)
window.resizable(width=False, height=False)

# CRIANDO FRAMES 
main = Frame(window)
main.config(bg="grey25")
main.pack()

buttons = Frame(window)
buttons.config(bg="grey99")
buttons.pack()

# variaveis
subject_var = StringVar()
# subject_var.set("pesquise aqui:")

# WIDGETS

label_title = Label(main, text="NOTÍCIAS")
label_title.configure(bg="grey25", fg='grey99', font=('Verdana', 18, 'bold'))
label_title.pack(pady=(5, 10))

label_subject = Label(main, text="ASSUNTO PARA PESQUISA:")
label_subject.configure(bg="grey25", fg='grey99', font=('Verdana', 8, 'bold'))
label_subject.pack(anchor=W, pady=(5, 2))


entry_subject = Entry(main, textvariable=subject_var)
entry_subject.bind("<Return>", lambda event: fx_search_news(subject_var, list_box_news))
entry_subject.configure(width=122, bg="grey25", fg='grey99', font=('Verdana', 10, 'bold'))
entry_subject.pack(pady=(5, 10))

label_results = Label(main, text="RESULTADOS:")
label_results.configure(bg="grey25", fg='grey99', font=('Verdana', 10, 'bold'))
label_results.pack(anchor=W, pady=(5, 2))

list_box_news = Listbox(main)
list_box_news.bind("<Double-1>", lambda event: fx_news_details(list_box_news))
list_box_news.configure(width=138, bg="grey25", fg='grey99', font=('Verdana', 10), justify='left')
list_box_news.pack(pady=(5, 10))


button_open = Button(buttons, text="VER DETALHES", command=lambda: fx_news_details(list_box_news), font=('Verdana', 8, 'bold'))
button_open.configure(bg="grey25", fg="white")
button_open.grid(row=0)


window.mainloop()
