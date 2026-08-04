# Question: Create a function that accepts multiple keyword arguments using **kwargs.

def student(**data):
    print(data)

student(Name="Amir", Age=19, City="Meerut")