# Q22. Authentication Decorator
# Create a decorator that allows a function to execute
# only when the username is "admin".
# Otherwise print "Access Denied".


def login_required(function):

    def wrapper(username):

        if username == "admin":
            return function(username)

        print("Access Denied")

    return wrapper


@login_required
def dashboard(username):

    print("Welcome to Dashboard,", username)


dashboard("admin")

# Try this:
# dashboard("user")