# Deploy Econômico no Azure com Docker, ACR, AKS e ACI

Este guia fornece instruções para criar e usar ambientes de containers no Azure de forma econômica utilizando **Azure Kubernetes Service (AKS)** ou **Azure Container Instances (ACI)**.

---

## Seção 1: AKS com Baixo Custo

### Passos para Criar o AKS:

1. **Definir Variáveis**:
    ```bash
    RG="grupo-teste"
    LOCATION="brazilsouth"
    ACR_NAME="acrteste123"         # Nome globalmente único
    AKS_NAME="aksteste"
    NODE_SIZE="Standard_B2s"       # VM mais econômica
    NODE_COUNT=1
    ```

2. **Criar Resource Group**:
    ```bash
    az group create --name $RG --location $LOCATION
    ```

3. **Criar Azure Container Registry (ACR) com SKU Basic**:
    ```bash
    az acr create \
      --resource-group $RG \
      --name $ACR_NAME \
      --sku Basic \
      --admin-enabled true \
      --location $LOCATION
    ```

4. **Criar o AKS com um único nó e VM barata**:
    ```bash
    az aks create \
      --resource-group $RG \
      --name $AKS_NAME \
      --node-count $NODE_COUNT \
      --node-vm-size $NODE_SIZE \
      --generate-ssh-keys \
      --attach-acr $ACR_NAME \
      --enable-managed-identity
    ```

5. **Acessar o Cluster AKS**:
    ```bash
    az aks get-credentials --resource-group $RG --name $AKS_NAME
    ```

6. **Testar se está tudo funcionando**:
    ```bash
    kubectl get nodes
    ```

---

## Seção 2: Usando Azure Container Instance (ACI)

### Passos para Criar um ACI:

1. **Definir Variáveis**:
    ```bash
    RG_NAME="rg-aci-app"
    LOCATION="eastus"
    ACI_NAME="my-aci-app"
    ACR_NAME="meuacr123"  # Nome único
    ACR_LOGIN_SERVER="$ACR_NAME.azurecr.io"
    ACR_IMAGE="$ACR_NAME.azurecr.io/minha-imagem:latest"
    ACI_DNS_LABEL="meuaci$RANDOM"
    STORAGE_ACCOUNT="minhastorageaci"
    FILE_SHARE_NAME="acishare"
    STORAGE_MOUNT_PATH="/mnt/storage"
    ACI_ENV_VARS="APP_MODE=production DATABASE_URL=mysql://user:pass@host/db"
    ```

2. **Criar Resource Group**:
    ```bash
    az group create --name $RG_NAME --location $LOCATION
    ```

3. **Criar o ACR**:
    ```bash
    az acr create --resource-group $RG_NAME --name $ACR_NAME --sku Basic --admin-enabled true
    ```

4. **Fazer Login no ACR**:
    ```bash
    az acr login --name $ACR_NAME
    ```

5. **Obter Credenciais do ACR**:
    ```bash
    ACR_USERNAME=$(az acr credential show --name $ACR_NAME --query "username" --output tsv)
    ACR_PASSWORD=$(az acr credential show --name $ACR_NAME --query "passwords[0].value" --output tsv)
    ```

6. **Criar Storage Account (opcional, para volume persistente)**:
    ```bash
    az storage account create --name $STORAGE_ACCOUNT --resource-group $RG_NAME --location $LOCATION --sku Standard_LRS
    STORAGE_KEY=$(az storage account keys list --resource-group $RG_NAME --account-name $STORAGE_ACCOUNT --query "[0].value" --output tsv)
    ```

7. **Criar File Share**:
    ```bash
    az storage share create --name $FILE_SHARE_NAME --account-name $STORAGE_ACCOUNT --account-key $STORAGE_KEY
    ```

8. **Criar o ACI**:
    ```bash
    az container create \
      --resource-group $RG_NAME \
      --name $ACI_NAME \
      --image $ACR_IMAGE \
      --dns-name-label $ACI_DNS_LABEL \
      --ports 80 443 \
      --environment-variables $ACI_ENV_VARS \
      --azure-file-volume-account-name $STORAGE_ACCOUNT \
      --azure-file-volume-account-key $STORAGE_KEY \
      --azure-file-volume-share-name $FILE_SHARE_NAME \
      --azure-file-volume-mount-path $STORAGE_MOUNT_PATH \
      --registry-login-server $ACR_LOGIN_SERVER \
      --registry-username $ACR_USERNAME \
      --registry-password $ACR_PASSWORD
    ```

9. **Obter IP público ou DNS do container**:
    ```bash
    echo "Acesse a aplicação em: http://$(az container show --resource-group $RG_NAME --name $ACI_NAME --query ipAddress.fqdn --output tsv)"
    ```

---

## Seção 3: Trabalhando com Docker + Azure CLI

### Passos para Criar, Testar e Enviar Imagens:

1. **Criar Imagem Docker**:
    ```bash
    docker build -t nome/imagem:latest .
    ```

2. **Verificar Imagens Criadas**:
    ```bash
    docker images
    ```

3. **Rodar o Container Docker**:
    ```bash
    docker run -d -p 80:80 nome/imagem:latest
    ```

4. **Verificar Containers em Execução**:
    ```bash
    docker ps
    ```

5. **Parar o Container**:
    ```bash
    docker stop <container_id>
    ```

---

## Seção 4: Publicar Imagens no ACR

### Passos para Subir Imagens ao ACR:

1. **Login na Azure**:
    ```bash
    az login
    ```

2. **Caso necessário, logar com Tenant**:
    ```bash
    az login --tenant <seu_tenant_id>
    ```

3. **Login no ACR**:
    ```bash
    az acr login --name nome_do_acr
    ```

4. **Taggear a Imagem Docker**:
    ```bash
    docker tag nome/imagem:latest nome_do_acr.azurecr.io/nome_imagem:latest
    ```

5. **Enviar a Imagem para o ACR**:
    ```bash
    docker push nome_do_acr.azurecr.io/nome_imagem:latest
    ```

6. **Verificar as Imagens no ACR**:
    ```bash
    az acr repository list --name nome_do_acr --output table
    ```

---

## Seção 5: Ativar Caminhos Longos no Windows (Se necessário)

1. **Abrir Editor de Políticas de Grupo Local**:
    - Pressione `Win + R` e digite `gpedit.msc`.
  
2. **Navegar até o Caminho**:
    - Configuração do Computador > Modelos Administrativos > Sistema > Sistema de Arquivos.

3. **Ativar Caminhos Longos**:
    - Ative a opção **"Ativar caminhos de arquivo Win32 longos"**.

4. **Reiniciar o Computador**:
    - Após a ativação, reinicie o computador para aplicar as alterações.

---
