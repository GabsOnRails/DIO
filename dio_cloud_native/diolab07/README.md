# 📦 Projeto App Locadora - Diolab07

Este repositório contém uma solução completa para uma aplicação de locadora, incluindo frontend, backend em Node.js e funções serverless em .NET para processamento de aluguel e pagamento.

## 📁 Estrutura do Projeto

```
diolab07/
├── app-locadora/
│   ├── backend/         # API Node.js (Express)
│   │   ├── .env
│   │   ├── Dockerfile
│   │   ├── index.js
│   │   └── package.json
│   └── frontend/        # (Frontend da aplicação)
├── app-locadora-v1/     # Versão alternativa/simplificada do backend
│   ├── dockerfile
│   ├── index.js
│   └── package.json
└── functions/
    └── fnRentProcess/   # Funções serverless em .NET
        ├── fnPaymanet/      # Função de pagamento
        │   ├── fnPaymanet.csproj
        │   ├── Function1.cs
        │   ├── PaymanetModel.cs
        │   └── Program.cs
        └── fnRentProcess/   # Função de processamento de aluguel
            ├── fnRentProcess.csproj
            ├── Function1.cs
            └── Program.cs
```

## 🚀 Tecnologias Utilizadas

- **Node.js** (Express) — Backend da aplicação
- **.NET (C#)** — Funções serverless (Azure Functions)
- **Docker** — Containerização dos serviços
- **JavaScript** — Lógica do frontend e backend

## ⚙️ Como Executar

### Backend Node.js

```bash
cd diolab07/app-locadora/backend
npm install
npm start
```

### Funções Serverless (.NET)

Abra a solução `fnRentProcess.sln` no Visual Studio ou utilize o Azure Functions Core Tools:

```bash
cd diolab07/functions/fnRentProcess/fnRentProcess
func start
```

Faça o mesmo para `fnPaymanet` se necessário.

### Docker

Para rodar o backend via Docker:

```bash
cd diolab07/app-locadora/backend
docker build -t app-locadora-backend .
docker run -p 3000:3000 --env-file .env app-locadora-backend
```

## 📄 Observações

- Configure as variáveis de ambiente no arquivo `.env` conforme necessário.
- O frontend pode ser desenvolvido na pasta `frontend/` (verifique se há instruções específicas).
- As funções serverless podem ser publicadas no Azure Functions.

---

Desenvolvido para fins educacionais no contexto do