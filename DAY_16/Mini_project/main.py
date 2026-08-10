# ============================================================
# 🚀 DAY 16 MINI PROJECT
# PERFORMANCE MONITOR & ACCESS LOGGER
# ============================================================
#
# Concepts Used:
#
# 1. First-Class Functions
# 2. Higher-Order Functions
# 3. Nested Functions
# 4. Closures
# 5. Decorators
# 6. Wrapper Functions
# 7. *args
# 8. **kwargs
# 9. functools.wraps
# 10. Multiple Decorators
# 11. Authentication
# 12. Logging
# 13. Performance Monitoring
#
# ============================================================

import time
from functools import wraps


# ============================================================
# 1. AUTHENTICATION DECORATOR
# ============================================================

def authentication(function):
    """
    Authentication decorator.

    Only the username 'admin'
    is allowed to access the dashboard.
    """

    @wraps(function)
    def wrapper(username, *args, **kwargs):

        # Check username
        if username != "admin":

            print("\n❌ Authentication Failed")
            print("❌ Access Denied!")

            return None

        # Authentication successful
        print("\n✅ Authentication Successful")

        # Execute original function
        return function(username, *args, **kwargs)

    return wrapper


# ============================================================
# 2. LOGGING DECORATOR
# ============================================================

def logger(function):
    """
    Logging decorator.

    Displays the name of the function
    being executed.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Display function name
        print("📝 Function Called:", function.__name__)

        # Execute original function
        return function(*args, **kwargs)

    return wrapper


# ============================================================
# 3. PERFORMANCE DECORATOR
# ============================================================

def performance(function):
    """
    Performance decorator.

    Measures the execution time
    of the original function.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Record start time
        start_time = time.time()

        # Execute original function
        result = function(*args, **kwargs)

        # Record end time
        end_time = time.time()

        # Calculate execution time
        execution_time = end_time - start_time

        print(
            f"⏱️ Execution Time: "
            f"{execution_time:.6f} seconds"
        )

        # Return result
        return result

    return wrapper


# ============================================================
# 4. DASHBOARD FUNCTION
# ============================================================

@authentication
@logger
@performance
def dashboard(username):
    """
    Dashboard function.

    Performs a calculation after
    successful authentication.
    """

    print(
        f"\n👋 Welcome to the Dashboard, {username}!"
    )

    # Variable for storing total
    total = 0

    # Calculate sum from 1 to 999999
    for number in range(1, 1000000):

        total += number

    # Return final result
    return total


# ============================================================
# 5. MAIN PROGRAM
# ============================================================

print("=" * 55)

print(
    "       PERFORMANCE MONITOR & ACCESS LOGGER"
)

print("=" * 55)


# ============================================================
# 6. USER INPUT
# ============================================================

username = input(
    "\nEnter username: "
)


# ============================================================
# 7. CALL DASHBOARD
# ============================================================

result = dashboard(username)


# ============================================================
# 8. DISPLAY RESULT
# ============================================================

if result is not None:

    print(
        "\n🧮 Calculation Result:",
        result
    )

    print(
        "\n✅ Program completed successfully."
    )

else:

    print(
        "\n⚠️ Program stopped because "
        "authentication failed."
    )


# ============================================================
# 9. END PROGRAM
# ============================================================

print("\n" + "=" * 55)

print(
    "                    THANK YOU"
)

print("=" * 55)