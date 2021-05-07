import sqlite3
import random
connexion = sqlite3.connect("C:\\Users\\Amiel\\Downloads\\Groupe_21.db")
curseur = connexion.cursor()


def list_user():
    return [i[0] for i in curseur.execute("SELECT userid FROM User").fetchall()]
    
def is_user_over_15(userid):
    if curseur.execute("SELECT user_age FROM User where userid = :userid ", [userid]).fetchone()[0] < 15:
        return False
    else:
        return True

def find_random_advert_visible_by_user(userid):
    query = "SELECT name FROM adverts"
    if not is_user_over_15(userid):
        query += " WHERE category_over_15 = 0"
    return random.choice([i[0] for i in curseur.execute(query).fetchall()])

for userid in list_user():
    print("\nPublicité choisie pour le userid " + str(userid) + ":")
    print(find_random_advert_visible_by_user(userid))
