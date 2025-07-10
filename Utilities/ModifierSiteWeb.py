import pandas as pd
import tkinter as tk
import customtkinter as ctk


chroniques = {}
spreadsheet_path = ""
spreadsheet_title = ""
spreadsheet_date = ""
audio_path = ""

def file_format_error():
    pass

def select_spreadsheet():
    global spreadsheet_path
    global spreadsheet_title
    global spreadsheet_date
    spreadsheet_path = tk.filedialog.askopenfilename(title="Sélectionner le fichier infos",
                                                     filetypes=(("Fichiers Excel", ".xlsx"), ("Tous les fichiers", ".*")))
    spreadsheet_title = spreadsheet_path.split("/")[-1].split(" - ")[0]
    spreadsheet_date = spreadsheet_path.split("/")[-1].split(" - ")[1]
    label_spreadsheet_path = ctk.CTkLabel(master=app, text=f"Fichier sélectionné : {spreadsheet_path}", width=165)
    label_spreadsheet_title = ctk.CTkLabel(master=app, text=f"Nom enregistré : {spreadsheet_title}", width=165)
    label_spreadsheet_date = ctk.CTkLabel(master=app, text=f"Date enregistrée : {spreadsheet_date}", width=165)
    label_spreadsheet_path.pack(pady=5)
    label_spreadsheet_title.pack(pady=0)
    label_spreadsheet_date.pack(pady=0)

def select_audio():
    global audio_path
    audio_path = tk.filedialog.askopenfilename(title="Sélectionner le fichier audio",
                                                     filetypes=(("Fichiers MP3", ".mp3"), ("Tous les fichiers", ".*")))
    label_audio_path = ctk.CTkLabel(master=app, text=f"Fichier audio sélectionné : {audio_path}", width=165)
    label_audio_path.pack(pady=5)

def read_spreadsheet(path):
    global chroniques
    file = pd.read_excel(path, sheet_name=0, converters={'Début (MM:SS)' : str})
    if file.iloc[0,0] != "Nom/type de la chronique" or file.iloc[0,1] != "Début (MM:SS)" or file.iloc[0,0] != "Nom pour le podcast" :
        file_format_error()
    height, width = file.shape
    
    for i in range(height) :
        chroniques[file.iloc[i,0]] = file.iloc[i, 1][:-3]
    
    return chroniques

app = ctk.CTk()
app.geometry("400x400")
app.title("ModifierSiteWeb")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

bouton_tableur = ctk.CTkButton(master=app, text="Sélectionner le fichier infos", command=select_spreadsheet)
bouton_tableur.pack(pady=5)

bouton_tableur = ctk.CTkButton(master=app, text="Sélectionner le fichier audio", command=select_audio)
bouton_tableur.pack(pady=10)

app.mainloop()