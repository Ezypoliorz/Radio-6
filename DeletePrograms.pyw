import tkinter as tk # Tkinter : Interface graphique
import customtkinter as ctk # CustomTkinter : Version améliorée de Tkinter
from bs4 import BeautifulSoup # BeautifulSoup : Récupération de fichiers HTML
import os # OS : Gestion des fichiers et répertoires
import re 

def SupprimerEmission(entrée_titre, app):
    titre = entrée_titre.get()

    label_état = ctk.CTkLabel(master=app, text="")

    with open(str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/") + "/émissions.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        balise_titre = soup.find('h2', string=titre)
        if balise_titre :
            div_émission = balise_titre.parent.parent.parent
            div_émission.decompose()
            label_état.configure(text=f"L'émission \"{titre}\" et ses chroniques ont été supprimées !")
        else :
            label_état.configure(text=f"L'émission \"{titre}\" n'existe pas", text_color="red")
        
    with open(str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/") + "/podcasts-chroniques-scientifiques.html", "r", encoding="utf-8") as s:
        soup_s = BeautifulSoup(s, "html.parser")
        if soup_s.find('h2', string=re.compile(re.escape(f"{titre} - "))):
            soup_s.find('h2', string=re.compile(re.escape(f"{titre} - "))).parent.parent.parent.decompose()
            s.write(soup_s.prettify())
        s.close()

    with open(str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/") + "/podcasts-chroniques-touristiques.html", "r", encoding="utf-8") as t:
        soup_t = BeautifulSoup(t, "html.parser")
        if soup_t.find('h2', string=re.compile(re.escape(f"{titre} - "))):
            soup_t.find('h2', string=re.compile(re.escape(f"{titre} - "))).parent.parent.parent.decompose()
            t.write(soup_t.prettify())
        t.close()

    with open(str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/") + "/podcasts-chroniques-culturelles.html", "r", encoding="utf-8") as c:
        soup_c = BeautifulSoup(c, "html.parser")
        if soup_c.find('h2', string=re.compile(re.escape(f"{titre} - "))):
            soup_c.find('h2', string=re.compile(re.escape(f"{titre} - "))).parent.parent.parent.decompose()
            c.write(soup_c.prettify())
        c.close()

    with open(str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/") + "/podcasts-portraits.html", "r", encoding="utf-8") as p:
        soup_p = BeautifulSoup(p, "html.parser")
        if soup_p.find('h2', string=re.compile(re.escape(f"{titre} - "))):
            soup_p.find('h2', string=re.compile(re.escape(f"{titre} - "))).parent.parent.parent.decompose()
            p.write(soup_p.prettify())
        p.close()

    label_état.pack(pady=10)

app = ctk.CTk()
app.geometry("400x700")
app.title("EditWebsite")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

entrée_titre = ctk.CTkEntry(master=app, placeholder_text="Titre de l'émission à supprimer", width=200)
entrée_titre.pack(pady=10)

bouton_titre_date = ctk.CTkButton(master=app, text="Supprimer", command=lambda: SupprimerEmission(entrée_titre, app))
bouton_titre_date.pack(pady=10)

app.mainloop()