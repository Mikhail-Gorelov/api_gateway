from dataclasses import dataclass
from typing import Optional


@dataclass
class RemoteUser:
    id: int
    full_name: str
    email: Optional[str] = None
    phone_number: Optional[str] = None
