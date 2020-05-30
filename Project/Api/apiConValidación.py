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
    
    # ---- Se insertan datos del SO
    def insertInfoServer(self, IP, Processor, ProcessorType):
        sql = "INSERT INTO `InfoServer`(`IP`, `ProcessorInfo`,`ProcessorType`  ) VALUES ('{}','{}','{}')".format(IP, Processor, ProcessorType)
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
            sql = "INSERT INTO `ActiveUsers`(`IP`, `Users`) VALUES ('{}','{}')".format(IP, User)
            try:
                self.cursor.execute(sql) 
                self.connection.commit() #envio a la BD
            except Exception as e:
                print(e)
                raise      
    def insertProcess(self, IP, Process, User):
            sql = "INSERT INTO `ActiveProcess`(`IP`, `Process`,`User`) VALUES ('{}','{}')".format(IP, Process, User)
            try:
                self.cursor.execute(sql) 
                self.connection.commit() #envio a la BD
            except Exception as e:
                print(e)
                raise

    def updateActiveUsers(self,IP,User):
        sql ="UPDATE `ActiveUsers` SET `IP`= '{}',`Users`= '{}'".format(IP,User)
        try:
                self.cursor.execute(sql) 
                self.connection.commit() #envio a la BD
        except Exception as e:
            print(e)
            raise

    def updateProcess(self,IP,Process):
        sql ="UPDATE `ActiveUsers` SET `IP`= '{}',`Process`= '{}'".format(IP,Process)
        try:
                self.cursor.execute(sql) 
                self.connection.commit() #envio a la BD
        except Exception as e:
            print(e)
            raise

            
    #Función para validar si ya existen datos en la base        
    def getBDSVInfo(self):
        sql = 'SELECT IP,SOName,SOVersion,ProcessorInfo FROM InfoServer'

        try:
            self.cursor.execute(sql)
            svInfo = self.cursor.fetchall()
            #print(svInfo)
        except Exception as e:
            print (e)
            raise
        return svInfo
        
    #Función para validar si ya existen datos en la base          
    def getBDProcess(self):
        sql = 'SELECT `IP`, `Process` FROM `ActiveProcess`' 

        try:
            self.cursor.execute(sql)
            proc = self.cursor.fetchall()
            
        except Exception as e:
            print (e)
            raise
        return proc
        
    #Función para validar si ya existen datos en la base          
    def getBDUsers(self):
        sql = 'SELECT `IP`, `Users` FROM `ActiveUsers`' 
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
        except Exception as e:
            print (e)
            raise
        return user
    
    def getBDUsersByIP(self, IP):
        sql = "SELECT `IP`, `Users` FROM `ActiveUsers` WHERE IP = '{}'".format(IP) 
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
        except Exception as e:
            print (e)
            raise
        return user
    

  
database = DataBase()
#Llamada a las funciones con la información obtenida
SO = getSO() #info que obtiene el agente sobre el SO
IP = getIP() #IP
processor = getProcessor() #información del procesador
process = getProcess() # Procesos activos
users = getUsers()
#Valida si existe información
'''database.getBDProcess()
processList = DataBase().getBDProcess()
for pro in process:
    for p in processList:
        print (p)
        if p[0] == IP:
            database.updateProcess(IP,pro)
        else: 
            database.insertProcess(IP,pro)'''
    
database.getBDUsers()

hasUser = database.getBDUsersByIP(IP)
print(hasUser)
if hasUser:
    database.updateActiveUsers(IP,users)
else:
    database.insertActiveUsers(IP,users)
    

database.insertInfoServer(IP,processor['pro'], processor['proType'])
database.insertOSInfo(IP,SO['SO_name'], SO['SO_version'])


for user in users: 
    database.insertActiveUsers(IP,user)
    
for pro in process:
    database.insertProcess(IP,pro,users)






 
    
