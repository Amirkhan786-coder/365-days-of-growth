# Q23. Permission Decorator
# Create a decorator that checks whether the user
# has permission before accessing a function.


def permission_required(function):

    def wrapper(user, permission):

        if permission == "admin":
            return function(user, permission)

        print("Permission Denied")

    return wrapper


@permission_required
def delete_data(user, permission):

    print(user, "can delete data.")


delete_data("Amir", "admin")

# Try this:
# delete_data("Amir", "user")