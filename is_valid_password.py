def is_palinrome(number):
    return str(number) == str(number)[::-1]


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_even(number):
    return number % 2 == 0


def is_valid_password(password):
    parts = password.split(':')

    if len(parts) != 3:
        return False

    try:
        a = int(parts[0])
        b = int(parts[1])
        c = int(parts[2])
    except ValueError:
        return False

    if is_palinrome(a) and is_prime(b) and is_even(c):
        return True

    return False


psw = input()
print(is_valid_password(psw))
