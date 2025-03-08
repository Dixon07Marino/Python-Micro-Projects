import requests, json

print(f"Bienvenido al programa: Rick and Morty.")
nombre = input("Coloca tu nombre: ").strip().title()

#buscar, agregar/quitar a favoritos y salir

def accion_usuario():
    while True:
        try:
            number = int(input(f"{nombre}. Por favor, dinos lo que quieres hacer:\n1.Buscar personajes\n2.Agregar a favoritos\n3.Quitar de favoritos\n4.Salir del programa "))
            return number
        except ValueError as noNumero:
            print(f"No ingresaste un número! Error: {noNumero}")


while True:
    opcion = accion_usuario()
    if opcion in [1, 2, 3, 4]:
        if opcion == 1:
            id_number = input(f"{nombre}. Busca a tu personaje por el ID: ")
            url = "https://rickandmortyapi.com/api/character/" + id_number
            respuesta = requests.get(url).json()
            name, gender, status, species, location = respuesta["name"], respuesta["gender"], respuesta["status"], respuesta["species"], respuesta["location"]["name"]
            print(f"Nombre: {name}\nGenero: {gender}\nEstado: {status}\nEspecie: {species}\nUbicación: {location}")
        elif opcion == 2:
            id_number = input(f"{nombre}. Busca al personaje que vas a agregar por el ID: ")
            url = "https://rickandmortyapi.com/api/character/" + id_number
            respuesta = requests.get(url).json()
            name, gender, status, species, location = respuesta["name"], respuesta["gender"], respuesta["status"], respuesta["species"], respuesta["location"]["name"]
            character = {
                "name": name,
                "gender": gender,
                "status": status,
                "species": species,
                "location": location
            }
            #agregar a json
            with open("characters.json", mode="a") as file:
                json.dump(character, file, indent=4)
        elif opcion == 3:
            break
    else:
        print("Opción inválida!")