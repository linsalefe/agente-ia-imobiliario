-- Database: agente_imoveis

-- Tabela de leads
CREATE TABLE IF NOT EXISTS leads (
    id SERIAL PRIMARY KEY,
    phone VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(255),
    email VARCHAR(255),
    
    -- Interesse
    imovel_interesse VARCHAR(50),
    tipo_contrato VARCHAR(20),
    bairro_preferido VARCHAR(100),
    preco_max DECIMAL(12, 2),
    
    -- Agendamento
    data_visita_preferida DATE,
    horario_visita_preferido VARCHAR(10),
    
    -- Estado e integração
    current_state VARCHAR(50) NOT NULL DEFAULT 'INICIAL',
    jetimob_lead_id INTEGER,
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de mensagens
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    lead_id INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    role VARCHAR(20) NOT NULL, -- 'user' ou 'assistant'
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de follow-ups
CREATE TABLE IF NOT EXISTS followups (
    id SERIAL PRIMARY KEY,
    lead_id INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    type VARCHAR(10) NOT NULL, -- 'D1' ou 'D3'
    scheduled_for TIMESTAMP NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending', -- 'pending', 'sent', 'cancelled'
    executed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_leads_phone ON leads(phone);
CREATE INDEX idx_leads_state ON leads(current_state);
CREATE INDEX idx_messages_lead ON messages(lead_id);
CREATE INDEX idx_followups_lead ON followups(lead_id);
CREATE INDEX idx_followups_status ON followups(status);