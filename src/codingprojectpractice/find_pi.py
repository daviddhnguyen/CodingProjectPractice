import math

def find_pi(n):
    # Set precision a few digits higher than n for accuracy
    if n>50:
        return "Error too many digits; enter 50 or less!"

    pi = math.pi
    # Return as string, trimming the extra digits
    return str(pi)[:n+2]  # 1 digit before the decimal + n digits after