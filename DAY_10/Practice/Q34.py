# Question:
# Use the random module to generate a 6-digit OTP.

import random

otp = random.randint(100000, 999999)

print("Your OTP is:", otp)