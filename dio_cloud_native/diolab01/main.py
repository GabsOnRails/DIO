# importando as bibliotecas necessárias
import streamlit as st
import pyodbc
import os
import pymssql
import uuid
import json
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
load_dotenv ()  # Carregar variáveis de ambiente do arquivo .env

# Pegando as variáveis de ambiente de Blob Storage
blobConnectionString = os.getenv("BLOB_CONNECTION_STRING")
blobContainerName = os.getenv("BLOB_CONTAINER_NAME")
blobAccountName = os.getenv("BLOB_ACCOUNT_NAME")

# Pega as informações seguras
server = st.secrets["sql_server"]["server"]
database = st.secrets["sql_server"]["database"]
username = st.secrets["sql_server"]["username"]
password = st.secrets["sql_server"]["password"]

# Faz a conexão
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
)

# Testar conexão
cursor = conn.cursor()
cursor.execute("SELECT @@VERSION")
row = cursor.fetchone()
st.success(f"Conectado com sucesso! Versão do SQL Server: {row[0]}")

# Essa não funciona comigo
# Pegando as variáveis de ambiente de SQL Server
# SQL_SERVER = os.getenv("SQL_SERVER_NAME")
# SQL_DATABASE = os.getenv("SQL_DATABASE") 
# SQL_USERNAME = os.getenv("SQL_USERNAME")
# SQL_PASSWORD = os.getenv("SQL_PASSWORD")

# Configurando tela de streamlit
st.title("Cadastro de Produtos")
product_name = st.text_input("Nome do Produto")
product_description = st.text_area("Descrição do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_image = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

# Salvar imagem no Blob Storage
if product_image is not None:
    # Gerar um nome único para a imagem
    image_name = str(uuid.uuid4()) + os.path.splitext(product_image.name)[1]
    
    # Conectar ao Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    blob_client = blob_service_client.get_blob_client(container=blobContainerName, blob=image_name)
    
    # Fazer upload da imagem
    blob_client.upload_blob(product_image, overwrite=True)
    
    # Obter a URL da imagem
    image_url = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{image_name}"


# Botão para cadastrar o produto
if st.button("Cadastrar Produto"):
    # Conectar ao SQL Server
    conn = pymssql.connect(server=server, user=username, password=password, database=database)
    cursor = conn.cursor()
    
    # Inserir o produto no banco de dados
    cursor.execute("INSERT INTO Produtos (nome, descricao, preco, imagem_url) VALUES (%s, %s, %s, %s)", 
                   (product_name, product_description, product_price, image_url))
    
    # Salvar as alterações e fechar a conexão
    conn.commit()
    cursor.close()
    conn.close()
    
    st.success("Produto cadastrado com sucesso!")

# Exibir produtos cadastrados
st.subheader("Produtos Cadastrados")
conn = pymssql.connect(server=server, user=username, password=password, database=database)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Produtos")
products = cursor.fetchall()
conn.close()
for product in products:
    st.image(product[4], width=100)  # Exibir imagem
    st.write(f"**Nome:** {product[1]}")
    st.write(f"**Descrição:** {product[2]}")
    st.write(f"**Preço:** R$ {product[3]:.2f}")
    st.write("---")

    
