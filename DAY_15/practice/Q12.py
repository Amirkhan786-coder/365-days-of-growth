# Q12. Demonstrate multiple inheritance using Father and Mother.

class Father:

    def father_skill(self):
        print("Father's skill")


class Mother:

    def mother_skill(self):
        print("Mother's skill")


class Child(Father, Mother):

    def child_skill(self):
        print("Child's skill")


child1 = Child()

child1.father_skill()
child1.mother_skill()
child1.child_skill()