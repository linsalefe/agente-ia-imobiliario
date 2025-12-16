from typing import Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def build_jetimob_lead_data(
    nome: str,
    telefone: str,
    email: str = None,
    imovel_codigo: str = None,
    tipo_contrato: str = None,
    data_visita: str = None,
    horario_visita: str = None,
    mensagem_adicional: str = None
) -> Dict[str, Any]:
    """
    Constrói payload para criar lead no Jetimob
    """
    
    # Dados obrigatórios
    lead_data = {
        "full_name": nome,
        "phone": telefone,
    }
    
    # Email opcional
    if email:
        lead_data["email"] = email
    
    # Código do imóvel
    if imovel_codigo:
        lead_data["property_code"] = imovel_codigo
    
    # Tipo de contrato (1=Venda, 2=Locação, 3=Temporada)
    if tipo_contrato:
        contrato_map = {
            "compra": 1,
            "venda": 1,
            "locacao": 2,
            "locação": 2,
            "temporada": 3
        }
        lead_data["property_contract"] = contrato_map.get(tipo_contrato.lower(), 1)
    
    # Montar mensagem
    mensagem_partes = []
    
    if data_visita and horario_visita:
        mensagem_partes.append(f"📅 Gostaria de agendar visita para {data_visita} às {horario_visita}")
    elif data_visita:
        mensagem_partes.append(f"📅 Gostaria de agendar visita para {data_visita}")
    
    if mensagem_adicional:
        mensagem_partes.append(mensagem_adicional)
    
    if mensagem_partes:
        lead_data["message"] = "\n".join(mensagem_partes)
    
    # Tags
    lead_data["tags"] = "WhatsApp Bot,Qualificado"
    
    # Source
    lead_data["source"] = "WhatsApp Bot"
    
    logger.info(f"Lead data construído para {nome}")
    
    return lead_data