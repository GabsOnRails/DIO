az extension add --name containerapp --upgrade

az provider register --namespace Microsoft.App

az provider register --namespace Microsoft.OperationalInsights

# Defina as variáveis para o seu ambiente
# Substitua os valores abaixo pelos seus próprios
myRG = nome_do_seu_grupo_de_recursos
location = sua_localizacao # Exemplo: "eastus"
myAppContainerEnv = nome_do_seu_ambiente_de_contêiner # Exemplo: "myContainerAppEnv"

# Criar o grupo de recursos
az group create --name $myRG --location $location

# Criar o ambiente de contêiner
# Essas variáveis devem ser definidas antes de executar o comando
# Substitua os valores abaixo pelos seus próprios
az containerapp env create --name $myAppContainerEnv --resource-group $myRG --location $location   

az containerapp create --name my-container-app ` # podemos usar \ para quebrar linhas
--resource-group $myRG `
--location $location `
--environment $myAppContainerEnv `
--image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest `
--target-port 80 `
--ingress external `
--query properties.configuration.ingress.fqdn