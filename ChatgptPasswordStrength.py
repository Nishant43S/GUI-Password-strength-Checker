def check_password_strength(password):
    # Criteria points
    points = {
        'length': 3,           # Minimum length of 3 characters
        'uppercase': 2,        # Points for at least one uppercase letter
        'lowercase': 1,        # Points for at least one lowercase letter
        'special': 3,          # Points for at least one special character
        'number': 1            # Points for at least one digit
    }

    total_points = 0

    # Check each criterion and calculate points
    if len(password) >= points['length']:
        total_points += points['length']

    if any(char.isupper() for char in password):
        total_points += points['uppercase']

    if any(char.islower() for char in password):
        total_points += points['lowercase']

    if any(char.isdigit() for char in password):
        total_points += points['number']

    if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>/?'" for char in password):
        total_points += points['special']

    # Determine strength based on total points
    if total_points >= 14:
        return "Password is very strong! Total points: {}".format(total_points)
    elif total_points >= 12:
        return "Password is strong! Total points: {}".format(total_points)
    elif total_points >= 10:
        return "Password is less strong! Total points: {}".format(total_points)
    elif total_points >= 8:
        return "Password is good! Total points: {}".format(total_points)
    elif total_points >= 6:
        return "Password is medium! Total points: {}".format(total_points)
    else:
        return "Password is weak. Total points: {}".format(total_points)

# Test the function
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
