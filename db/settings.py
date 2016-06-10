from sqlite import Sqlite

class Settings(Sqlite):
  
  table="settings"
  def __init__(self):
    Sqlite.__init__(self)
    #This table must be included in the default schema (see evolutions)
  
  def put(self,key, value):
    c = self._conn.cursor()
    c.execute("REPLACE INTO settings (key,value) VALUES (?,?)",[key,value])
    self._conn.commit()
    c.close()
    
  def get(self,key):
    c = self._conn.cursor()
    c.execute('SELECT key,value FROM settings WHERE key=? LIMIT 1',[key])
    result = c.fetchone()
    c.close()
    return result[1] #If the key doesn't exists it will fail