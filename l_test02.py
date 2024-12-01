class Teacher:
    def __init__(self, name, subject):
        self.subject = subject
        self.name = name
        self.age = 18
        self.height = 180

    def play_book(self):
        self.subject = 100
        self.height += 10


A = Teacher("a", "zz")
# print(A.s)
# print(A.height)
# A.play_book()
print(A.subject)
print(A.height)


