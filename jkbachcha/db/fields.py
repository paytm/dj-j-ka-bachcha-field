from django.db import models
from django.utils.translation import ugettext_lazy as _

from jkbachcha.forms.widgets import JsonTextWidget


class JsonField(models.TextField):
    description = _("Json Field")

    def formfield(self, **kwargs):
        defaults = {}
        defaults.update(**kwargs)
        defaults.update({
            'widget': JsonTextWidget
        })
        return super(JsonField, self).formfield(**defaults)
