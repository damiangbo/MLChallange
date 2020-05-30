from flask import Flask, jsonify
import pymysql
from getInfo import *
# Connect to the MySQL database

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='remotemysql.com',
            port =3306,
            user = 'cJ9ZD5EpTk',
            password = 'gAXLY3ihxH',
            db = 'cJ9ZD5EpTk',
            charset ='utf8mb4',
        )
        self.cursor = self.connection.cursor()
        print ("Conexión establecida existosamente")
    

    '''def getBDInfo(self):
        sql = 'SELECT IP,SOName,SOVersion,ProcessorInfo FROM InfoServer'

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            print ("IP:",user[0])
            print ("SOVersion:",user[1])
            print ("SOName",user[2])
            print ("ProcessorInfo",user[3])
        except Exception as e:
            print (e)
            raise'''

    # ---- Se insertan datos del SO
    def insertInfoServer(self, IP, Processor, ProcessorType):
        sql = "INSERT INTO `InfoServer`(`IP`, `ProcessorInfo`,`ProcessorType`) VALUES ('{}','{}','{}')".format(IP, Processor, ProcessorType)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)
            raise

    def insertOSInfo(self, IP, SOName, SOVersion):
        sql = "INSERT INTO `SOInfo`(`IP`, `SOName`, `SOVersion` ) VALUES ('{}','{}','{}')".format(IP, SOName, SOVersion)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)
            raise    

    def insertActiveUsers(self, IP, User):
        sql = "INSERT INTO `ActiveUsers`(`IP`, `User`) VALUES ('{}','{}')".format(IP, User)
        try:
            self.cursor.execute(sql) 
            self.connection.commit() #envio a la BD
        except Exception as e:
            print(e)
            raise      

    def insertProcess(self, IP, Process):
        sql = "INSERT INTO `ActiveProcess`(`IP`, `Process`) VALUES ('{}','{}')".format(IP, Process)
        try:
            self.cursor.execute(sql) 
            self.connection.commit()
        except Exception as e:
            print(e)
            raise
#Llamada a las funciones con la información obtenida
SO = getSO() #info que obtiene el agente sobre el SO
IP = getIP() #IP obtenida
users = getUsers() #Usuarios activos
process = getProcess() # Procesos activos
processor = getProcessor() #información del procesador

#Conexión a BD
database = DataBase()

#Ejecución de los insert a la base
database.insertInfoServer(IP,processor['pro'], processor['proType'])
database.insertOSInfo(IP,SO['SO_name'], SO['SO_version'])

for user in users: 
    database.insertActiveUsers(IP,user)

for pro in process:
        database.insertProcess(IP,pro)


    
