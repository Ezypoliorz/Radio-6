#  » EditWebsite
#  » © Web Radio du lycée Arcisse de Caumont, 2025

import tkinter as tk
import customtkinter as ctk
from bs4 import BeautifulSoup
import sys
import os
from pydub import AudioSegment
from subprocess import Popen, PIPE, STDOUT


titre_émission = "Titre"
date_émission = "Date"
url_audio_émission = "Émissions/Musique test 3.mp3"
id_number = 0

username = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split('Users/')[1].split('/')[0]
repository_path = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split(username)[0] + username + "/Documents/GitHub/Radio-6"

AudioSegment.converter = "ffmpeg"

def AjouterSujets(chroniques, noms_chroniques, noms_fichiers_chroniques, liste_temps_programme_réel, sujets, audio, titre, date, entrée_chronique_scientifique, entrée_chronique_culturelle, entrée_chronique_touristique, entrée_portraits, app):

    if entrée_chronique_scientifique.get() != None:
        sujets["Chronique scientifique"] = entrée_chronique_scientifique.get()

    if entrée_chronique_culturelle.get() != None:
        sujets["Chronique culturelle"] = entrée_chronique_culturelle.get()

    if entrée_chronique_touristique.get() != None:
        sujets["Chronique touristique"] = entrée_chronique_touristique.get()

    if entrée_portraits.get() != None:
        sujets["Portrait"] = entrée_portraits.get()

    app.destroy()
    
    for i in range(len(noms_chroniques)) :
        if noms_chroniques[i] in chroniques :
            temps_chronique_début = chroniques[noms_chroniques[i]]
            temps_chronique_fin = liste_temps_programme_réel[liste_temps_programme_réel.index(temps_chronique_début)+1]
            sujet_chronique = sujets[noms_chroniques[i]]

            audio_chronique = AudioSegment.from_file(audio)
            audio_chronique = audio_chronique[temps_chronique_début*1000:temps_chronique_fin*1000]
            audio_chronique = audio_chronique.fade_in(1500)
            audio_chronique = audio_chronique.fade_out(1500)
            audio_chronique.export(f"{noms_chroniques[i]} - {sujet_chronique}.wav", format="WAV")

            source_path = f"{noms_chroniques[i]} - {sujet_chronique}.wav"
            destination_path = f"Émissions/{noms_chroniques[i]} - {sujet_chronique}.wav"
            os.rename(source_path, destination_path)

            source_path = "/chemin/vers/le/fichier/source.txt"
            destination_path = "/chemin/vers/le/nouveau/dossier/destination.txt"

            with open(repository_path + noms_fichiers_chroniques[noms_chroniques[i]], "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                print("soup ", soup)

            id_number = int(soup.find("audio", {"class": "audio"})["id"].split("Audio")[-1]) + 1

            html_ajout_chroniques = f"""

    <div class="div-émission-background">
        <div class="div-émission">
            <div class="infos-émission">
                <h2 class="titre-émission">{sujet_chronique}</h2>
                <h3 class="date-émission">{titre} - {date}</h3>
            </div>

            <div class="div-audio-podcasts">
                <audio controls class="audio" id="Audio{id_number}">
                    <source src="{noms_chroniques[i]} - {sujet_chronique}.mp3" type="audio/mpeg">
                    Votre navigateur ne supporte pas l'élément audio.
                </audio>
            </div>
        </div>
    </div>

"""
            soup_ajout_chroniques = BeautifulSoup(html_ajout_chroniques, "html.parser")

            div = soup.find("div", {"class": "conteneur-podcasts"})
            div.insert(0, soup_ajout_chroniques)

            with open(repository_path + noms_fichiers_chroniques[noms_chroniques[i]], "w", encoding="utf-8") as f:
                f.write(str(soup))
                f.close()

    p = Popen(repository_path + "/UploadGitHub.bat", shell=True, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = p.communicate()

def AjouterEmission(titre, date, audio, programme) :
    with open(repository_path + "/émissions.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    id_number = int(soup.find("div", {"class": "infos"})["id"].split("Infos")[-1]) + 1
    id_programme = ""
    temps_programme = ""
    temps_programme_réel = 0
    liste_temps_programme_réel = []
    noms_chroniques = ["Chronique scientifique", "Chronique culturelle", "Chronique touristique", "Portrait"]
    chroniques = {}
    sujets = {}
    noms_fichiers_chroniques = {"Chronique scientifique" : "/podcasts-chroniques-scientifiques.html", "Chronique culturelle" : "/podcasts-chroniques-culturelles.html", "Chronique touristique" : "/podcasts-chroniques-touristiques.html", "Portrait": "/podcasts-portraits.html"}
    titre_programme = ""

    html_ajout = f"""

            <div class="div-émission-background">
                <div class="div-émission">
                    <div class="infos-émission">
                        <h2 class="titre-émission">{titre}</h2>
                        <h3 class="date-émission">{date}</h3>
                    </div>

                    <div class="infos" id="Infos{id_number}"><img class="icone-infos" src="Images/Programme.svg" alt="" height="45px"></div>

                    <br>

                    <div class="div-audio">
                        <audio controls class="audio" id="Audio{id_number}">
                            <source src="{audio}" type="audio/mpeg">
                            Votre navigateur ne supporte pas l'élément audio.
                        </audio>
                    </div>
                </div>
            </div>

        <div class="div-programme-background" id="Programme-background{id_number}">
            <div class="div-programme-ensemble">
                <div class="div-programme">
                    <h2 class="programme">Programme de l'émission :</h2>
    """
    for i in range(len(programme)) :
        titre_programme = programme[i].split(" - ")[1]
        temps_programme = programme[i].split(" - ")[0]

        if programme[i].split(" - ")[0].split(":")[0] == "0" :
            minute_programme_réel = int(programme[i].split(" - ")[0].split(":")[0][:-1])*60
        else :
            minute_programme_réel = int(programme[i].split(" - ")[0].split(":")[0])*60

        if programme[i].split(" - ")[0].split(":")[1] == "0" :
            seconde_programme_réel = int(programme[i].split(" - ")[0].split(":")[1][:-1])
        else :
            seconde_programme_réel = int(programme[i].split(" - ")[0].split(":")[1])

        temps_programme_réel = minute_programme_réel + seconde_programme_réel
        liste_temps_programme_réel.append(temps_programme_réel)
        id_programme = f"Chronique{id_number}-{i+1}"

        ajout_programme = f"""
                        <h3 class="programme" id="{id_programme}">• {temps_programme} - {titre_programme}</h3><script>document.getElementById("{id_programme}").onclick = function () →document.getElementById("Audio{id_number}").currentTime = {temps_programme_réel}; document.getElementById("Audio{id_number}").play();←</script>
        """
        ajout_programme = ajout_programme.replace("→", "{").replace("←", "}")
        html_ajout += ajout_programme

        if titre_programme == "Chronique scientifique" or titre_programme == "Chronique culturelle" or titre_programme == "Chronique touristique" or titre_programme == "Portrait" :
            chroniques[titre_programme] = temps_programme_réel


    ajout_programme = f"""
                </div>
                <div class="fermer" id="Close{id_number}"><img class="icone-fermer" src="Images/Fermer.svg" alt="" height="45px"></div>
            </div>
        </div>
    """
    html_ajout += ajout_programme

    soup_ajout = BeautifulSoup(html_ajout, "html.parser")

    div = soup.find("div", {"class": "conteneur-émissions"})
    div.insert(0, soup_ajout)

    with open(repository_path + "/émissions.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
        f.close()

    app = ctk.CTk()
    app.geometry("400x400")
    app.title("EditWebsite")
    ctk.set_appearance_mode("System")

    entrée_chronique_scientifique = ctk.CTkEntry(master=app, placeholder_text="Entrer le thème de la chronique scientifique", width=250)
    entrée_chronique_culturelle = ctk.CTkEntry(master=app, placeholder_text="Entrer le thème de la chronique culturelle", width=250)
    entrée_chronique_touristique = ctk.CTkEntry(master=app, placeholder_text="Entrer le thème de la chronique touristique", width=250)
    entrée_portraits = ctk.CTkEntry(master=app, placeholder_text="Entrer le thème du portrait", width=250)
    bouton_thèmes = ctk.CTkButton(master=app, text="Confirmer les informations", command=lambda: AjouterSujets(chroniques, noms_chroniques, noms_fichiers_chroniques, liste_temps_programme_réel, sujets, audio, titre, date, entrée_chronique_scientifique, entrée_chronique_culturelle, entrée_chronique_touristique, entrée_portraits, app), fg_color="white", text_color="black", hover_color="grey")

    print("chroniques ", chroniques)

    if "Chronique scientifique" in chroniques :
        entrée_chronique_scientifique.pack(pady=5)
        print("Chronique scientifique")

    if "Chronique culturelle" in chroniques :
        entrée_chronique_culturelle.pack(pady=5)

    if "Chronique touristique" in chroniques :
        entrée_chronique_touristique.pack(pady=5)

    if "Portraits" in chroniques :
        entrée_portraits.pack(pady=5)

    bouton_thèmes.pack(pady=10)

    app.mainloop()
            
def TitreDate() :
    global titre_émission
    global date_émission
    global entrée_titre
    global entrée_date
    global bouton_titre_date

    titre_émission = entrée_titre.get()
    date_émission = entrée_date.get()
    bouton_titre_date.configure(text="Changer le titre/date")

def RecupAudio() :
    global url_audio_émission
    global bouton_url_audio
    global label_url_audio
    bouton_url_audio.configure(text="Changer le fichier audio")
    url_audio_émission = tk.filedialog.askopenfilename(title="Sélectionner l'audio",
                                                       filetypes=(("Fichiers MP3", "*.mp3"), ("Tous les fichiers", "*.*")))
    label_url_audio.configure(text=f"Fichier audio : " + url_audio_émission.split("Émissions/")[-1])
    url_audio_émission = "Émissions" + str(url_audio_émission.split("Émissions")[-1])
    
def InfosBase() :
    try :
        app.destroy()
    except Exception:
        sys.stderr = sys.__stderr__
    ListeModifiable().mainloop()

def Programme(elements, App) :
    global titre_émission
    global date_émission
    global url_audio_émission

    App.destroy()

    AjouterEmission(titre_émission, date_émission, url_audio_émission, elements)

class ListeModifiable(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("EditWebsite")

        self.liste_elements = []

        self.champ_saisie = ctk.CTkEntry(self, placeholder_text="Ajouter un élément")
        self.champ_saisie.pack(pady=10)

        self.bouton_ajouter = ctk.CTkButton(self, text="Ajouter", command=self.ajouter_element)
        self.bouton_ajouter.pack(pady=5)

        self.bouton_confirmer = ctk.CTkButton(self, text="Confirmer", command=lambda: Programme(self.liste_elements, self), fg_color="white", text_color="black", hover_color="grey")
        self.bouton_confirmer.pack(pady=5)

        self.cadre_liste = ctk.CTkScrollableFrame(self)
        self.cadre_liste.pack(pady=5, fill="x", expand=True)

        self.afficher_liste()

    def ajouter_element(self):
        element = self.champ_saisie.get()
        if element:
            self.liste_elements.append(element)
            self.champ_saisie.delete(0, "end")
            self.afficher_liste()

    def supprimer_element(self, element):
        self.liste_elements.remove(element)
        self.afficher_liste()

    def afficher_liste(self):
        for widget in self.cadre_liste.winfo_children():
            widget.destroy()

        for element in self.liste_elements:
            cadre_element = ctk.CTkFrame(self.cadre_liste)
            cadre_element.pack(pady=5, fill="x")

            etiquette = ctk.CTkLabel(cadre_element, text=element)
            etiquette.pack(side="left")

            bouton_supprimer = ctk.CTkButton(cadre_element, text="Supprimer", command=lambda e=element: self.supprimer_element(e))
            bouton_supprimer.pack(side="right")

app = ctk.CTk()
app.geometry("400x400")
app.title("EditWebsite")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

entrée_titre = ctk.CTkEntry(master=app, placeholder_text="Entrer le titre de l'émission", width=165)
entrée_titre.pack(pady=10)

entrée_date = ctk.CTkEntry(master=app, placeholder_text="Entrer la date de l'émission", width=165)
entrée_date.pack(pady=5)

bouton_titre_date = ctk.CTkButton(master=app, text="Confirmer le titre/date", command=TitreDate)
bouton_titre_date.pack(pady=20)

label_url_audio = ctk.CTkLabel(master=app, text="Aucun fichier audio sélectionné", width=165)
label_url_audio.pack(pady=5)

bouton_url_audio = ctk.CTkButton(master=app, text="Sélectionner un fichier audio", command=RecupAudio)
bouton_url_audio.pack(pady=0)

bouton_titre_date_audio = ctk.CTkButton(master=app, text="Confirmer les informations", command=InfosBase, fg_color="white", text_color="black", hover_color="grey")
bouton_titre_date_audio.pack(pady=30)

app.mainloop()