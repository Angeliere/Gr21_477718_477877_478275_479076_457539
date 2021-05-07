import sqlite3
connexion = sqlite3.connect('/Users/briceverola/desktop/database1.db')
curseur = connexion.cursor()



def find_user(x):
query = "SELECT userid FROM User WHERE user_age < :x"
resultats = curseur.execute(query,{"user":userid})
userid = resultats.fetchall()

def find_adverts(category_over_15):
query = "SELECT name FROM adverts WHERE category_over_15 = 0"
resultats = curseur.execute(query, {"adverts": name})
name = resultats.fetchall()

if category_over_15 = 0:
print(curseur.execute('select name from adverts').fetchone())