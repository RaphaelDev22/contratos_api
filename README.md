# 📑 Contratos API

Uma API desenvolvida com Django Rest Framework para gerenciamento de contratos e suas parcelas. Permite cadastro, consulta, filtragem e resumo consolidado dos contratos.

---

## 🚀 Funcionalidades

- ✅ Cadastro de contratos e suas parcelas
- 🔍 Consulta de contratos com filtros (CPF, ID, data, estado)
- 📊 Resumo financeiro por CPF, data ou estado
- 🔐 Validações automáticas via serializers
- 🧪 Testes unitários (em desenvolvimento)

---

## 📦 Tecnologias

- Python 3.11+
- Django 4.x
- Django Rest Framework
- SQLite (padrão)

---
🔗 Endpoints da API
📌 Criar Contrato (com parcelas)
POST /api/contratos/


🔎 Consultar Contratos
GET /api/contratos/

Filtros disponíveis:
id (ex: /api/contratos/?id=1)

cpf (ex: /api/contratos/?cpf=12345678901)

data_emissao (ex: /api/contratos/?data_emissao=2025-06-10)

estado (ex: /api/contratos/?estado=SP)

📊 Resumo dos Contratos
GET /api/resumo/

Filtros:
cpf
data_emissao
estado

🧪 Testes
python manage.py test



## ⚙️ Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/contratos_api.git
cd contratos_api

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Migrações
python manage.py migrate

# Crie um superusuário (opcional)
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver
