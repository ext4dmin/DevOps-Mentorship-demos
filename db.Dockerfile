FROM postgres:14
COPY ./create-multiple-databases.sh /docker-entrypoint-initdb.d/