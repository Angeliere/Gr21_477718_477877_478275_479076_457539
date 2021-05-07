import sqlite3
import random
connexion = sqlite3.connect("C:\\Users\\Amiel\\Downloads\\Groupe_21.db")
curseur = connexion.cursor()

def list_user():
    return [i[0] for i in curseur.execute("SELECT userid FROM User").fetchall()]

def get_username(userid):
    if type(userid) != type(0):
        return ""
    first_and_last_name= curseur.execute("select user_firstname , user_lastname from user where userid = :UserId", [userid]).fetchone()
    return first_and_last_name[0] + " " + first_and_last_name[1]

def get_user_and_parrain(userid):
    full_user_fromdb = curseur.execute("select user1.userid , parrain.userid , user1.parrain_since from user as user1 left join user as parrain on user1.parrain_id = parrain.userid where user1.userid = :UserId", [userid]).fetchone()
    return {
        "fullname": get_username(full_user_fromdb[0]),
        "userid": full_user_fromdb[0],
        "parrain": {
            "fullname": get_username(full_user_fromdb[1]),
            "parrainsince": full_user_fromdb[2]
        }
    }

def print_user_with_parrain(userstruct):
    print("L'utilisateur " + userstruct["fullname"] + " a pour parrain " + userstruct["parrain"]["fullname"] + " depuis le " + userstruct["parrain"]["parrainsince"])

def get_potential_parrains():
    potential_parrains = []
    i = 100
    while i > 0:
        potential_parrains.append(random.choice([i[0] for i in curseur.execute("SELECT userid FROM User").fetchall()]))
        i -= random.randrange(66)
    return potential_parrains

for user in list_user():
    full_user = get_user_and_parrain(user)
    if full_user["parrain"]["fullname"] == "":
        print("l'utilisateur " + get_username(user) + " n'a pas de parrain !")
        print("Liste des parrains potentiels:")
        for parrain in get_potential_parrains():
            print(get_username(parrain))
    else:
        print_user_with_parrain(full_user)
    print()






connexion.close()
