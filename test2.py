from itertools import tee
from wsgiref import headers
from requests_html import HTMLSession


import dearpygui.dearpygui as dpg


session = HTMLSession()
temperature =""

def getMeteo (lieu):
    #f permet d'y ajouter un parametre
    url =f'https://www.google.com/search?q=meteo+{lieu}'
    r = session.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'})


    #first permet de recuperer le premier element renvoyé
    temperature = r.html.find('span#wob_tm',first=True).text


    #cherche wob_t dans vk_bk.wob-unit
    unite = r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text
    print(temperature+unite)

    #cherche la description
    description = r.html.find('span#wob_dc',first=True).text
    print(description)


    #cherche l'humidité
    humidité = r.html.find('span#wob_hm',first=True).text
    print("humidité : "+humidité)

    #prochains jours
    #description = r.html.find('div.R3Y3ec.rr3bxd',first=True).find()
    prochainsJours = r.html.find('div.wob_df',first=True).text
    print(prochainsJours)
    return "Metéo actuelle à "+lieu+" : "+temperature+unite+" \nHumidité à "+humidité+""



def changerLieu(sender,data,userdata):
    dpg.set_value("affichage",getMeteo(dpg.get_value("oui")))



texteMeteo = getMeteo('riviere+du+loup')


dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Ma météo :"):
    dpg.add_text(texteMeteo,tag = "affichage")
    dpg.add_button(label="bouton",callback=changerLieu)
    dpg.add_input_text(tag = "oui")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
