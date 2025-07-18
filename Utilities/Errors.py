import requests
import tkinter as tk
import customtkinter as ctk
import time

def raise_error(app, error, tool, mail = False, specific_error = None) :
    app.destroy()
    app = ctk.CTk()
    app.geometry("600x400")
    app.title("ModifierSiteWeb")
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    label_arror = ctk.CTkLabel(master=app, text=error, width=165, text_color="red")
    label_arror.pack(pady=5)
    label_advice1 = ctk.CTkLabel(master=app, text="Lisez la documentation et réessayez", width=165, text_color="red")
    label_advice1.pack(pady=0)
    label_advice2 = ctk.CTkLabel(master=app, text="Pour toute  aide supplémentaire, contactez oscar.mazeure@orange.fr", width=165, text_color="red")
    label_advice2.pack(pady=0)

    if mail != False and specific_error != None :
        send_email_error(error, specific_error, tool)
    
    return app

def send_email_error(general_error, specific_error, tool) :
    API_KEY = 'a70e4f2a288cedbb6ee2a7400b35b2bc-0ce15100-4db55af5'
    DOMAIN = 'sandboxb632eaab2fa5464db7cd429072be3408.mailgun.org'
    API_BASE_URL = 'https://api.mailgun.net/v3'
    FROM_EMAIL = f'Rapport d\'erreur <mailgun@{DOMAIN}>'
    TO_EMAIL = 'oscar.mazeure@orange.fr'
    SUBJECT = f'{time.strftime("%d/%m/%Y", time.localtime())} - {general_error}'
    HTML_CONTENT = f'''<h2>Date : {time.strftime("%d/%m/%Y", time.localtime())}</h2><br>
                       <h2>Outil utilisé : {tool}</h2><br>
                       <h2>Erreur générale : {general_error}</h2><br>
                       <h2>Détails de l'erreur : {specific_error}</h2><br>
    specific_error'''
    TEXT_CONTENT = f'Date : {time.strftime("%d/%m/%Y", time.localtime())}\nOutil utilisé : {tool}\nErreur générale : {general_error}\nDétails de l\'erreur : {specific_error}'

    try :
        response = requests.post(
            f"{API_BASE_URL}/{DOMAIN}/messages",
            auth=("api", API_KEY),
            data={
                "from" : FROM_EMAIL,
                "to" : TO_EMAIL,
                "subject" : SUBJECT,
                "html" : HTML_CONTENT,
                "text" : TEXT_CONTENT
            }
        )

        if response.status_code == 200:
            print(f"Email envoyé avec succès !")
            print(f"Réponse de Mailgun: {response.json()}")
        else:
            print(f"Erreur lors de l'envoi de l'email. Code de statut: {response.status_code}")
            print(f"Réponse de Mailgun: {response.json()}")

    except Exception as e:
        print(e)

"""app = ctk.CTk()
app.geometry("775x400")
app.title("ModifierSiteWeb")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

bouton_erreur = ctk.CTkButton(master=app, text="Test de la fonction erreur", command=lambda : raise_error(app, "Erreur générale test !", "Outil test", mail=True, specific_error="Erreur détaillée\nDétails supplémentaires"))
bouton_erreur.pack(pady=5)

app.mainloop()"""