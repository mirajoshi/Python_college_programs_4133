#Custom Excpetion
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative: " + str(age))
    elif age > 150:
        raise InvalidAgeError("Age is too large: " + str(age))
    else:
        print("Valid age:", age)

ages = [25, -5, 200]

for age in ages:
    try:
        validate_age(age)
    except InvalidAgeError as e:
        print("InvalidAgeError caught ->", e)
