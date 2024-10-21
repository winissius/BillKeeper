FROM mongo:latest

# Crie um diretório para os dados do MongoDB dentro do container
VOLUME ["/data/db"]

# Exponha a porta do MongoDB
EXPOSE 27017

# Inicie o serviço do MongoDB na inicialização do container
CMD ["mongod"]