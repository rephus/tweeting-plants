import time
from gpio.resistance import Resistance
from gpio.motor import Motor
from db.sensor import Sensor
from db.action import Action
#GPIO components should be in a different file

#GPIO.setmode(GPIO.BOARD)
light = Resistance(7)
humidity = Resistance(8)
temperature = Resistance(10)
pump = Motor (11)

#In degrees
TEMPERATURE_LOW = 10
TEMPERATURE_HIGH = 25

HUMIDITY_LOW = 1
HUMIDITY_HIGH = 2

LIGHT_LOW = 1
LIGHT_HIGH = 2

timeBetweenTweets = 60*60 # 1 hour
timeBetweenTopics = 60*60*24 # 1 day

sensor = Sensor()
action = Action()

def collectData():
    sensor.save(temperature = temperature.get(), humidity = humidity.get(), light = light.get())
    
def getPhrase(topic):
    #TODO: Get a random phrase here acording to the topic (a map[string,seq[string]] would be great)
    return topic
    
def tweet(topic): 
    lastTweet = action.last("tweet")
    
    since = timeSince(lastTweet)
    print "lastTweet was {} seconds ago".format(since)
    if since > timeBetweenTweets:
        lastTopic = action.last("tweet", category = topic)
        since = timeSince(lastTopic)
        print "lastTopic {} was {} seconds ago".format(topic,since)
        if since >  timeBetweenTopics :
            phrase = getPhrase(topic)
            print "Tweeting about {}: {} ".format(topic,phrase)
            action.save("tweet",topic, phrase)
            #TODO: Tweet random phrase

def timeSince(action): # in seconds
  now = int(time.time())
  if action == None:
    return now
  else: 
    timestamp = int(action[1])
    return now - timestamp

#It maybe not the last data stored, so it's easier to use a different function rather than collectData 
def ai():
  pass
  #TODO: Create a method for every different behaviour
      #TODO: Collect data (last, avg, last x, etc)
      #TODO: Check data
      #TODO: Do something
  
  #eg: 
  #isCold()
  #isDry()
  #Can we include all this methods in an array or something ? 

'''    
def isCold():
    temperature = sensor.last()
    if temperature[2] < TEMPERATURE_LOW:
        tweet("cold") 

def isDry():
    humidity = sensor.last()
    if int(humidity[2]) < HUMIDITY_LOW:
        tweet("dry") 
        #enablePump(PIN_PUMP)
    else: 
        print "disable Pump"
        #disablePump(PIN_PUMP)
'''
print "Running 'tweeting-plants', press Ctrl+C to exit"    
try: 
    while True:
        collectData()
        ai() #Artificial intelligence
        time.sleep(30) #30 seconds
        
except KeyboardInterrupt:
    print "Quit"
 
