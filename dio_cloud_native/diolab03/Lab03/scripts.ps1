# Build a Docker image
docker build -t my-app:latest .

# Run the container in detached mode (em background)
docker run -d -p 80:80 my-app:latest

# Login to Azure
az login

# Create a resource group
az group create --name my-resource-group --location eastus

# Create Azure Container Registry (ACR)
az acr create --resource-group my-resource-group --name myacrname --sku Basic

# Login to ACR
az acr login --name myacrname

# Tag the image with the ACR path
docker tag my-app:latest myacrname.azurecr.io/my-app:latest

# Push the image to ACR
docker push myacrname.azurecr.io/my-app:latest

# Variables (representação genérica de informações sensíveis)
# containerID = myacrname.azurecr.io/my-app:latest
# registry-username = myacrname
# registry-password = <ACR_PASSWORD>

# Create Container Apps environment
az containerapp env create \
  --name my-container-env \
  --resource-group my-resource-group \
  --location eastus

# Create the Container App
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
