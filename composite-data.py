import csv
import copy

# Definición del diccionario myVehicle
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Imprimir las propiedades iniciales de myVehicle
print("Propiedades iniciales de myVehicle:")
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Lista para almacenar los vehículos
myInventoryList = []

# Leer el archivo CSV y procesar su contenido
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Nombres de las columnas: {", ".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = int(row[3])  # Convertir año a entero
            currentVehicle["range"] = int(row[4])  # Convertir rango a entero
            currentVehicle["topSpeed"] = int(row[5])  # Convertir velocidad máxima a entero
            currentVehicle["zeroSixty"] = float(row[6])  # Convertir zeroSixty a flotante
            currentVehicle["mileage"] = int(row[7])  # Convertir kilometraje a entero
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')

# Imprimir las propiedades de cada vehículo en myInventoryList
print("Inventario de vehículos:")
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")
