class StringTasks:
    def __init__(self):
        self.mystring = ""

    def getString(self):
        self.mystring = input("Enter your name: ")

    def printString(self):
        print("Your name with big letters:", self.mystring.upper())

task = StringTasks()
task.getString()
task.printString()
