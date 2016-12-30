#How we structure programs

class Program():

    def __init__(self):

        self.language = input("What language?:")
        self.version = float(input("Version?:"))
        self.skill = input("What skill level?:")

    def upgrade(self):
        new_version = float(input("What version?:"))
        print("We have upgraded the version for", self.language)
        self.version = new_version

p1 = Program()
p2 = Program()


