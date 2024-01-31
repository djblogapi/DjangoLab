
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


MAX_FILE_SIZE = 10  # MB

ACCEPTED_IMAGE_FORMATS = ['jpeg', 'jpg', 'png']

@deconstructible
class MaxValueFileSizeValidator(BaseValidator):
    message = _('The maximum file size that can be uploaded is %(limit_value)s MB.')
    code = 'max_value'

    def compare(self, a, b):
        return a > b*1024*1024

    def clean(self, x):
        return x.size

