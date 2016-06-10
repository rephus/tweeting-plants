from sqlite import Sqlite
import time

class Sensor(Sqlite):
   
  table = "sensors"
  
  def __init__(self):
    Sqlite.__init__(self)
    #This table must be included in the default schema (see evolutions)
  
  def save(self,temperature, humidity, light):
    c = self._conn.cursor()
    now = int(time.time())
    datetime = time.strftime("%Y-%m-%d %H:%M:%S")
    print "[{}] Saving sensors: temperature {}, humidity {}, light {} ".format(datetime,temperature,humidity,light)

    c.execute("INSERT INTO sensors (timestamp,datetime,  temperature, humidity, light ) VALUES (?,?,?,?,?)",[now,datetime,temperature, humidity, light])
    self._conn.commit()
    c.close()
    
  def last(self):
    c = self._conn.cursor()
    c.execute('SELECT id,timestamp,date, temperature, humidity, light FROM sensors ORDER BY timestamp DESC LIMIT 1')
    result = c.fetchone()
    c.close()
    return result #If the key doesn't exists it will fail