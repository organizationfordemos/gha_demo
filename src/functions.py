def sum(a, b):
    return a + b


def divide(a, b):
    return a / b


def subtract(a, b):
    return a - b


password = "MySuperSecretPassword123!"
API_TOKEN = "1234567890abcdef1234567890abcdef"
AZURE_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IkpXVC1L...fake-token-for-demo..."
)


def unsafe_query(user_input):
    query = "SELECT * FROM users WHERE username = '" + user_input + "';"
    return query
