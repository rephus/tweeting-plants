#https://docs.python.org/2/library/sqlite3.html
import sqlite3

#TODO: This class must be a singleton (1 connection)
class Sqlite:
  
  _db = "/var/sqlite/tweeting-plants.db"
  def __init__(self):
    self._conn = sqlite3.connect(self._db, check_same_thread=False)
    self._evolutions()
    
  def version(self):
    c = self._conn.cursor()
    c.execute("SELECT key,value FROM settings WHERE key = 'version'")
    result = c.fetchone()
    c.close()
    return result[1]
  
  def _evolutions(self):
    try:
      version = self.version()
      #print "Rows in settings ", self._count("settings")
      if version < 0: # Replace 0 with next version
        pass #_schema_v1() should appear here
      else: 
        #Last case (db is updated)
        print "Database is updated, version: {}".format(version)
      
    except Exception as error:
      print "Database exception: ",error
      self._schema_v0()
      print "Database successfully created"
      
  def _schema_v0(self):
    c = self._conn.cursor()
    c.execute("CREATE TABLE settings (key TEXT PRIMARY KEY,value TEXT)")
    c.execute("INSERT INTO settings (key,value) VALUES (?,?)",["version","0"])
    c.execute("CREATE TABLE sensors (id INTEGER PRIMARY KEY,timestamp INTEGER,datetime TEXT, temperature INTEGER, humidity INTEGER, light INTEGER)")
    c.execute("CREATE TABLE actions (id INTEGER PRIMARY KEY,timestamp INTEGER,datetime TEXT, action TEXT, category TEXT, content TEXT)")
    self._conn.commit()
    c.close()
  
  def all(self):
    c = self._conn.cursor()
    c.execute('SELECT * FROM {}'.format(self.table))
    result = c.fetchall()
    c.close()
    return result
  
  def count(self):
    c = self._conn.cursor()
    c.execute('SELECT COUNT(*) FROM {}'.format(self.table))
    result = c.fetchone()
    c.close()
    return result[0]
  
  def destroy(self):
    self._conn.close()