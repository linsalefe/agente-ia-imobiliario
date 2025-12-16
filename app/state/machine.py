from typing import Dict, Set, Tuple
from app.state.schema import LeadState, LeadContext
from app.state.events import LeadEvent


# Transições permitidas: (estado_atual, evento) -> novo_estado
TRANSITIONS: Dict[Tuple[LeadState, LeadEvent], LeadState] = {
    # Do INICIAL
    (LeadState.INICIAL, LeadEvent.INICIO_CONVERSA): LeadState.QUALIFICANDO,
    
    # Do QUALIFICANDO
    (LeadState.QUALIFICANDO, LeadEvent.INTERESSE_CONFIRMADO): LeadState.QUALIFICANDO,
    (LeadState.QUALIFICANDO, LeadEvent.VISITA_AGENDADA): LeadState.AGENDADO,
    (LeadState.QUALIFICANDO, LeadEvent.LEAD_PERDIDO): LeadState.PERDIDO,
    
    # Do AGENDADO
    (LeadState.AGENDADO, LeadEvent.RETOMAR_CONVERSA): LeadState.QUALIFICANDO,
    
    # Do PERDIDO
    (LeadState.PERDIDO, LeadEvent.RETOMAR_CONVERSA): LeadState.QUALIFICANDO,
}


def is_transition_allowed(current_state: LeadState, event: LeadEvent) -> bool:
    """
    Verifica se a transição é permitida
    """
    return (current_state, event) in TRANSITIONS


def get_next_state(current_state: LeadState, event: LeadEvent) -> LeadState:
    """
    Retorna o próximo estado após aplicar o evento
    """
    if not is_transition_allowed(current_state, event):
        raise ValueError(
            f"Transição inválida: {current_state} -> {event}"
        )
    
    return TRANSITIONS[(current_state, event)]


def transition(context: LeadContext, event: LeadEvent) -> LeadContext:
    """
    Aplica transição de estado no contexto do lead
    """
    new_state = get_next_state(context.state, event)
    context.state = new_state
    
    return context