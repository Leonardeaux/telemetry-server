def param_to_message(**kwargs: str):
    message = "{"
    for key, value in kwargs.items():
        message += f'"{key}": {value},'

    message = message[:-1]
    message += '}\n'
    return message
