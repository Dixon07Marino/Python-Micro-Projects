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
        #DONE

    def update_task(self):
        tasks.update({self.id_task: self.task})
        # self.done = True
        #DONE

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
            task = Tasks(number_task, task_is)
            task.create_task()
            print(tasks)
        elif choice == 'Visualizar':
            find_task = int(input('Ingresa el ID de la tarea que quieres visualizar: '))
            task.id_task = find_task
            task.read_task()
        elif choice == 'Actualizar':
            find_task = int(input('Ingresa el ID de la tarea que quieres actualizar: '))
            task.id_task = find_task
            task_is = input(f'Nueva tarea: ').strip().title()
            task.task = task_is
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


"""
{

"1": {
    "Task": "Comer"
    "DONE": True
},
"2": {
    "Task": "Comer"
    "DONE": False
},
"3": {
    "Task": "Comer"
    "DONE": True
}

#Posible solución

"4": ["comer", True]

}

"""