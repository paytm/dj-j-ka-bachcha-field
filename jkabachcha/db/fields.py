import json

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from jkabachcha.forms.widgets import JsonTextWidget


class JsonField(models.TextField):
    description = _("Json Field")
    default_error_messages = {
        'invalid': _('Enter a valid json. Truncating original json'),
    }

    def formfield(self, **kwargs):
        defaults = {}
        defaults.update(**kwargs)
        defaults.update({
            'widget': JsonTextWidget
        })
        return super(JsonField, self).formfield(**defaults)

    def to_python(self, value):
        try:
            json_object = json.loads(value)
        except ValueError as e:
            raise ValidationError(self.error_messages['invalid'], code='invalid')

        return value
