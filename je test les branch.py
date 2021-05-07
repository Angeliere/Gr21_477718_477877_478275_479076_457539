import sqlite3
connexion = sqlite3.connect('/Users/maximedevroede/Downloads/database1.db')
curseur = connexion.cursor()

def voir_table(table):
    query = "SELECT values(user_messagequantity) FROM user where userid =1"
    resultat = curseur.execute(query)
    print("Voici le nombre de messages total actuel", table)
    for row in resultat:
        print(row)
        
messages = query

if 29999 > messages > 10000:
        print("Coupon -5% chez Farm pour un produit Bio")
    
elif 49999 > messages > 30000:
        print("Journée de la plantation double!")
    
elif 99999 >  messages > 50000:
        print("Coupon -15% chez Exki")
    
elif messages > 100000:
        print("Journée de la plantation triple!")
messages = 0
print(messages)

voir_table('user')