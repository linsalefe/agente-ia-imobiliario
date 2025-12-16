import sys
import asyncio
sys.path.append('.')

from app.jetimob.client import JetimobClient
from app.jetimob.mapper import format_imovel_info, extract_imovel_summary

async def main():
    print("=== Testando Jetimob API ===\n")
    
    client = JetimobClient()
    
    # Teste 1: Buscar imóveis
    print("1. Buscando primeiros 5 imóveis...")
    try:
        result = await client.get_imoveis(page=1, page_size=5)
        total = result.get("total", 0)
        imoveis = result.get("data", [])
        
        print(f"✅ Total de imóveis: {total}")
        print(f"✅ Retornados: {len(imoveis)}\n")
        
        if imoveis:
            # Mostrar primeiro imóvel formatado
            primeiro = imoveis[0]
            print("Exemplo de imóvel formatado:")
            print("-" * 50)
            print(format_imovel_info(primeiro))
            print("-" * 50)
            
            # Teste 2: Buscar por código
            codigo = primeiro.get("codigo")
            if codigo:
                print(f"\n2. Buscando imóvel por código: {codigo}")
                imovel = await client.get_imovel_by_codigo(codigo)
                if imovel:
                    print(f"✅ Imóvel {codigo} encontrado!")
                    resumo = extract_imovel_summary(imovel)
                    print(f"Resumo: {resumo}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print("\n✅ Testes concluídos!")

if __name__ == "__main__":
    asyncio.run(main())