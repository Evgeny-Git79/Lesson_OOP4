class Task():

    def __init__(self):
        self.task_list = []

    def task_add(self, id, description, date_done, status):
        self.id = id
        self.description = description
        self.date_done = date_done
        self.status = status
        self.task_list.append([self.id, self.description, self.date_done, self.status])
        print(f"Создана задача {self.id} c датой {self.date_done} выполнения , статус {self.status}")
        #print(self.task_list)

    def task_print_status(self, id):
        self.id = id
        self.task = self.task_list[self.id - 1]
        print(f"Статус {self.id} задачи {self.task[3]}")

    def task_mark_done (self, id):
        self.id = id
        self.task = self.task_list.pop(id - 1)
        self.status = self.task.pop(3)
        self.task.append("1")
        self.task_list.insert(id-1, self.task)


id = 1
description = "задача"
date_done = "date_done"
status = "0"
list = Task()
list.task_add(id, description, date_done, status)

id = 2
description = "задача2"
date_done = "date_done2"
status = "0"
list.task_add(id, description, date_done, status)

id = 2
list.task_print_status(id)
list.task_mark_done(id)
list.task_print_status(id)

