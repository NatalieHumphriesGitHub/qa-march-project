FROM mysql:5.7
env MYSQL_DATABASE=plant-db
env MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
COPY ./CreateTable.sql docker-entrypoint-initdb.d/CreateTable.sql