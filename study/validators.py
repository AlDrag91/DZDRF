import re
from rest_framework.serializers import ValidationError
from urllib.parse import urlparse


# def validate_link(value):
#     parsed_url = urlparse(value)
#     if parsed_url.netloc and 'youtube.com' not in parsed_url.netloc:
#         raise ValidationError('Ссылки на сторонние ресурсы, кроме youtube.com, запрещены.')

class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('youtube.com')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Ссылки на сторонние ресурсы, кроме youtube.com, запрещены.')
