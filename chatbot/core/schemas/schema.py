from fastapi import Form
import pydantic as _pdt

# private class
class UserConvo(_pdt.BaseModel):
    message: str

    @classmethod
    def as_form(
        cls,
        message: str = Form(...)
    ):
        return cls(
            message = message
        )

