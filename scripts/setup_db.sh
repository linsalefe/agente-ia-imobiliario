#!/bin/bash

# Criar banco de dados
psql postgres -c "CREATE DATABASE agente_imoveis;"

# Executar schema
psql agente_imoveis -f db/schema.sql

echo "✅ Banco de dados criado com sucesso!"