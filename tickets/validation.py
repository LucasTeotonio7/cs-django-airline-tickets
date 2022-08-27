def equals_origin_destiny(origin: str, destiny: str, errors_list: list):
    """check if origin and destiny are the same

    Args:
        origin `str`: value of the departure point of the trip
        destiny `str`: travel arrival point value
        errors_list `list`: list to store errors
    """
    if origin == destiny:
        errors_list['destiny'] = 'Origem e destino não podem ser iguais'

def field_has_number(field_value: str, field_name: str, errors_list: list):
    """checks if the field has numeric characters

    Args:
        field_value `str`: value entered in the field
        field_name `str`: field name in form
        errors_list `list`: list to store errors
    """
    if any(char.isdigit() for char in field_value):
        errors_list[field_name] = 'O campo não pode ter caracteres númericos'

