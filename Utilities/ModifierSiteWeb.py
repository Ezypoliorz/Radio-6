import pandas as pd
import tkinter as tk
import customtkinter as ctk
import os
import subprocess
import shutil
from pydub import AudioSegment
from bs4 import BeautifulSoup
import sys
import requests
import Errors

chroniques = []
spreadsheet_path = ""
spreadsheet_title = ""
spreadsheet_date = ""
audio_path = ""
noms_chroniques_podcasts = {"Chronique scientifique" : "podcasts-chroniques-scientifiques.html", "Chronique touristique" : "podcasts-chroniques-touristiques.html", "Chronique culturelle" : "podcasts-chroniques-culturelles.html", "Portrait" : "podcasts-portraits.html"}
changed_files = ["émissions.html"]
AudioSegment.converter = "ffmpeg"

app = ctk.CTk()
app.geometry("775x400")
app.title("ModifierSiteWeb")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def commit_changes():
    global changed_files
    global app
    repo_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/Radio-6/"
    repo_url = f"https://oauth2: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@github.com/ArcisseDeCaumont/Radio-6.git"
    os.chdir(repo_path)
    
    try:
        subprocess.run(['git', 'remote', 'set-url', 'origin', repo_url], check=True, capture_output=True, text=True)
        print("Repo URL set")
        
        subprocess.run(['git', 'add', '-A'], check=True, capture_output=True, text=True)
        print("All changes added to staging.")

        status_result = subprocess.run(['git', 'status', '--porcelain'], check=True, capture_output=True, text=True)
        if not status_result.stdout.strip():
            print("No changes to commit, skipping.")
            return

        commit_result = subprocess.run(['git', 'commit', '-m', "Upload automatique"], check=True, capture_output=True, text=True)
        print("Changes committed.")
        print("Commit Output:", commit_result.stdout)

        push_result = subprocess.run(['git', 'push'], check=True, capture_output=True, text=True, timeout=700)
        print("All changes pushed successfully.")
        print("Push Output:", push_result.stdout)

    except subprocess.CalledProcessError as e:
        print(e)
        print(e.stderr)
        Errors.raise_error(app, "Erreur lors de la synchronisation GitHub.", "ModifierSiteWeb.py", mail=True, specific_error=e)
        return


class Chronique:
    def __init__(self, type_chronique, nom_chronique, index, timestamp):
        self.type = type_chronique
        self.nom = nom_chronique
        self.index = index
        self.timestamp = timestamp
        self.timestamp_réel = timestamp
        self.podcast = False



def read_spreadsheet(path):
    print("Read Spreadsheet")
    global chroniques
    global noms_chroniques_podcasts

    file = pd.read_excel(path, sheet_name=0, converters={'Début (MM:SS)' : str}, header=None)
    print("File converted to pandas object")
    if file.iloc[0,0] != "Nom/type de la chronique" or file.iloc[0,1] != "Début (MM:SS)" or file.iloc[0,2] != "Nom pour le podcast" :
        Errors.raise_error(app, "Mise en page du fichier Excel incorrecte !", "ModifierSiteWeb.py")
    height, width = file.shape
    
    for i in range(1, height) :
        nouvelle_chronique = Chronique(type_chronique=file.iloc[i,0], nom_chronique=None, index=i, timestamp=file.iloc[i, 1])
        chroniques.append(nouvelle_chronique)
        if nouvelle_chronique.type in noms_chroniques_podcasts :
            nouvelle_chronique.podcast = True
            nouvelle_chronique.nom = file.iloc[i, 2]
            print(nouvelle_chronique.nom)
        timestamp_minutes = nouvelle_chronique.timestamp.split(":")[0]
        timestamp_secondes = nouvelle_chronique.timestamp.split(":")[1]
        if str(timestamp_minutes[0]) == "0":
            timestamp_minutes = timestamp_minutes[1:]
        if str(timestamp_secondes[0]) == "0":
            timestamp_secondes = timestamp_secondes[1:]
        nouvelle_chronique.timestamp_réel = int(timestamp_minutes)*60 + int(timestamp_secondes)
    print("End of Read Shpreadsheet")

def modify_html():
    global spreadsheet_title
    global spreadsheet_date
    global audio_path
    global chroniques
    global changed_files

    with open(f"C:/Users/{os.getlogin()}/Documents/GitHub/Radio-6/émissions.html", "r", encoding="utf-8") as f :
        soup = BeautifulSoup(f, "html.parser")

    id_number = int(soup.find("div", {"class": "infos"})["id"].split("Infos")[-1]) + 1

    html_ajout = f"""

            <div class="div-émission-background">
                <div class="div-émission">
                    <div class="infos-émission">
                        <h2 class="titre-émission">{spreadsheet_title}</h2>
                        <h3 class="date-émission">{spreadsheet_date}</h3>
                    </div>

                    <div class="infos" id="Infos{id_number}"><img class="icone-infos" src="Images/Programme.svg" alt="" height="45px"></div>

                    <br>

                    <div class="div-audio">
                        <audio controls class="audio" id="Audio{id_number}">
                            <source src="Émissions/{audio_path.split("/")[-1]}" type="audio/mpeg">
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

    for chronique in chroniques :
        id_chronique =  f"Chronique{id_number}-{chronique.index+1}"
        html_ajout += f"""
                        <h3 class="programme" id="{id_chronique}">• {chronique.timestamp} - {chronique.type}</h3><script>document.getElementById("{id_chronique}").onclick = function ()""" + "{" + f"""document.getElementById("Audio{id_number}").currentTime = {chronique.timestamp_réel}; document.getElementById("Audio{id_number}").play();""" + "}" + """</script>
        """
    html_ajout += f"""
                </div>
                <div class="fermer" id="Close{id_number}"><img class="icone-fermer" src="Images/Fermer.svg" alt="" height="45px"></div>
            </div>
        </div>
    """
    soup_ajout = BeautifulSoup(html_ajout, "html.parser")
    div = soup.find("div", {"class": "conteneur-émissions"})
    if div :
        div.insert(0, soup_ajout)
    else :
        print("div = None !")
        sys.exit()
    with open(f"C:/Users/{os.getlogin()}/Documents/GitHub/Radio-6/émissions.html", "w", encoding="utf-8") as f :
        f.write(str(soup))
        f.close()

    for chronique in chroniques :
        if chronique.podcast == True :

            with open(f"C:/Users/{os.getlogin()}/Documents/GitHub/Radio-6/{noms_chroniques_podcasts[chronique.type]}", "r", encoding="utf-8") as f :
                print(noms_chroniques_podcasts[chronique.type])
                soup = BeautifulSoup(f, "html.parser")
                changed_files.append(noms_chroniques_podcasts[chronique.type])
            html_ajout_chroniques = f"""
            <div class="div-émission-background">
                <div class="div-émission">
                    <div class="infos-émission">
                        <h2 class="titre-émission">{chronique.nom}</h2>
                        <h3 class="date-émission">{spreadsheet_title} - {spreadsheet_date}</h3>
                    </div>

                    <div class="div-audio-podcasts">
                        <audio controls class="audio" id="Audio{id_number}">
                            <source src="Émissions/{chronique.type} - {chronique.nom.replace('?', '').replace('<', '').replace('>', '').replace(':', '').replace('/', '').replace('|', '').replace('*', '')}.mp3" type="audio/mpeg">
                            Votre navigateur ne supporte pas l'élément audio.
                        </audio>
                    </div>
                </div>
            </div>
        """
            soup_ajout_chroniques = BeautifulSoup(html_ajout_chroniques, "html.parser")
            div = soup.find("div", {"class": "conteneur-podcasts"})
            print(type(div))
            div.insert(0, soup_ajout_chroniques)
            with open(f"C:/Users/{os.getlogin()}/Documents/GitHub/Radio-6/{noms_chroniques_podcasts[chronique.type]}", "w", encoding="utf-8") as f :
                f.write(str(soup))
                f.close()

    commit_changes()

def process_info():
    print("Process Info")
    global spreadsheet_title
    global spreadsheet_date
    global audio_path
    global chroniques
    global changed_files

    for chronique in chroniques :
        if chronique.podcast == True :
            audio_chronique = AudioSegment.from_file(audio_path)
            print(int(chronique.timestamp_réel*1000))
            print(int(chroniques[chronique.index+1].timestamp_réel*1000))
            audio_chronique = audio_chronique[int(chronique.timestamp_réel*1000):int(chroniques[chronique.index+1].timestamp_réel*1000)]
            audio_chronique = audio_chronique.fade_in(1500)
            audio_chronique = audio_chronique.fade_out(1500)
            audio_chronique.export(f"{chronique.type} - {chronique.nom.replace('?', '').replace('<', '').replace('>', '').replace(':', '').replace('/', '').replace('|', '').replace('*', '')}.mp3", format="MP3")
            try :
                shutil.move(f"{chronique.type} - {chronique.nom.replace('?', '').replace('<', '').replace('>', '').replace(':', '').replace('/', '').replace('|', '').replace('*', '')}.mp3", f"C:/Users/{os.getlogin()}/Documents/GitHub/Radio-6/Émissions")
            except shutil.SameFileError :
                pass
            except shutil.Error :
                pass
            changed_files.append(f"Émissions/{chronique.type} - {chronique.nom.replace('?', '').replace('<', '').replace('>', '').replace(':', '').replace('/', '').replace('|', '').replace('*', '')}.mp3")

    modify_html()

def select_spreadsheet(app):
    print("Select Spreadsheet")
    global spreadsheet_path
    global spreadsheet_title
    global spreadsheet_date
    spreadsheet_path = tk.filedialog.askopenfilename(title="Sélectionner le fichier infos",
                                                     filetypes=(("Fichiers Excel", ".xlsx"), ("Tous les fichiers", ".*")))
    if spreadsheet_path.split(".")[-1] != "xlsx" :
        Errors.raise_error(app, "Format de fichier invalide ! Fichier Excel (.xlsx) nécessaire", "ModifierSiteWeb.py")
        return
    else :
        spreadsheet_title = spreadsheet_path.split("/")[-1].split(" - ")[0]
        spreadsheet_date = spreadsheet_path.split("/")[-1].split(" - ")[1].replace("_","/")[:-5]
        label_spreadsheet_path = ctk.CTkLabel(master=app, text=f"Fichier sélectionné : {spreadsheet_path}", width=165)
        label_spreadsheet_title = ctk.CTkLabel(master=app, text=f"Nom enregistré : {spreadsheet_title}", width=165)
        label_spreadsheet_date = ctk.CTkLabel(master=app, text=f"Date enregistrée : {spreadsheet_date}", width=165)
        label_spreadsheet_path.pack(pady=5)
        label_spreadsheet_title.pack(pady=0)
        label_spreadsheet_date.pack(pady=0)

    print("Calling Read Spreadsheet")
    read_spreadsheet(spreadsheet_path)

def select_audio():
    global audio_path
    audio_path = tk.filedialog.askopenfilename(title="Sélectionner le fichier audio",
                                                     filetypes=(("Fichiers MP3", ".mp3"), ("Tous les fichiers", ".*")))
    label_audio_path = ctk.CTkLabel(master=app, text=f"Fichier audio sélectionné : {audio_path}", width=165)
    label_audio_path.pack(pady=5)
    try :
        shutil.copy(audio_path, f"C:/Users/{os.getlogin()}/Documents/GitHub/Radio-6/Émissions")
    except shutil.SameFileError :
        pass
    except shutil.Error :
        pass

bouton_tableur = ctk.CTkButton(master=app, text="Sélectionner le fichier infos", command=lambda : select_spreadsheet(app))
bouton_tableur.pack(pady=5)

bouton_audio = ctk.CTkButton(master=app, text="Sélectionner le fichier audio", command=select_audio)
bouton_audio.pack(pady=10)

bouton_validation = ctk.CTkButton(master=app, text="Valider les informations", command=process_info, fg_color="white", text_color="black", hover_color="grey")
bouton_validation.pack(pady=10)

app.mainloop()
