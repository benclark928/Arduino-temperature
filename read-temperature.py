import serial 
import mysql.connector
import time
from decimal import Decimal
from datetime import datetime

#connects to mysql and find my database
dbConn = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='temperature')
#open a cursor to the database
cursor = dbConn.cursor()

device = 'COM3' #this will have to be changed to the serial port you are using
try:
    print("Trying...") 
    arduino = serial.Serial(device, 9600) 
except: 
    print("Failed to connect on")
while True:
    try:
        time.sleep(60)
        data = arduino.readline()  #read the data from the arduino
        temp = str(data)
        temp = temp.replace("b'", "")
        temp = temp.replace("\\r\\n'", "")

        now = datetime.now()
        current_time = now.strftime("%H:%M")

        print("Temp: %s, Time: %s" % (temp, current_time))

    except:
        print("Failed to get data from Arduino!")
    
    try:        
        add_temperature = ("INSERT INTO dht11serial "
                          "(temperature, currentTime) "
                          "VALUES (%s, %s)")
                          
        data_temperature = (temp, current_time,)

        cursor.execute(add_temperature, data_temperature)
        
        dbConn.commit() #commit the insert

    except Exception as e:
        print("failed to insert data")
        print(e)
