'''
En un principio vamos a usar como base de datos SQLite, pero el objetivo es intentar implementar llamadas a APIs
o manipulación de archivos de algun tipo para cumplir con la naturaleza de este proyecto

gestor.py funcionaria como modelo siguiendo la arquitectura MVC para tener separada la manipulación de datos, la
modularizacón, estructura e implementación de bases de datos esta abierta a cambios 

'''
# python -m venv venv
# .\venv\Scripts\activate


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.crear_db import get_connection

def create_client(name, phone):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO clients (name, phone) VALUES (?, ?)"
    cursor.execute(query, (name, phone))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def create_med(name, dosage):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO medications (name, dosage) VALUES (?, ?)"
    cursor.execute(query, (name, dosage))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def create_schedule(client_id, med_id, hour):
    conn = get_connection()
    cursor = conn.cursor()
    # Format "08:30"
    query = "INSERT INTO schedules (client_id, med_id, hour) VALUES (?, ?, ?)"
    cursor.execute(query, (client_id, med_id, hour))
    conn.commit()
    conn.close()
    
def get_reminders_for_current_time(current_time):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = '''
        SELECT clients.name, clients.phone, medications.name, schedules.hour
        FROM schedules
        JOIN clients ON schedules.client_id = clients.client_id
        JOIN medications ON schedules.med_id = medications.med_id
        WHERE schedules.hour = ?
    '''
    
    cursor.execute(query, (current_time,))
    results = cursor.fetchall()
    conn.close()
    return results