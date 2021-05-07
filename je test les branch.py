import sqlite3
connexion = sqlite3.connect("C:\\Users\\Amiel\\Downloads\\Groupe_21.db")
curseur = connexion.cursor()

def voir_table(userid):
        return curseur.execute("SELECT user_messagequantity FROM user where userid = :userid",[userid]).fetchall()[0][0]


userids=curseur.execute("select Userid from User").fetchall()
userids = [i[0] for i in userids]

for userid in userids:
        messages = voir_table(userid)

        if 299 > messages >= 100:
                print("Coupon -5% chez Farm pour un produit Bio")

        elif 499 > messages >= 300:
                print("Journée de la plantation double!")

        elif 999 > messages >= 500:
                print("Coupon -15% chez Exki")
        
        elif messages >= 1000:
                print("Journée de la plantation triple!")

        print("le userid " + str(userid) + " possède " + str(messages))
