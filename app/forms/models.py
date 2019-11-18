from django.db import models
from django.contrib.auth import get_user_model

from app.core import models as core_models


Account = get_user_model()


class JobChangeRequest(core_models.BaseModel):
    SUBMITTED = 'submitted'
    VALIDATED = 'validated'
    RECEIVED = 'received'
    STATUS = (
        (SUBMITTED, _('Submitted')),
        (VALIDATED, _('Validated by manager')),
        (RECEIVED, _('Received by HR')),
    )

    requested_by = models.ForeignKey(Account, on_delete=models.CASCADE)

    employee_name = models.CharField()
    employee_wwid = models.CharField()
    effective_date = models.DateTimeField()
    country = models.CharField()
    is_data_change = models.BooleanField()
    is_employee_change = models.BooleanField()
    """more fields
    .
    .
    .
    .
    """
    status = models.CharField(
       max_length=32,
       choices=STATUS,
       default=SUBMITTED,
    )
