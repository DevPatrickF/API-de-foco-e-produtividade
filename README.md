API de Foco e Produtividade
📌 Sobre o Projeto

A API de Foco e Produtividade foi desenvolvida com o objetivo de registrar sessões de foco e gerar diagnósticos inteligentes de produtividade com base nos dados informados pelo usuário.

O sistema permite registrar períodos de trabalho, estudo ou desenvolvimento, armazenando informações como nível de foco, tempo de duração e comentários da sessão. A partir desses registros, a API realiza análises automáticas e fornece feedbacks personalizados sobre a produtividade do usuário.

🚀 Tecnologias Utilizadas
Python 3.12
FastAPI
SQLAlchemy
SQLite
Uvicorn
Pydantic
🧠 Funcionalidades

✅ Registro de sessões de foco
✅ Persistência de dados com SQLite
✅ Diagnóstico inteligente de produtividade
✅ Cálculo de média de foco
✅ Tempo total focado
✅ Categoria mais produtiva
✅ Feedback automático baseado nos dados
✅ Documentação automática com Swagger

🏗 Arquitetura do Projeto

O projeto foi estruturado utilizando separação de responsabilidades para manter o código mais organizado, limpo e escalável.

├── main.py
├── database.py
├── dependencies.py
├── models.py
├── schemas.py
├── foco_routes.py
├── performance_routes.py
└── README.md
📂 Explicação dos Arquivos
main.py
Responsável por iniciar a aplicação FastAPI e registrar os routers.

database.py
Realiza a configuração da conexão com o banco SQLite.

dependencies.py
Gerencia as sessões do banco de dados utilizando dependency injection do FastAPI.

models.py
Define os modelos/tabelas do banco de dados utilizando SQLAlchemy.

schemas.py
Define os schemas de validação utilizando Pydantic.

foco_routes.py
Contém os endpoints relacionados ao registro de sessões de foco.

performance_routes.py
Contém os endpoints responsáveis pelo diagnóstico e análise de produtividade.

🔀 Utilização de Routers

O projeto utiliza APIRouter do FastAPI para separar responsabilidades dos endpoints, facilitando manutenção, organização e escalabilidade da aplicação.

Essa abordagem evita arquivos muito grandes e melhora a estrutura geral do backend.

📡 Endpoints
POST /foco/registro-foco
Responsável por registrar uma nova sessão de foco.

Exemplo de requisição
{
  "nivel_foco": 5,
  "tempo_minutos": 120,
  "comentario": "Desenvolvimento da API utilizando FastAPI",
  "categoria": "programação"
}

GET /performance/diagnostico-produtividade
Retorna um diagnóstico inteligente baseado em todos os registros armazenados.

Exemplo de resposta
{
  "media_foco": 4.5,
  "tempo_total_focado": 320,
  "total_registros": 4,
  "categoria_mais_produtiva": "programação",
  "feedback": "Parabéns, excelente desempenho, você está em estado de FLOW!!"
}

🤖 Feedback Inteligente

A API possui uma lógica automática de feedback baseada na média geral de foco registrada pelo usuário.

Exemplos:

Média baixa → Sugestão para reduzir distrações
Média intermediária → Sugestão de melhoria de consistência
Média alta → Feedback positivo de alta produtividade
🖼 Documentação Swagger

🗄 Banco de Dados SQLite
Estrutura do banco SQLite


▶ Como Executar o Projeto
1. Clonar repositório
git clone https://github.com/DevPatrickF/API-de-foco-e-produtividade.git
2. Criar ambiente virtual
python -m venv venv
3. Ativar ambiente virtual
Windows
venv\Scripts\activate
4. Instalar dependências
pip install -r requirements.txt
5. Executar aplicação
uvicorn main:app --reload

👨‍💻 Autor

Desenvolvido por Patrick utilizando Python, FastAPI e SQLite.
