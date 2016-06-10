from sqlite import Sqlite
import time

class Action(Sqlite):
   
  table = "actions"
  
  def __init__(self):
    Sqlite.__init__(self)
    #This table must be included in the default schema (see evolutions)
  
  def save(self, action, category = None, content= None ):
    c = self._conn.cursor()
    now = int(time.time())
    datetime = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO actions (timestamp,datetime, action,category,content) VALUES (?,?,?,?)",[now,datetime, action,category,content])
    self._conn.commit()
    c.close()
    
  def last(self, action, category = "", content = ""):
    c = self._conn.cursor()
    c.execute("""SELECT id, timestamp, action,category,content FROM actions 
                 WHERE action like '%{}%' AND
                       category like '%{}%' AND
                       content like '%{}%'
                 ORDER BY timestamp DESC LIMIT 1""".format(action,category,content))
    result = c.fetchone()
    c.close()
    return result #If the key doesn't exists it will fail