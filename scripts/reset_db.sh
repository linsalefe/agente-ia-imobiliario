#!/bin/bash

echo "⚠️  Isso vai apagar todos os dados!"
read -p "Tem certeza? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Operação cancelada."
    exit 0
fi

# Dropar banco
psql postgres -c "DROP DATABASE IF EXISTS agente_imoveis;"

# Recriar banco
psql postgres -c "CREATE DATABASE agente_imoveis;"

# Executar schema
psql agente_imoveis -f db/schema.sql

echo "✅ Banco resetado com sucesso!"