from enum import Enum
from typing import Optional, Dict, Any
from datetime import datetime


class LeadState(str, Enum):
    """Estados possíveis do lead"""
    INICIAL = "INICIAL"
    QUALIFICANDO = "QUALIFICANDO"
    AGENDADO = "AGENDADO"
    PERDIDO = "PERDIDO"


class LeadContext:
    """Contexto do lead com metadados"""
    
    def __init__(
        self,
        lead_id: int,
        phone: str,
        state: LeadState = LeadState.INICIAL,
        name: Optional[str] = None,
        email: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.lead_id = lead_id
        self.phone = phone
        self.state = state
        self.name = name
        self.email = email
        self.metadata = metadata or {}
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "lead_id": self.lead_id,
            "phone": self.phone,
            "state": self.state.value,
            "name": self.name,
            "email": self.email,
            "metadata": self.metadata,
            "updated_at": self.updated_at.isoformat()
        }