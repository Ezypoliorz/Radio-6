#  » DeletePrograms
#  » © Web Radio du lycée Arcisse de Caumont, 2025

import tkinter as tk # Tkinter : Interface graphique
import customtkinter as ctk # CustomTkinter : Version améliorée de Tkinter
from bs4 import BeautifulSoup # BeautifulSoup : Récupération de fichiers HTML
import os # OS : Gestion des fichiers et répertoires
import re
from subprocess import Popen, PIPE, STDOUT # Subprocess : Exécution du fichier Batch
import sys
import time

username = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split('Users/')[1].split('/')[0]
repository_path = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split(username)[0] + username + "/Documents/GitHub/Radio-6"

def SupprimerEmission(entrée_titre, app):
    titre = entrée_titre.get()

    label_état = ctk.CTkLabel(master=app, text="")

    with open(repository_path + "/émissions.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        f.close()
    balise_titre = soup.find('h2', string=titre)
    if balise_titre :
        div_émission = balise_titre.parent.parent.parent
        div_émission.decompose()
        soup.find("div", {"class": "div-programme-background"}).decompose()
        with open(repository_path + "/émissions.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
            f.close()
        label_état.configure(text=f"L'émission \"{titre}\" et ses chroniques ont été supprimées !")
    else :
        label_état.configure(text=f"L'émission \"{titre}\" n'existe pas", text_color="red")
        
    with open(repository_path + "/podcasts-chroniques-scientifiques.html", "r", encoding="utf-8") as s:
        soup_s = BeautifulSoup(s, "html.parser")
        s.close()
    if soup_s.find('h2', string=re.compile(re.escape(f"{titre} - "))):
        soup_s.find('h2', string=re.compile(re.escape(f"{titre} - "))).parent.parent.parent.decompose()
        with open(repository_path + "/podcasts-chroniques-scientifiques.html", "w", encoding="utf-8") as s:
            s.write(soup_s.prettify())
            s.close()

    with open(repository_path + "/podcasts-chroniques-culturelles.html", "r", encoding="utf-8") as c:
        soup_c = BeautifulSoup(c, "html.parser")
        c.close()
    if soup_c.find('h2', string=re.compile(re.escape(f"{titre} - "))):
        soup_c.find('h2', string=re.compile(re.escape(f"{titre} - "))).parent.parent.parent.decompose()
        with open(repository_path + "/podcasts-chroniques-culturelles.html", "w", encoding="utf-8") as c:
            c.write(soup_c.prettify())
            c.close()

    with open(repository_path + "/podcasts-chroniques-touristiques.html", "r", encoding="utf-8") as t:
        soup_t = BeautifulSoup(t, "html.parser")
        t.close()
    if soup_t.find('h2', string=re.compile(re.escape(f"{titre} - "))):
        soup_t.find('h2', string=re.compile(re.escape(f"{titre} - "))).parent.parent.parent.decompose()
        with open(repository_path + "/podcasts-chroniques-scientifiques.html", "w", encoding="utf-8") as t:
            t.write(soup_t.prettify())
            t.close()

    with open(repository_path + "/podcasts-portraits.html", "r", encoding="utf-8") as p:
        soup_p = BeautifulSoup(p, "html.parser")
        p.close()
    if soup_p.find('h2', string=re.compile(re.escape(f"{titre} - "))):
        soup_p.find('h2', string=re.compile(re.escape(f"{titre} - "))).parent.parent.parent.decompose()
        with open(repository_path + "/podcasts-portraits.html", "w", encoding="utf-8") as p:
            p.write(soup_p.prettify())
            p.close()

    p = Popen(repository_path + "/UploadGitHub.bat", shell=True, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = p.communicate()

    label_état.pack(pady=10)

    time.sleep(5)
    app.destroy()
    sys.exit()

app = ctk.CTk()
app.geometry("700x400")
app.title("EditWebsite")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

entrée_titre = ctk.CTkEntry(master=app, placeholder_text="Titre de l'émission à supprimer", width=200)
entrée_titre.pack(pady=10)

bouton_titre_date = ctk.CTkButton(master=app, text="Supprimer", command=lambda: SupprimerEmission(entrée_titre, app))
bouton_titre_date.pack(pady=10)

app.mainloop()