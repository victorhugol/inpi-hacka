# Aplicação criada para do Hacka do INPI

## Pre requisitos

-   Ubuntu
-   Docker
-   Terminal
-   Python3

## Primeiros Passos

## Container

1 - docker run --name inpi -e MYSQL_ROOT_PASSWORD=minha-senha -d -p 3306:3306 mysql/mysql-server:latest


## Aplicação

1 - Instalar o venv
```bash
$ sudo apt install python3-venv
```
2 - Criar um ambiente virtual na raiz do projeto
```bash
$ pip3 install -r requirements.txt
```
4 - criar um arquivo .env para armazenar as variaveis de ambiente seguintes:
```
DB_URL=localhost:3306

```

3 - rodar setup
```bash
$ python3 setup.py run
```