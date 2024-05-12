from django.core.exceptions import ValidationError


def validate_phone_number(phone_number: str) -> None:
    """This function validates phone number"""
    if not len(phone_number) != 17 or not phone_number.startswith('+998') or phone_number[1:].isdigit():
        raise ValidationError('Phone number is not valid')