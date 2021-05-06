import sqlite3
connexion = sqlite3.connect("D:\\cours INFO\\Groupe21.db")
curseur = connexion.cursor()





n=find_user(User_firstname)
def n
  query = "SELECT id FROM Users WHERE User_id = :User"
  resultats = curseur.execute(query, {"User": User_firstname})
  User_id = resultats.fetchone()[0]
  return user_id

i=delete_user_content(User_id)

def i
  queries = [
  "DELETE FROM Conversation WHERE User_id = ?",
  "DELETE FROM Participants WHERE User_id = ?",
  "DELETE FROM Users WHERE id = ?"
  ]


f=deleted_account(User_firstname)
def f
  User_id = find_user(User_firstname)
  delete_user_content(User_firstname)
  print("Your account has been deleted")



Deleted_account("DonaldTrump")



see_table("User")