# Q30. REAL-WORLD DECORATOR SYSTEM
#
# Create a mini decorator system containing:
#
# @logger
# @performance
# @authentication
#
# The program should:
# 1. Check authentication.
# 2. Log the function call.
# 3. Measure execution time.
# 4. Execute the function.
# 5. Return the result.


import time
from functools import wraps


# ============================================================
# 🔐 AUTHENTICATION DECORATOR
# ============================================================

def authentication(function):

    @wraps(function)
    def wrapper(username, *args, **kwargs):

        if username != "admin":

            print("❌ Authentication Failed")

            return None

        print("✅ Authentication Successful")

        return function(username, *args, **kwargs)

    return wrapper


# ============================================================
# 📝 LOGGER DECORATOR
# ============================================================

def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("📝 Function Called:",
              function.__name__)

        return function(*args, **kwargs)

    return wrapper


# ============================================================
# ⏱️ PERFORMANCE DECORATOR
# ============================================================

def performance(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print(
            "⏱️ Execution Time:",
            end - start,
            "seconds"
        )

        return result

    return wrapper


# ============================================================
# 🚀 APPLY DECORATORS
# ============================================================

@authentication
@logger
@performance
def dashboard(username):

    print("🎯 Welcome to the Dashboard,", username)

    total = 0

    for i in range(1000000):
        total += i

    return total


# ============================================================
# PROGRAM START
# ============================================================

print("================================")
print("       DECORATOR SYSTEM")
print("================================")

result = dashboard("admin")

print("Result:", result)

print("================================")