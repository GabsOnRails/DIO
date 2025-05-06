# 🚀 Lab 02: Deploy de Aplicação Web no Azure App Service

## 📘 Visão Geral

Este laboratório prático faz parte da trilha de aprendizado **Cloud Native** da DIO e tem como objetivo demonstrar o processo de implantação de uma aplicação web no **Azure App Service**, utilizando ferramentas modernas de desenvolvimento e práticas recomendadas de DevOps.

## 🎯 Objetivos

* Compreender o funcionamento do Azure App Service como plataforma de hospedagem de aplicações web.
* Realizar o deploy de uma aplicação web utilizando o Azure App Service.
* Configurar variáveis de ambiente e entender as opções de escalonamento automático.
* Monitorar a aplicação implantada por meio do Azure Monitor e Application Insights.

## 🧰 Tecnologias Utilizadas

* **Azure App Service**: Serviço de hospedagem de aplicações web.
* **Azure CLI**: Ferramenta de linha de comando para gerenciamento de recursos Azure.
* **Git**: Sistema de controle de versão para gerenciamento do código-fonte.
* **Visual Studio Code**: Editor de código-fonte para desenvolvimento e testes locais.

## 📂 Estrutura do Projeto

```
diolab02/
├── app/
│   ├── index.html
│   └── styles.css
├── scripts/
│   └── deploy.sh
└── README.md
```

* `app/`: Contém os arquivos da aplicação web.
* `scripts/`: Contém scripts de automação para implantação no Azure.
* `README.md`: Documentação do laboratório.

## 🛠️ Pré-requisitos

Antes de iniciar, certifique-se de ter:

* Uma conta ativa no [Microsoft Azure](https://azure.microsoft.com/).
* Azure CLI instalada e configurada. [Instalação da Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)
* Git instalado em sua máquina. [Instalação do Git](https://git-scm.com/downloads)
* Visual Studio Code ou outro editor de código de sua preferência.

## 🚀 Passo a Passo

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/GabsOnRails/DIO.git
   cd DIO/dio_cloud_native/diolab02
   ```

2. **Login no Azure**

   ```bash
   az login
   ```

3. **Criar um Grupo de Recursos**

   ```bash
   az group create --name diolab02-rg --location eastus
   ```

4. **Criar um Plano de Serviço do App**

   ```bash
   az appservice plan create --name diolab02-plan --resource-group diolab02-rg --sku FREE
   ```

5. **Criar o App Web**

   ```bash
   az webapp create --name diolab02-app --resource-group diolab02-rg --plan diolab02-plan
   ```

6. **Implantar a Aplicação**

   Utilize o script de deploy disponível em `scripts/deploy.sh` ou implante manualmente os arquivos da pasta `app/` para o Azure App Service.

7. **Acessar a Aplicação**

   Após a implantação, acesse a aplicação pelo navegador utilizando a URL fornecida pelo Azure App Service.

## 📈 Monitoramento e Logs

* Utilize o Azure Monitor e o Application Insights para acompanhar o desempenho e os logs da aplicação.
* Configure alertas e métricas personalizadas conforme necessário.

## 📚 Recursos Adicionais

* [Documentação do Azure App Service](https://learn.microsoft.com/azure/app-service/)
* [Tutorial de Implantação no Azure App Service](https://learn.microsoft.com/azure/app-service/quickstart-html)
