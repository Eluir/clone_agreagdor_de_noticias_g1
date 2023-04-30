import requests
from bs4 import BeautifulSoup
import csv
import webbrowser
from tkinter import *
import textwrap

def fx_search_news(subject_var, list_box_news):
    """
    funcao que realiza a busca no site com base no texto do user e alimenta o list box e gera arquivo csv
    com titulo, descricao e link de acesso
    """

    url_base = 'https://g1.globo.com/busca/?q='

    # obetem o texto informado pelo user
    search = subject_var.get()

    # faz a requisição pro site do G1 com o tema informado
    answer = requests.get(url_base + search)

    # formata o resultado em HTML
    site = BeautifulSoup(answer.text, 'html.parser')

    # busca toda as DIV que contem o conteudo das noticias
    news = site.findAll('div', attrs={'class': 'widget--info__text-container'})

    # contador de itens
    list_box_index = 0

    # lista com headers da planilha
    news_list = [['title', 'description', 'link']]

    # iteração por cada item da lista de DIV de conteudo
    for new in news:
        # identificando o titulo das materias
        title = new.find('div', attrs={'class': 'widget--info__title'}).text

        # identificando a descricao da materia
        description = new.find('p', attrs={'class': 'widget--info__description'}).text

        # identificando bloco com o link
        link = new.find('a')

        # montando o link com caminho correto
        link = 'https:' + link['href']

        # removendo os espaços com fatiamento
        title = title[9:-7]

        # adicionando elementos na lista que ira gerar o csv
        news_list.append([title, description, link])

        # inserindo titulo e posicao no list box da tela
        list_box_news.insert(list_box_index, title)

        # incrementando valor
        list_box_index += 1

    with open(file= "news_clone.csv", mode="w") as csv_file:
        writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
        writer.writerows(news_list)

def fx_news_details(list_box):

    title = list_box.get(list_box.curselection())

    csv_file = open(file= "news_clone.csv", mode='r')
    table = csv.reader(csv_file, delimiter=';', lineterminator='\n')

    for row in table:
        if (row[0] == title):
            news = row
            break

    window_top = Toplevel()
    window_top.title('DETALHAMENTO DE NOTÍCIAS')
    # window_top.geometry('400x250')
    window_top.configure(padx = 20)
    window_top.configure(bg='grey25')

    # Wraping the news description
    title = textwrap.fill(news[0], 60)
    descricao = textwrap.fill(news[1], 60)

    label_title = Label(window_top, text=title, font=('Verdana', 14, 'bold'))
    label_title.configure(fg='grey99', bg='grey25')
    label_title.pack(pady=10)

    label_description = Label(window_top, text=descricao, font=('Verdana', 11))
    label_description.configure(fg='grey99', bg='grey25')
    label_description.pack(pady=10)

    button_open = Button(window_top, text='ABRIR NO NAVEGADOR', command = lambda : webbrowser.open(news[2]), font=('Verdana', 8, 'bold'))
    button_open.pack(pady=10)