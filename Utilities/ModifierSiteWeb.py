import pandas as pd
import tkinter as tk
import customtkinter as ctk


chroniques = {}

def file_format_error():
    pass

def read_spreadsheet(path):
    global chroniques
    file = pd.read_excel(path, sheet_name=0)
    if file.iloc[0,0] != "Nom/type de la chronique" or file.iloc[0,1] != "Début (MM:SS)" or file.iloc[0,0] != "Nom pour le podcast" :
        file_format_error()
    
    cell = file.iloc[1,0]
    row_index = 1
    while not pd.isna(cell) :
        chroniques[cell] = file.iloc[row_index, 1]
        row_index += 1
        cell = file.iloc[row_index, 0]
    
    return chroniques

print(read_spreadsheet("C:/Users/oscar/Documents/GitHub/Radio-6/Nom de l'émission - 01_01_2025.xlsx"))