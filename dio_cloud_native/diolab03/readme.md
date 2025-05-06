# 🚀 Lab 03: Deploy de Aplicação Web no Azure Container Apps

## 📘 Visão Geral

Este laboratório prático faz parte da trilha de aprendizado **Cloud Native** da DIO e tem como objetivo demonstrar o processo de implantação de uma aplicação web no **Azure Container Apps**, utilizando ferramentas modernas de desenvolvimento e práticas recomendadas de DevOps.

## 🎯 Objetivos

* Compreender o funcionamento do Azure Container Apps como plataforma de hospedagem de aplicações containerizadas.
* Realizar o deploy de uma aplicação web utilizando o Azure Container Apps.
* Configurar variáveis de ambiente e entender as opções de escalonamento automático.
* Monitorar a aplicação implantada por meio do Azure Monitor e Application Insights.

## 🧰 Tecnologias Utilizadas

* **Azure Container Apps**: Serviço de hospedagem de aplicações containerizadas.
* **Azure CLI**: Ferramenta de linha de comando para gerenciamento de recursos Azure.
* **Docker**: Plataforma para desenvolvimento, envio e execução de aplicações em containers.
* **Git**: Sistema de controle de versão para gerenciamento do código-fonte.
* **Visual Studio Code**: Editor de código-fonte para desenvolvimento e testes locais.

## 📂 Estrutura do Projeto

```
diolab03/
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
* Docker instalado em sua máquina. [Instalação do Docker](https://docs.docker.com/get-docker/)
* Git instalado em sua máquina. [Instalação do Git](https://git-scm.com/downloads)
* Visual Studio Code ou outro editor de código de sua preferência.

## 🚀 Passo a Passo

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/GabsOnRails/DIO.git
   cd DIO/dio_cloud_native/diolab03
   ```

2. **Login no Azure**

   ```bash
   az login
   ```

3. **Criar um Grupo de Recursos**

   ```bash
   az group create --name my-resource-group --location eastus
   ```

4. **Criar um Registro de Container (ACR)**

   ```bash
   az acr create --resource-group my-resource-group --name myacrname --sku Basic
   ```

5. **Login no ACR**

   ```bash
   az acr login --name myacrname
   ```

6. **Build e Tag da Imagem Docker**

   ```bash
   docker build -t my-app:latest .
   docker tag my-app:latest myacrname.azurecr.io/my-app:latest
   ```

7. **Push da Imagem para o ACR**

   ```bash
   docker push myacrname.azurecr.io/my-app:latest
   ```

8. **Criar Ambiente do Container App**

   ```bash
   az containerapp env create --name my-container-env --resource-group my-resource-group --location eastus
   ```

9. **Criar o Container App**

   ```bash
   az containerapp create \
     --name my-container-app \
     --resource-group my-resource-group \
     --image myacrname.azurecr.io/my-app:latest \
     --environment my-container-env \
     --target-port 80 \
     --ingress external \
     --registry-username myacrname \
     --registry-password <ACR_PASSWORD> \
     --registry-server myacrname.azurecr.io
   ```

   > **Nota:** Substitua `<ACR_PASSWORD>` pela senha do seu Azure Container Registry. Para obter a senha, utilize o comando:

   ```bash
   az acr credential show --name myacrname --query "passwords[0].value"
   ```

10. **Acessar a Aplicação**

    Após a implantação, acesse a aplicação pelo navegador utilizando a URL fornecida pelo Azure Container Apps.

## 📈 Monitoramento e Logs

* Utilize o Azure Monitor e o Application Insights para acompanhar o desempenho e os logs da aplicação.
* Configure alertas e métricas personalizadas conforme necessário.

## 📚 Recursos Adicionais

* [Documentação do Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)
* [Tutorial de Implantação no Azure Container Apps](https://learn.microsoft.com/azure/container-apps/quickstart-deploy-container)

