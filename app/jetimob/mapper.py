from typing import Dict, Any, Optional


def format_imovel_info(imovel: Dict[str, Any]) -> str:
    """
    Formata informações do imóvel de forma legível
    """
    # Dados básicos
    codigo = imovel.get("codigo", "N/A")
    contrato = imovel.get("contrato", "N/A")
    tipo = imovel.get("tipo", "N/A")
    subtipo = imovel.get("subtipo", "N/A")
    
    # Localização
    cidade = imovel.get("endereco_cidade", "N/A")
    bairro = imovel.get("endereco_bairro", "N/A")
    logradouro = imovel.get("endereco_logradouro", "")
    numero = imovel.get("endereco_numero", "")
    
    # Características
    dormitorios = imovel.get("dormitorios", 0)
    suites = imovel.get("suites", 0)
    banheiros = imovel.get("banheiros", 0)
    garagens = imovel.get("garagens", 0)
    area_total = imovel.get("area_total") or imovel.get("area_privativa")
    
    # Valores
    valor_venda = imovel.get("valor_venda")
    valor_locacao = imovel.get("valor_locacao")
    valor_condominio = imovel.get("valor_condominio")
    valor_iptu = imovel.get("valor_iptu")
    
    # Montar texto
    texto = f"🏠 *Código:* {codigo}\n"
    texto += f"📍 *Localização:* {bairro}, {cidade}\n"
    
    if logradouro and numero:
        texto += f"   {logradouro}, {numero}\n"
    
    texto += f"🏗️ *Tipo:* {tipo} - {subtipo}\n"
    texto += f"🛏️ *Quartos:* {dormitorios}"
    
    if suites > 0:
        texto += f" ({suites} suíte{'s' if suites > 1 else ''})"
    texto += f"\n🚿 *Banheiros:* {banheiros}\n"
    texto += f"🚗 *Garagens:* {garagens}\n"
    
    if area_total:
        texto += f"📐 *Área:* {area_total}m²\n"
    
    # Valores
    if contrato in ["Compra", "Venda"] and valor_venda:
        texto += f"💰 *Valor de Venda:* R$ {format_currency(valor_venda)}\n"
    
    if contrato == "Locação" and valor_locacao:
        texto += f"💰 *Valor de Locação:* R$ {format_currency(valor_locacao)}/mês\n"
        
        if valor_condominio:
            texto += f"🏢 *Condomínio:* R$ {format_currency(valor_condominio)}\n"
        
        if valor_iptu:
            texto += f"📋 *IPTU:* R$ {format_currency(valor_iptu)}\n"
    
    return texto


def format_currency(value: float) -> str:
    """
    Formata valor monetário
    """
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def extract_imovel_summary(imovel: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extrai resumo do imóvel para contexto
    """
    return {
        "codigo": imovel.get("codigo"),
        "tipo": f"{imovel.get('tipo')} - {imovel.get('subtipo')}",
        "bairro": imovel.get("endereco_bairro"),
        "cidade": imovel.get("endereco_cidade"),
        "dormitorios": imovel.get("dormitorios", 0),
        "valor_venda": imovel.get("valor_venda"),
        "valor_locacao": imovel.get("valor_locacao"),
        "contrato": imovel.get("contrato")
    }