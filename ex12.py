import json, os
list_task = []
CAMINHO_DIR = os.path.dirname(__file__) #Pasta aonde me encontro, letra maiscula para representar constantes
SAVE_TO = os.path.join(CAMINHO_DIR, "ex12.json")
def switch(option):
    optionUpper = option.upper()
    if optionUpper == "LISTAR":
        return listTask()
    elif optionUpper == "DESFAZER":
        return remove_Task()
    elif optionUpper == "REFAZER":
        return remake_task()
    else:
        return add_Task(option)

def add_Task(task):
    list_task.append(task)
    list_write_json(task)
    listTask()

def remove_Task():
    numberTask = len(list_task) -1
    del list_task[numberTask]

    return listTask(value="remove_Task")
    
def remake_task():
        with open(SAVE_TO,"r") as file:
            tasks = json.load(file)#agora ja o load e de puxar e que nos da o poder de ler o arquivo
            for  i in range(len(tasks)):
                if tasks[i] not in list_task :
                    list_task.append(tasks[i])
                    return listTask()
            print()
            print("Nenhuma tarefa para refazer")
            print()

def listTask(value=""):
    if value == "remove_Task":
        if len(list_task) == 0:
            print()
            print("Não á nenhuma tarefa")
            print()
        else:
            print()
            print("Tarefas: ")
            print()
            for task in list_task:
                print(task)
            print() 
    else:
        if len(list_task) == 0:
            print()
            print("Não á nenhuma tarefa")
            print()
        else:
            print()
            print("Tarefas: ")
            print()
            for task in list_task:
                print(task)
            print()
            
def list_write_json(task, lista=[]):
    lista.append(task)
    with open(SAVE_TO,"w") as file:
        json.dump(lista, file, indent=2)

def start():
    welcome = "Bem-Vindo a Lista de Tarefas"
    print("#"*len(welcome))
    print(f"{welcome}")
    print("#"*len(welcome))
    while True:
        print("Comandos: Listar, Desfazer, Refazer ")
        option=input("Digite uma tarefa ou comando: ")
        switch(option)

start()