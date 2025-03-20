import tkinter as tk
import customtkinter as ctk
from bs4 import BeautifulSoup
import sys

titre_émission = "Test 1"
date_émission = "Teeest 1"
url_audio_émission = "Émissions/Musique test 3.mp3"
id_number = 0
thread = "main"
test = "0"

def AjouterEmission(titre, date, audio) :
    with open("émissions.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    id_number = soup.find("div", {"class": "infos"})["id"].split("Infos")[-1]

    html_ajout = f"""

            <div class="div-émission-background">
                <div class="div-émission">
                    <div class="infos-émission">
                        <h2 class="titre-émission">{titre}</h2>
                        <h3 class="date-émission">{date}</h3>
                    </div>

                    <div class="infos" id="Infos{id_number}"><img src="Images/Programme.svg" alt="" height="45px"></div>

                    <br>

                    <div class="div-audio">
                        <audio controls class="audio" id="Audio{id_number}">
                            <source src="{audio}" type="audio/mpeg">
                            Votre navigateur ne supporte pas l'élément audio.
                        </audio>
                    </div>
                </div>
            </div>

    """

    soup_ajout = BeautifulSoup(html_ajout, "html.parser")

    div = soup.find("div", {"class": "conteneur-émissions"})
    div.insert(0, soup_ajout)

    with open("émissions.html", "w", encoding="utf-8") as f:
        f.write(str(soup))

def TitreDate() :
    global titre_émission
    global date_émission
    global entrée_titre
    global entrée_date
    global bouton_titre_date

    titre_émission = entrée_titre.get()
    date_émission = entrée_date.get()
    bouton_titre_date.configure(text="Changer le titre/date")

    print(titre_émission)
    print(date_émission)

def RecupAudio() :
    global url_audio_émission
    global bouton_url_audio
    bouton_url_audio.configure(text="Changer le fichier audio")
    url_audio_émission = tk.filedialog.askopenfilename(title="Sélectionner l'audio", filetypes=(("Fichiers MP", "*.mp3"), ("Tous les fichiers", "*.*")))
    print(url_audio_émission)
    
def InfosBase() :
    try :
        app.destroy()
    except Exception:
        sys.stderr = sys.__stderr__
    ListeModifiable().mainloop()

class ListeModifiable(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")
        self.title("Liste modifiable")

        self.liste_elements = []

        self.champ_saisie = ctk.CTkEntry(self, placeholder_text="Ajouter un élément")
        self.champ_saisie.pack(pady=10)

        self.bouton_ajouter = ctk.CTkButton(self, text="Ajouter", command=self.ajouter_element)
        self.bouton_ajouter.pack(pady=5)

        self.cadre_liste = ctk.CTkScrollableFrame(self)
        self.cadre_liste.pack(pady=10, fill="both", expand=True)

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
        # Effacer le cadre
        for widget in self.cadre_liste.winfo_children():
            widget.destroy()

        # Afficher les éléments
        for element in self.liste_elements:
            cadre_element = ctk.CTkFrame(self.cadre_liste)
            cadre_element.pack(pady=5, fill="x")

            etiquette = ctk.CTkLabel(cadre_element, text=element)
            etiquette.pack(side="left")

            bouton_supprimer = ctk.CTkButton(cadre_element, text="Supprimer", command=lambda e=element: self.supprimer_element(e))
            bouton_supprimer.pack(side="right")

app = ctk.CTk()
app.geometry("800x400")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

entrée_titre = ctk.CTkEntry(master=app, placeholder_text="Entrer le titre de l'émission")
entrée_titre.pack(pady=10)

entrée_date = ctk.CTkEntry(master=app, placeholder_text="Entrer la date de l'émission")
entrée_date.pack(pady=15)

bouton_titre_date = ctk.CTkButton(master=app, text="Confirmer le titre/date", command=TitreDate)
bouton_titre_date.pack(pady=20)

bouton_url_audio = ctk.CTkButton(master=app, text="Sélectionner un fichier audio", command=RecupAudio)
bouton_url_audio.pack(pady=25)

bouton_titre_date_audio = ctk.CTkButton(master=app, text="Confirmer les informations;", command=InfosBase)
bouton_titre_date_audio.pack(pady=30)

app.mainloop()