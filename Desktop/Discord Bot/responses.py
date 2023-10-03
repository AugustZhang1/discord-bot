import random
import bot


def get_response(message : str)->str:
    p_message = message.lower()


    if p_message == 'hello':
        return 'Hello there'

    if  p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == 'i love you':
        return 'I love you too Crundee'
    
    if p_message == 'whats':
        return 'moaning'
    

        

    
    
    if p_message == '!help':
        return "`This is a help message that you can modify`"
    
    return " I don't know what you said"