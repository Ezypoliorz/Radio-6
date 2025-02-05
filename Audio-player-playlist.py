# »»» Programme permettant de lire une playlist audio à partir d'un fichier CSV
# »»» © Oscar Mazeure - 2025

# Importation des modules
from playsound import playsound # Playsound : lecture du fichier audio
import pyaudio # Pyaudio : utilisé pour la sélection du périphérique audio
from time import sleep # Time : utilisé pour les fonctions de délai
import csv # CSV : lecture du fichier CSV
import sys # Sys : utilisé pour quitter le programme

# Définition des variables
csv_file = "C:/Users/ordi2429044/Documents/Programmation/Python/Projets/Audio player/Playlist/playlist.csv" # Nom du fichier CSV
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
        audio_url = "C:/Users/ordi2429044/Documents/Programmation/Python/Projets/Audio player/Playlist/" + audio_files[i] + ".mp3" # Chemin du fichier audio
        playsound(audio_url) # Lecture du fichier audio

elif mode == "pause" :
    for i in range(len(audio_files)) :
        input("Appuyez sur Entrée pour continuer...") # Attente de l'appui sur la touche Entrée
        audio_url = "C:/Users/ordi2429044/Documents/Programmation/Python/Projets/Audio player/Playlist/" + audio_files[i] + ".mp3" # Chemin du fichier audio
        playsound(audio_url) # Lecture du fichier audio

print("🎉Fin de la playlist !")