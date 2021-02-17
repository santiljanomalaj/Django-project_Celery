from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_rating(value):
    if value > 5:
        raise ValidationError(
            _('%(value)s should be 5 maximum.'),
            params={'value': value},
        )