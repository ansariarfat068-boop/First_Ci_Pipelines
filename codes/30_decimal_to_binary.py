"""Program 30: Convert a decimal integer to binary without bin()."""
def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Negative numbers are not supported")
    if number == 0:
        return "0"
    digits = ""
    while number > 0:
        remainder = number % 2
        digits = str(remainder) + digits
        number //= 2
    return digits
