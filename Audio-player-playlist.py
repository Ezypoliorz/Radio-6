# »»» Programme permettant de lire une playlist audio à partir d'un fichier CSV
# »»» © Oscar Mazeure - 2025

# Importation des modules
from playsound import playsound # Playsound : lecture du fichier audio
from time import sleep # Time : utilisé pour les fonctions de délai
import csv # CSV : lecture du fichier CSV
import sys # Sys : utilisé pour quitter le programme
import os # OS : utilisé pour les chemins de fichiers

# Définition des variables
script_dir = os.path.dirname(os.path.abspath(__file__)) # Get the directory of the scriptz
csv_file = os.path.join(script_dir, "Playlist/playlist.csv") # Construct the full path to the CSV file
audio_files = [] # Liste des fichiers audio
mode = "" # Mode de lecture : flow (sans interruption) ou pause (avec interruption)

# Fonction de lecture du fichier CSV
def Read_CSV(file) :
    with open(csv_file, mode='r', newline='') as csvfile :
        reader = csv.reader(csvfile, delimiter=';') # Ouverture du fichier CSV en mode lecture
        for row in reader :
            audio = str(row) # Lecture de chaque ligne du fichier CSV
            audio = audio[2:-2] # Suppression des caractères inutiles
            audio_files.append(audio) # Ajout du fichier audio à la liste

print("💡 Avez-vous pensé à renseigner les fichiers audio dans le fichier CSV ?")
mode = input("Mode de lecture (flow/pause) → ")

if mode not in ["flow", "pause"]:
    print("❌ Mode de lecture invalide.")
    sleep(5) # Délai de 5 secondes
    sys.exit() # Fermeture du programme

Read_CSV(csv_file)

print("🎵 Liste des fichiers audio :")
for i in range(len(audio_files)) :
    print(f"{i+1} - {audio_files[i]}") # Affichage de la liste des fichiers audio

if mode == "flow" :
    for i in range(len(audio_files)) :
        audio_url = os.path.normpath(os.path.join(script_dir, "Playlist", audio_files[i] + ".mp3")).replace("\\", "/") # Chemin du fichier audio
        playsound(audio_url) # Lecture du fichier audio

elif mode == "pause" :
    for i in range(len(audio_files)) :
        input("Appuyez sur Entrée pour continuer...") # Attente de l'appui sur la touche Entrée
        audio_url = os.path.normpath(os.path.join(script_dir, "Playlist", audio_files[i] + ".mp3")).replace("\\", "/") # Chemin du fichier audio
        playsound(audio_url) # Lecture du fichier audio

print("🎉Fin de la playlist !")