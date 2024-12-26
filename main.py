class Task():

    def __init__(self, id, description, date_done, status):
        self.id = id
        self.description = description
        self.date_done = date_done
        self.status = status
        


    def task_add(self, id, description, date_done, status):
        self.id = id
        self.description = description
        self.date_done = date_done
        self.status = status
        print(f"Создана задача {self.id} c датой {self.date_done} выполнения , статус {self.status}" )
