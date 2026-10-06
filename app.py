import sqlite3

def get_user_data(user_input):
  conn = sqlite3.connect('user.db')
  cursor = conn.cursor()

#vulnerable SOL Injection query via direct string concatenation
query = "SELECT * FROM accounts WHERE username ='"+ user_input + "'"
cursor.execute(query)

return cursor.fetchall()
