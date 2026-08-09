# Q13. Use constructors in a multiple inheritance example.

class Father:

    def __init__(self, father_name):
        self.father_name = father_name


class Mother:

    def __init__(self, mother_name):
        self.mother_name = mother_name


class Child(Father, Mother):

    def __init__(self, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)


child1 = Child("Ramesh", "Sunita")

print("Father:", child1.father_name)
print("Mother:", child1.mother_name)