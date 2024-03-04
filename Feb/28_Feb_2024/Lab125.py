from abc import ABC, abstractmethod

class ATB(ABC):

    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass

class Amit(ATB): # whenever you enforce something, will use abstraction

    def perform_task1(self):
        return "Task1"

    def perform_task2(self):
        return "Task2"

amit = Amit()
print(amit.perform_task1())
print(amit.perform_task2())
