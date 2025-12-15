# 🏠 Agente WhatsApp Imobiliário

Bot de qualificação de leads imobiliários integrado ao Jetimob via WhatsApp.

## 🚀 Stack

- Python 3.11
- FastAPI
- PostgreSQL
- Redis
- Evolution API (WhatsApp)
- ChatGPT (OpenAI)
- Jetimob API

## 📋 Setup Local
```bash
# Criar ambiente virtual
python3.11 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar .env
cp .env.example .env
# Editar .env com suas credenciais

# Rodar aplicação
uvicorn app.main:app --reload
```

## 🔗 Endpoints

- `GET /` - Informações da API
- `GET /health` - Health check
- `GET /docs` - Documentação Swagger

## 📦 Estrutura
```
agente-ia-imobiliario/
├── app/
│   ├── flows/          # Fluxos de conversa
│   ├── state/          # State machine
│   ├── jetimob/        # Integração Jetimob
│   ├── whatsapp/       # Integração WhatsApp
│   ├── kb/             # Base de conhecimento
│   ├── llm/            # ChatGPT
│   ├── sched/          # Agendamento e workers
│   ├── security/       # Segurança
│   └── observability/  # Logs e métricas
├── db/                 # Scripts SQL
├── kb/                 # Arquivos de conhecimento
├── docs/               # Documentação
└── scripts/            # Scripts utilitários
```

## 🔧 Servidor de Produção

**Evolution API:** http://44.201.147.174:8080
**Instância:** Agente-la-imobiliário