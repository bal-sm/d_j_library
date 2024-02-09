from django.db import models
from django.utils.translation import gettext_lazy as _


class DJangoOrderMixin(models.Model):
    d_j_order = models.PositiveBigIntegerField(
        editable=False,
        verbose_name=_("ke-"),
    )

    class Meta:
        abstract = True
        ordering = ["d_j_order"]


class JSONDetailsMixin(models.Model):
    """
    A mixin for models that have `JSONField` `details`.
    """

    details = models.JSONField(
        null=False,
        blank=True,
        default=dict,
        verbose_name=_("detil-detil lainnya"),
    )

    class Meta:
        abstract = True
