from django.db import models

from app.core import models as core_models


class DocumentType(core_models.BaseModel):
    pass


class DocumentPurpose(core_models.BaseModel):
    pass


class DocumentRequest(core_models.BaseModel):
    type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL)
    purpose = models.ForeignKey(DocumentPurpose, on_delete=models.SET_NULL)


class File(core_models.BaseModel):
    upload = models.FileField(upload_to='uploads/')
