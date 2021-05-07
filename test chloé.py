import sqlite3
connexion = sqlite3.connect("C:\\Users\\schwe\\Desktop\\Groupe 21.db")
curseur = connexion.cursor()
import time

b=0
a=curseur.execute("""select Userid from User""")


connexion.commit()
c=len(a.fetchall())
print(c)

d=curseur.execute("""select blocked_user from blocklist""")
print(d.fetchall)

for i in range(c):
 b += 1
 e=curseur.execute("""select count(blocked_user) from blocklist where blocked_user = :b""",[b])
 if e=5:
  def find_user(user_firstname):
   query = "SELECT id FROM Users WHERE User_id = :User"
   resultats = curseur.execute(query, {"User": User_firstname})
   User_id = resultats.fetchone()[0]
   return user_id

  def delete_user_content(User_id):
   queries = [
   "DELETE FROM Conversation WHERE creator_id = :b",
   "DELETE FROM Participants WHERE Userid = :b",
   "DELETE FROM Users WHERE userid = :b"
   "DELETE FROM Settings WHERE settings_userid = :b"
   "DELETE FROM contact_list WHERE user_id = :b"
   "DELETE FROM messages WHERE sender_id = :b"
   ]
   print ("your account has been banned")

  see_table("User")

 
connexion.commit()
connexion.close()