from abc import ABC, abstractmethod



class AbsClass(ABC):

    def print(self,x):
        print("Value:",x)


    @abstractmethod
    def task(self):
        print("We are inside a abstract class.")




class Test_Class(AbsClass):
    def task(Self):
        print("We are inside a text class.")



test_obj = Test_Class()
test_obj.task()
test_obj.print(100)
