from modules import db

def selectAll():
  sql = "SELECT * FROM type"
  cursor = db.cursor
  types = cursor.fetchall()
  db.CONNECTION.commit()

  return types
