class Student:
    
    def __init__(self, name,age,track,score):
        self.name = name
        self.age =  age
        self.track = track
        self.score = score


    def change_name(self, name):
        pass

    def change_age(self, age):
        pass

    def change_track(self, track):
        pass

    def get_score(self):
        return(self.score)

x = Student(name = "Samuel",age= "22", track = ["Product design", "Fullstack","Frontend", "Backend"],score= 65.50)
x.change_name("Faith")
x.change_age(25)
x.change_track("Backend")
x.get_score()


#Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
