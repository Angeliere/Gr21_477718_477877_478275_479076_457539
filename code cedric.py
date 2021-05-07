#connecter les message ID, les prendre dans la loupe. Ensuite crée une variable = au nombre de message ID
#AVec ca, a la fin du loop, on a notre variable et on doit dire a l'activateur que si cette variable est différente
#que la variable qui est la valeur de base , alors l'update se fait !



import time
import sqlite3
connexion = sqlite3.connect("C:\\Users\\cedri\\Downloads\\database projet.db", timeout = 15)
curseur = connexion.cursor()
seconds = time.time()



if seconds > 10:
curseur.execute("""SELECT * FROM Messages""")
nb_message_utilisateur = curseur.fetchall()
len(nb_message_utilisateur)
connexion.commit()



x = len(nb_message_utilisateur)
y = x



if y < x:
a = curseur.execute("""SELECT sender_id FROM Messages WHERE message_id = len(nb_message_utilisateur)""")
#il faut prendre le senderId du message id qu'on vient de prendre
curseur.execute("""UPDATE User SET User_MessageQuantity = User_MessageQuantity + 1 WHERE User_id = sender_id""")



seconds = 0



#on pourrait comparer les chiffres des messages avant de lancer le script des if seconds > 10 pour le comparer
# avec celui qu'on obtient quand la requête est lancée