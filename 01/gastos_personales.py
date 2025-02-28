import json

class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.total_ingresos = 0
        self.total_gastos = 0

    def ingresar_dinero(self) -> float:
        while True:    
            try:
                return float(input(f"{self.nombre}, ingresa tu dinero 💰: "))
            except ValueError:
                print("Ingresa un número valido!")

    def gastar_dinero(self) -> float:
        while True:
            try:
                return float(input(f"{self.nombre}, ingresa el monto de lo que gastaste 💸: "))
            except ValueError:
                    print("Ingresa un número valido!")
    
    def obtener_saldo(self) -> float:
        return self.total_ingresos - self.total_gastos

    def mostrar_total_disponible(self):
        print(f"{self.nombre}, el total de dinero 💸 en tu billetera es: {self.obtener_saldo():,.2f}")
    
#Opciones disponibles en el programa
opciones: list[str] = ["Ingresar", "Gastar", "Visualizar", "Salir"]
    
print("¡Bienvenido a tu gestor de gastos personales! 💰")
nombre: str = input(f"Querido, coloca tu nombre: ").strip().title()

#Instanciando clase Persona
persona = Persona(nombre)

#Cargar Datos del Json

with open("datos.json", mode="r") as json_file:
    datos_cargados = json.load(json_file)

persona.total_ingresos = datos_cargados["Ingresos"]
persona.total_gastos = datos_cargados["Gastos"]

#Programa
while True:
    opcion: str = input(f"Querido {persona.nombre}, por favor elige lo que quieres hacer: {opciones}").strip().title()
    if opcion in opciones:
        if opcion == "Ingresar":
            ingreso: float = persona.ingresar_dinero()
            persona.total_ingresos += ingreso
            print(f"{persona.nombre}, ingresaste: {ingreso:,.2f}$ 💸")
        elif opcion == "Gastar":
            gasto: float = persona.gastar_dinero()
            if gasto > persona.obtener_saldo():
                print(f"Dinero Insuficiente, tienes: {persona.obtener_saldo():,.2f}$")
            else:
                persona.total_gastos += gasto
                print(f"{persona.nombre}, gastaste: {gasto:,.2f}$ 💸")
        elif opcion == "Visualizar":
            persona.mostrar_total_disponible()
        else:
            print("Saliste del programa 🏦, vuelve pronto!")
            break
    else:
        print("❌Opcion no disponible en el programa!")

#Ingresar datos actualizados al JSON

datos = {
    "Nombre": persona.nombre,
    "Ingresos": persona.total_ingresos,
    "Gastos": persona.total_gastos,
    "Disponible": persona.obtener_saldo()
}

with open("datos.json", mode="w") as json_file:
    json.dump(datos, json_file, indent=4)

