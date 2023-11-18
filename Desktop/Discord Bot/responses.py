import random

def get_response(user_message: str) -> str:
    print("get_response function is called!") #Test Cases
    p_message = user_message.lower()
    print(f"Checking message: {p_message}")
    print(f"Input user_message: {user_message}")#Test Cases
    print(f"Lowercased p_message: {p_message}")#Test Cases

    if p_message == 'hello':
        return 'Hello there'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'i love you':
        return 'I love you too Crundee'

    if p_message == 'whats':
        return 'moaning'

    if p_message == '!help':
        return " !dotroy "


    if p_message.startswith('!'):
        return 'This is a special command'

    return "I don't know what you said"
