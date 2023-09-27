import random

ToDo = {'id': str, 'title': str, 'hasCompleted': bool}
ToDoList = list[ToDo]

todos: ToDoList = []


def generate_random_id(length=10):
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))


def create_new_todo(title: str):
    todo = {'id': generate_random_id(), 'title': title, 'hasCompleted': False}
    todos.append(todo)
    return todo


def update_todo(currentTodos: ToDoList, id: str):
    global todos

    def update_single_todo(todo: ToDo):
        if todo['id'] == id:
            todo['hasCompleted'] = not todo['hasCompleted']
        return todo

    updatedTodos = list(map(update_single_todo, currentTodos))

    todos = updatedTodos


def delete_todo(currentTodos: ToDoList, id: str):
    global todos

    updatedTodos = list(
        filter(lambda todo: todo['id'] != id, currentTodos)
    )

    todos = updatedTodos


print('---- Init ----')
print(todos)
print('\n')

create_new_todo('Primeiro ToDoList em Python! :D')
create_new_todo('Mais uma ToDoList em Python! :D')
create_new_todo('Preciso deletar essa! :D')
create_new_todo('Essa vai ser atualizada e a única no final! :D')

print('---- New ToDoList ----')
print(todos)
print('\n')

print('---- Updated ToDoList (hasCompleted) ----')
update_todo(todos, todos[1]['id'])
update_todo(todos, todos[3]['id'])
print(todos)
print('\n')

print('---- Deleted ToDoList ----')
delete_todo(todos, todos[0]['id'])
delete_todo(todos, todos[0]['id'])
delete_todo(todos, todos[0]['id'])
print(todos)
print('\n')
