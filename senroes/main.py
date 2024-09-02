import threading
import time
import random
from pymongo import MongoClient

#conectando com o mongo
client = MongoClient("mongodb://localhost:27017/")
db = client["bancoiot"]
collection = db["sensores"]

sensores = [
    {"nomeSensor": "Sensor1", "valorSensor": None, "unidadeMedida": "C°", "sensorAlarmado": False},
    {"nomeSensor": "Sensor2", "valorSensor": None, "unidadeMedida": "C°", "sensorAlarmado": False},
    {"nomeSensor": "Sensor3", "valorSensor": None, "unidadeMedida": "C°", "sensorAlarmado": False}
]

for sensor in sensores:
    collection.update_one({"nomeSensor": sensor["nomeSensor"]}, {"$setOnInsert": sensor}, upsert=True)

def sensor_simulação(sensor):
    while 1:
        estado_sensor = collection.find_one({"nomeSensor": sensor})
        
        if estado_sensor["sensorAlarmado"]:
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {sensor}!")
            break
        
        valor_temp = random.uniform(30, 40)
        print(f"{sensor} - Temperatura: {valor_temp:.2f} C°")
        
        collection.update_one(
            {"nomeSensor": sensor},
            {"$set": {"valorSensor": valor_temp, "sensorAlarmado": valor_temp > 38}}
        )

        if valor_temp > 38:
            print(f"Atenção! Temperatura muito alta! Verificar {sensor}!")
            break

        time.sleep(2)
        
s1 = threading.Thread(target=sensor_simulação, args=(f"Sensor{1}",))
s1.start()
s2 = threading.Thread(target=sensor_simulação, args=(f"Sensor{2}",))
s2.start()
s3 = threading.Thread(target=sensor_simulação, args=(f"Sensor{3}",))
s3.start()