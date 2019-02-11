Для простого разворачивания приложения на новом сервере необходимо установить docker, docker-compose: 

sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common
	
sudo curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
   
sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose

создать директорию с БД 

sudo mkdir /var/db

Поместить БД в данную директорию

Скопировать в рабочую директорию актуальную версию docker-compose.yml для приложения

Запустить 

docker-compose up -d   