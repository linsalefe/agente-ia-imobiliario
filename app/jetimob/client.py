import httpx
from typing import Dict, List, Optional, Any
from app.config import settings
import logging

logger = logging.getLogger(__name__)


class JetimobClient:
    """Cliente para API do Jetimob"""
    
    BASE_URL = "https://api.jetimob.com"
    
    def __init__(self):
        self.webservice_key = settings.JETIMOB_WEBSERVICE_KEY
        self.public_key = settings.JETIMOB_PUBLIC_KEY
        self.private_key = settings.JETIMOB_PRIVATE_KEY
        self.timeout = 30.0
    
    async def get_imoveis(
        self,
        page: int = 1,
        page_size: int = 100,
        filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Busca imóveis disponíveis
        """
        url = f"{self.BASE_URL}/webservice/{self.webservice_key}/imoveis"
        
        params = {
            "v": 1,
            "page": page,
            "pageSize": page_size
        }
        
        if filters:
            params.update(filters)
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                # Jetimob pode retornar lista ou objeto
                if isinstance(data, list):
                    result = {
                        "total": len(data),
                        "data": data,
                        "page": page,
                        "pageSize": page_size
                    }
                else:
                    result = data
                
                logger.info(f"Buscou {result.get('total', 0)} imóveis do Jetimob")
                return result
                
        except Exception as e:
            logger.error(f"Erro ao buscar imóveis: {e}")
            raise
    
    async def get_imovel_by_codigo(self, codigo: str) -> Optional[Dict[str, Any]]:
        """
        Busca imóvel específico por código
        """
        url = f"{self.BASE_URL}/webservice/{self.webservice_key}/imoveis/codigo/{codigo}"
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, params={"v": 1})
                response.raise_for_status()
                data = response.json()
                
                logger.info(f"Buscou imóvel {codigo} do Jetimob")
                return data
                
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                logger.warning(f"Imóvel {codigo} não encontrado")
                return None
            raise
        except Exception as e:
            logger.error(f"Erro ao buscar imóvel {codigo}: {e}")
            raise
    
    async def create_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria lead no Jetimob
        """
        url = f"{self.BASE_URL}/leads/{self.public_key}"
        
        headers = {
            "Authorization-Key": self.private_key,
            "Content-Type": "multipart/form-data"
        }
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, data=lead_data, headers=headers)
                response.raise_for_status()
                data = response.json()
                
                logger.info(f"Lead criado no Jetimob: {lead_data.get('full_name')}")
                return data
                
        except Exception as e:
            logger.error(f"Erro ao criar lead no Jetimob: {e}")
            raise