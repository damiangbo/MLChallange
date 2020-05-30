import platform 
import psutil
import json
import socket
import cpuinfo

def getUsers():
# ----- Usuarios con sesión abierta en el sistema
    users_list = []
    for user in psutil.users(): #Users: Return users currently connected on the system as a list of namedtuples including the following fields
        users_list.append(user.name)
    return users_list

def  getProcessor():
    # ----- Información sobre el procesador
    processor = platform.processor()
    processorType = cpuinfo.get_cpu_info()["brand"]
    return  {'pro' : processor, 'proType' : processorType}

def getSO():
    # ----- Nombre y versión del SO
    so = platform.system()
    so_version = platform.version()
    return {'SO_name' : so, 'SO_version' : so_version}

# ----- Listado de procesos corriendo
def getProcess():
    processes = []
    for process in psutil.process_iter():
        processes.append(process.name())
    return (processes)

# ---- Obtiene la IP
def getIP():
    name = socket.gethostname()
    ip = socket.gethostbyname(name)
    return (ip)

