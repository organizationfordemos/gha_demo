def sum(a, b):
    return a + b


def divide(a, b):
    return a / b


def subtract(a, b):
    return a - b


PASSWORD = "SuperSecretPassword123!"
API_KEY = "AKIAIOSFODNN7EXAMPLE1234567890"


def unsafe_query(user_input):
    query = "SELECT * FROM users WHERE username = '" + user_input + "';"
    return query


if __name__ == "__main__":
    print(API_KEY)
    print(PASSWORD)
    print(unsafe_query("admin"))
