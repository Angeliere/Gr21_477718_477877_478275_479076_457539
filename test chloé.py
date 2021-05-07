import sqlite3
connexion = sqlite3.connect("C:\\Users\\Amiel\\Downloads\\Groupe_21.db")
curseur = connexion.cursor()

def delete_user_content(User_id):
  queries = [
  "DELETE FROM Conversation WHERE creator_id = :b",
  "DELETE FROM Participants WHERE User_id = :b",
  "DELETE FROM User WHERE userid = :b",
  "DELETE FROM Settings WHERE settings_user_id = :b",
  "DELETE FROM contact_list WHERE user_id = :b",
  "DELETE FROM messages WHERE sender_id = :b"
  ]

  for query in queries:
    curseur.execute(query,[User_id])
  connexion.commit()
  print ("account id " + str(User_id) + " has been banned")

userids=curseur.execute("select Userid from User").fetchall()
userids = [i[0] for i in userids]

for userid in userids:
  e=curseur.execute("select count(blocked_user) from blocklist where blocked_user = :b",[userid]).fetchall()[0][0]
  if e>=5:
    delete_user_content(userid)


connexion.close()




