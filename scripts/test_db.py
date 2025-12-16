import sys
sys.path.append('.')

from app.database import test_connection
from app.state.schema import LeadState, LeadContext
from app.state.events import LeadEvent
from app.state.machine import transition

print("=== Testando Database ===")
test_connection()

print("\n=== Testando State Machine ===")

# Criar contexto
context = LeadContext(
    lead_id=1,
    phone="5583999999999",
    state=LeadState.INICIAL
)
print(f"Estado inicial: {context.state}")

# Transição 1: INICIAL -> QUALIFICANDO
context = transition(context, LeadEvent.INICIO_CONVERSA)
print(f"Após INICIO_CONVERSA: {context.state}")

# Transição 2: QUALIFICANDO -> AGENDADO
context = transition(context, LeadEvent.VISITA_AGENDADA)
print(f"Após VISITA_AGENDADA: {context.state}")

print("\n✅ State Machine funcionando!")