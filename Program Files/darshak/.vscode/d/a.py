class person:
    def speak(self):
        print("person can speak")
class darshak(person):
    def write(self):
        print("person can write")
class xyz (darshak):
    def abc(self):
        print("person can sing also ")
x=xyz()
x.speak()
x.write()
x.abc()
