#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from PIL import Image, ImageTk
from differents_dico import *

def click_result():
    abcdef = champ.get().lower()
    if not abcdef in dico:
        champ.configure(bg = 'IndianRed')
        return
    else:
        champ.configure(bg = 'white')

    im1 = Image.open(dico[abcdef][0])
    print()

    image_pictogramme = ImageTk.PhotoImage(im1)
    label_pictogramme.configure(image = image_pictogramme)
    label_pictogramme.image = image_pictogramme

    classe = dico[abcdef][1]
    text_classe.insert(END, dicoclasse[classe])

    mentions = '\n'.join([dico[abcdef][2][i] + ' : ' + dicomention[dico[abcdef][2][i]] for i in range(len(dico[abcdef][2]))])
    text_mentions.insert(END, mentions)

dicoclasse = {   
    "C01" : "'Explosibles, explosible instable','Explosibles, division 1.1','Explosibles, division 1.2','Explosibles, division 1.3','Explosibles, division 1.4','Substances et mélanges autoréactifs, type A','Substances et mélanges autoréactifs, type B','Peroxydes organiques, type A','Peroxydes organiques, type B'",
    "C02" : "'Gaz inflammables, catégories 1, 2','Aérosols, catégories 1, 2','Liquides inflammables, catégories 1, 2, 3','Matières solides inflammables, catégories 1, 2','Substances et mélanges autoréactifs, types B, C, D, E, F','Liquides pyrophoriques, catégorie 1','Matières solides pyrophoriques, catégorie 1','Substances et mélanges auto-échauffants, catégories 1, 2','Substances et mélanges qui, au contact de l’eau, dégagent des gaz inflammables, catégories 1, 2, 3','Peroxydes organiques, types B, C, D, E, F'",
    "C03" : "'Gaz comburants, catégorie 1','Liquides comburants, catégorie 1','Liquides comburants, catégorie 2','Liquides comburants, catégorie 3','Matières solides comburantes, catégorie 1','Matières solides comburantes, catégorie 2','Matières solides comburantes, catégorie 3'",
    "C04" : "'gaz comprimés','gaz liquéfiés','gaz liquéfiés réfrigérés','gaz dissous'",
    "C05" : "'Substances ou mélanges corrosifs pour les métaux, catégorie 1','Corrosion cutanée/irritation cutanée, catégorie 1A','Corrosion cutanée/irritation cutanée, catégorie 1B','Corrosion cutanée/irritation cutanée, catégorie 1C','Lésions oculaires graves/irritation oculaire, catégorie 1'",
    "C06" : "'Toxicité aiguë par voie orale, catégorie 1,2,3', 'Toxicité aiguë par voie cutanée, catégorie 1,2,3','Toxicité aiguë par inhalation, catégorie 1,2,3'",
    "C07" : "'Toxicité aiguë par voie orale, catégorie 4','Toxicité aiguë par voie cutanée, catégorie 4','Toxicité aiguë par inhalation, catégorie 4','Corrosion cutanée/irritation cutanée, catégorie 2','Lésions oculaires graves/irritation oculaire, catégorie 2','Sensibilisation cutanée, catégories 1, 1A, 1B','Toxicité spécifique pour certains organes cibles - Exposition unique, catégorie 3','Dangereux pour la couche d'ozone, catégorie 1'",
    "C08" : "'Sensibilisation respiratoire, catégories 1, 1A, 1B','Mutagénicité sur les cellules germinales, catégorie 1A','Mutagénicité sur les cellules germinales, catégorie 1B','Mutagénicité sur les cellules germinales, catégorie 2','Cancérogénicité, catégorie 1A','Cancérogénicité, catégorie 1B','Cancérogénicité, catégorie 2','Toxicité pour la reproduction, catégorie 1A','Toxicité pour la reproduction, catégorie 1B','Toxicité pour la reproduction, catégorie 2','Toxicité spécifique pour certains organes cibles - Exposition unique, catégorie 1','Toxicité spécifique pour certains organes cibles - Exposition unique, catégorie 2','Toxicité spécifique pour certains organes cibles - Exposition répétée, catégorie 1','Toxicité spécifique pour certains organes cibles - Exposition répétée, catégorie 2','Danger par aspiration, catégorie 1'",
    "C09" : "'Danger pour le milieu aquatique, toxicité à court terme (aiguë), catégorie 1','Danger pour le milieu aquatique, toxicité à long terme (chronique), catégorie 1 et 2'",
    }


dico = {
    'sgh01': ['SGH-01.jpg','C01',['H200','H201','H202','H203','H204','H205','H240','H241']],
    'sgh02': ['SGH-02.jpg','C02',['H220','H221','H222','H229','H224','H225','H226','H228','H241','H242','H250','H251','H252','H260','H261']],
    'sgh03': ['SGH-03.jpg','C03',['H270','H271','H272']],
    'sgh04': ['SGH-04.jpeg','C04',[]],
    'sgh05': ['SGH-05.jpeg','C05',['H290','H314','H318']],
    'sgh06': ['SGH-06.jpeg','C06',['H300','H310','H330','H301','H311','H331']],
    'sgh07': ['SGH-07.jpeg','C07',['H302','H312','H332','H315','H319','H317','H335','H336','H420']],
    'sgh08': ['SGH-08.jpeg','C08',['H334','H340','H341','H350','H351','H360','H361','H370','H371','H372','H373','H304']],
    'sgh09': ['SGH-09.jpeg','C09',['H400','H410','H411']],
    }

number_row=0
root = Tk()
w = Label (root, text="Entrez le nom du produit.")
w.grid(row=number_row, column=1)
number_row += 1

champ=Entry(root)
champ.grid(row=number_row, column=1)
number_row += 1


button_results= Button(root,text="Résultats", command=click_result)
button_results.grid(row=number_row,column=1)
number_row += 1


label_numero = Label (root, text = "Numéro CAS", font = "Helvetica 14 bold")
label_numero.grid(row=number_row)
number_row += 1


label_numero = Text (root, height = 2, width = 10)
label_numero.grid(row=number_row)
number_row += 1


label_formule = Label (root, text = "Formule chimique", font = "Helvetica 14 bold")
label_formule.grid(row=number_row)
number_row += 1

label_formule = Text (root, height = 2, width = 15)
label_formule.grid(row=number_row)
number_row += 2

image_bienvenue= Image.open("bienvenue.png")
image_pictogramme= ImageTk.PhotoImage(image_bienvenue)
label_pictogramme = Label (root, image= image_pictogramme)
label_pictogramme.grid(row=number_row)

number_row = 3
#repartir_colonne_droite_ligne3

label_classe = Label (root, text = "Classe du produit", font = "Helvetica 14 bold")
label_classe.grid(row=number_row, column=1)
number_row += 1


text_classe = Text(root, height = 6, width = 100)
text_classe.grid(row=number_row, column=1)
number_row += 1


label_mentions = Label (root, text = "Mentions de danger", font = "Helvetica 14 bold")
label_mentions.grid(row=number_row, column=1)
number_row += 1


text_mentions = Text(root, height = 6, width = 100)
text_mentions.grid(row=number_row, column=1)
number_row += 1


label_prudence = Label (root, text = "Mentions de prudence", font = "Helvetica 14 bold")
label_prudence.grid(row=number_row, column=1)
number_row += 1


text_prudence = Text(root, height = 6, width = 100)
text_prudence.grid(row=number_row, column=1, sticky=N)
number_row += 1


d= Button(root,text="Quitter", command=root.quit)
d.grid(row=number_row, column=1)
number_row += 1


root.mainloop()

try:
    root.destroy()
except:
    pass

