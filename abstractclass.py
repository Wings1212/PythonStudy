from abc import ABC, abstractclassmethod
import webbrowser


class MyClass(ABC):
    @abstractclassmethod
    def study(self, *args, **kwargs):
        pass

    @abstractclassmethod
    def read(self, *args, **kwargs):
        pass


class Student(MyClass):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, *args, **kwargs):
        dream = input('{0},你的梦想是什么？'.format(self.name))
        if dream == 'money':
            print('you are not good')
        else:
            print('ok, you are good')

    def read(self, *args, **kwargs):
        try:
            webbrowser.open('http://www.baidu.com')
        except Exception as ret:
            print(ret)
            raise ValueError from None
        else:
            print('the website was opened')


if __name__ == '__main__':
    student = Student('胡子鹏', 21)
    # 不能实例化抽象基类，继承于抽象基类的类必须重写其抽象方法要不也没法实例化
    # h = MyClass()
    student.study()
    print("*" * 50)
    student.read()
