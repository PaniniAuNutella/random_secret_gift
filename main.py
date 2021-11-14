import smtplib
import ssl
import random

# CONFIG
smtp_address = "smtp.gmail.com"
smtp_port = 465
context = ssl.create_default_context()

email_sender = "..."  # Mail de l'expéditeur
email_password = "..."  # MDP de l'expéditeur

list_email_receiver = ["mail_1@mail.com", "mail_2@mail.com", "mail_3@mail.com" ...]  # Liste des mails
L2 = ["mail_1@mail.com", "mail_2@mail.com", "mail_3@mail.com" ...] # Copie de la liste des mails
L3 = ["Prénom_1", "Prénom_2", "Prénom_3" ...] # Liste des prénoms dans le même ordre que L2
L4 = [] # Liste vide de vérification

print("Il y a", len(list_email_receiver), "personnes dans la liste 1 et", len(L2), "personnes dans la liste 2")
if list_email_receiver != L2:
    print("Listes différentes")
elif len(list_email_receiver) == 0:
    print("Listes vide !")
else:
    n = 0
    for i in range(0, len(list_email_receiver)):
        X = list_email_receiver[i]
        email_receiver = random.choice(L2)
        while X == email_receiver:
            email_receiver = random.choice(L2)
        name = L3[L2.index(email_receiver)]
        #print(name)
        L2.remove(email_receiver)
        L3.remove(name)
        print("? obtient", email_receiver) # Vérification si le mail est bien parvenu à toute la liste
        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server: # Connexion au Host Gmail
            server.login(email_sender, email_password) # Connexion au mail de l'expéditeur
            server.sendmail(email_sender, X, "Bravo, tu dois maintenant trouver un cadeau pour "+name + "\n Bonne chance :)") # Contenu du mail
            print("E-mail envoyé !\n")
        n += 1
    print("\n",list_email_receiver,"\n", L2,"\n", L3)
    print(n)
    print("FINI")

    for j in range(0, len(list_email_receiver)):
        if L3 != L4:
            print("Problème, il faut recommencer.")
            break
