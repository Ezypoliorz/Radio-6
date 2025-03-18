import customtkinter
# si la classe est dans un autre fichier
# from liste_modifiable import ListeModifiable

class ListeModifiable(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")
        self.title("Liste modifiable")

        self.liste_elements = []

        self.champ_saisie = customtkinter.CTkEntry(self, placeholder_text="Ajouter un élément")
        self.champ_saisie.pack(pady=10)

        self.bouton_ajouter = customtkinter.CTkButton(self, text="Ajouter", command=self.ajouter_element)
        self.bouton_ajouter.pack(pady=5)

        self.cadre_liste = customtkinter.CTkScrollableFrame(self)
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
            cadre_element = customtkinter.CTkFrame(self.cadre_liste)
            cadre_element.pack(pady=5, fill="x")

            etiquette = customtkinter.CTkLabel(cadre_element, text=element)
            etiquette.pack(side="left")

            bouton_supprimer = customtkinter.CTkButton(cadre_element, text="Supprimer", command=lambda e=element: self.supprimer_element(e))
            bouton_supprimer.pack(side="right")

class AppPrincipale(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Application principale")

        # Autres widgets de votre application existante
        label_titre = customtkinter.CTkLabel(self, text="Application avec liste modifiable")
        label_titre.pack(pady=20)

        # Instanciation de la classe ListeModifiable
        self.liste_modifiable = ListeModifiable()
        self.liste_modifiable.pack(pady=20, padx=20, fill="both", expand=True)

if __name__ == "__main__":
    app = AppPrincipale()
    app.mainloop()