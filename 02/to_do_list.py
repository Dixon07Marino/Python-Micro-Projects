#Usar Json para almacenar tareas del to-do-list
import json

#Cargar JSON
with open('tasks.json', mode='r') as tasks_file:
    tasks_from_json = json.load(tasks_file)

#Dicc de tareas

tasks = tasks_from_json

#Lista de opciones CRUD

choices = ['Crear', 'Visualizar', 'Actualizar', 'Eliminar', 'Salir']

#Clase tareas

class Tasks:
    def __init__(self, id_task, task):
        self.id_task = id_task
        self.task = task
          
    def create_task(self):
        tasks.update({self.id_task: self.task})
    
    def read_task(self):
        print(f'Task: {tasks[self.id_task]}')

    def update_task(self):
        tasks.update({self.id_task: self.task})

    def delete_task(self):
        tasks.pop(self.id_task)

#Programa to_do_list

number_task = len(tasks)
print(f'¡Bienvenido a tu lista de tareas!')

while True:
    choice = input(f'Elije la opción que quieres realizar: ').strip().title()
    if choice in choices:
        if choice == 'Crear':
            number_task += 1
            task_is = input(f'Crea tu tarea: ').strip().title()
            lista = [task_is, False]
            task = Tasks(number_task, lista)
            task.create_task()
            print(tasks)
        elif choice == 'Visualizar':
            find_task = int(input('Ingresa el ID de la tarea que quieres visualizar: '))
            task.id_task = find_task
            task.read_task()
        elif choice == 'Actualizar':
            find_task = int(input('Ingresa el ID de la tarea que quieres actualizar: '))
            action = int(input(f'Coloca 1, si quieres reemplazar la tarea\ny 2 si quieres cambiar el estado de la tarea: '))
            task.id_task = find_task
            if action == 1:
                task_is = input(f'Nueva tarea: ').strip().title()
                task.task[0] = task_is
            elif action == 2:
                task.task[1] = True
            task.update_task()
        elif choice == 'Eliminar':
            find_task = int(input('Ingresa el ID de la tarea que quieres eliminar: '))
            task.id_task = find_task
            task.delete_task()
        else:
            break
    else:
        print('¡Elije una opción valida!')

print(tasks)

#Ingresar datos al JSON
with open('tasks.json', mode='w') as tasks_file:
    json.dump(tasks, tasks_file, indent=2)