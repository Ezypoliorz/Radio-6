import json
import tkinter as tk
import customtkinter as ctk
import os
from subprocess import Popen, PIPE, STDOUT

username = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split('Users/')[1].split('/')[0]
repository_path = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split(username)[0] + username + "/Documents/GitHub/Radio-6"

path = repository_path + "/calendar.json"
titre = ""
date = ""
description = ""
image = ""

def WriteJson() :
    global path
    global titre
    global date
    global description
    global image
    données = {}
    données["titre"] = titre
    données["date"] = date
    données["description"] = description
    données["image"] = image
    with open(path, 'w') as f:
        json.dump(données, f, indent=4)

    p = Popen(repository_path + "/UploadGitHub.bat", shell=True, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = p.communicate()

def GetImage():
    global image
    global bouton_url_image
    global label_url_image
    bouton_url_image.configure(text="Changer l'affiche")
    image = tk.filedialog.askopenfilename(title="Sélectionner l'affiche",
                                                       filetypes=(("Fichiers JPG", "*.jpg"), ("Fichiers PNG", "*.png"), ("Tous les fichiers", "*.*")))
    label_url_image.configure(text=f"Affiche sélectionnée : " + image.split("Affiches/")[-1])
    image = "Affiches" + str(image.split("Affiches")[-1])

def GetInfos():
    global entrée_date
    global entrée_titre
    global entrée_infos
    global titre
    global date
    global description
    titre = entrée_titre.get()
    date = entrée_date.get()
    description = entrée_infos.get()
    WriteJson()


app = ctk.CTk()
app.geometry("700x400")
app.title("EditCalendar")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

entrée_titre = ctk.CTkEntry(master=app, placeholder_text="Titre de l'émission", width=200)
entrée_titre.pack(pady=10)

entrée_date = ctk.CTkEntry(master=app, placeholder_text="Date de l'émission", width=200)
entrée_date.pack(pady=10)

entrée_infos = ctk.CTkEntry(master=app, placeholder_text="Description de l'émission", width=200)
entrée_infos.pack(pady=10)

label_url_image = ctk.CTkLabel(master=app, text="Aucune affiche sélectionnée", width=165)
label_url_image.pack(pady=5)

bouton_url_image = ctk.CTkButton(master=app, text="Sélectionner une affiche", command=GetImage)
bouton_url_image.pack(pady=0)

bouton_titre_date_audio = ctk.CTkButton(master=app, text="Confirmer les informations", command=GetInfos, fg_color="white", text_color="black", hover_color="grey")
bouton_titre_date_audio.pack(pady=30)

app.mainloop()