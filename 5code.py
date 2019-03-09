class Student(object):
    def __init__(self, name, another_name):
        self.name = name
        self.another_name = another_name

    def call(self):
        number = input('请输入你要拨打电话：')
        print('你要拨打的电话为{}。'.format(number))

    def answer(self):
        print('你拨打的用户是{name}，另一个名称是{another_name}。'.format(name = self.name, another_name = self.another_name))

if __name__ == '__main__':
    student = Student('胡子鹏', 'wings')
    print('名字：{0}，小名：{1}'.format(student.name, student.another_name))
    student.call()
    print('*' * 50)
    student.answer()


