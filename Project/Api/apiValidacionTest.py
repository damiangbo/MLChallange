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
    def insertInfoServer(self, IP, SOName, SOVersion, Processor):
        sql = "INSERT INTO `InfoServer`(`IP`, `SOName`, `SOVersion`,`ProcessorInfo` ) VALUES ('{}','{}','{}','{}')".format(IP, SOName, SOVersion, Processor)
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
    def insertProcess(self, query):
            sql = "INSERT INTO `ActiveProcess`(`IP`, `Process`) VALUES {}".format(query)
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
            #print (user)
        except Exception as e:
            print (e)
            raise
        return user
    

  
database = DataBase()
#Llamada a las funciones con la información obtenida
SO = getSO() #info que obtiene el agente sobre el SO
IP = getIP() #IP
Processor = getProcessor() #información del procesador
#Valida si existe información
''''processList = DataBase().getBDProcess()
print (processList[0])
for p in processList:
    for pr in processList:
        print(pr[0])'''

     
database.getBDProcess()

users = getUsers() #Usuarios activos
process = getProcess() # Procesos activos

userList = DataBase().getBDUsers()
for user in users:
    for u in userList:
        if u == IP:
            database.insertActiveUsers(IP,users)
        else:
            database.insertActiveUsers(IP,users)


database.getBDUsers()




database.insertInfoServer(IP,SO['SO_name'], SO['SO_version'],Processor)
database.getBDSVInfo()


'''for user in users: #PROBAR ESTO EN ALGUNA COMPUTADORA QUE TENGA VARIAS SESIONES
    database.insertActiveUsers(IP,user)'''

processDataParsed = ''

for index, pro in enumerate(process, start=1):
    processDataParsed = processDataParsed + '(' + "'"+ IP + "'" + ',' +  "'" + pro + "'" + ')'
    
    if index != len(process): 
        processDataParsed = processDataParsed + ','  
database.insertProcess(processDataParsed)




 
    
