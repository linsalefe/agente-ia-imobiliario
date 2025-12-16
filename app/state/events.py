from enum import Enum


class LeadEvent(str, Enum):
    """Eventos que causam transições de estado"""
    INICIO_CONVERSA = "INICIO_CONVERSA"
    INTERESSE_CONFIRMADO = "INTERESSE_CONFIRMADO"
    VISITA_AGENDADA = "VISITA_AGENDADA"
    LEAD_PERDIDO = "LEAD_PERDIDO"
    RETOMAR_CONVERSA = "RETOMAR_CONVERSA"