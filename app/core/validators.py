from django.apps import apps
from django.core.exceptions import ValidationError


def validate_model(value):
    if value:
        try:
            apps.get_model(value)
        except ValueError:
            raise ValidationError('Model name is incorrect')
        except LookupError as error:
            raise ValidationError(error)
