#!/bin/bash
DB_NAME=`echo $DATABASE_URL | awk -F / '{ print $(NF) }'`
PROTOCOL="postgres://"
DB_URL=`echo $DATABASE_URL | awk -F / '{ print $(NF-1) }'`
if [ "$( psql "$PROTOCOL$DB_URL" -tAc "SELECT 1 FROM pg_database WHERE datname='DB_NAME'" )" = '1' ]
then
    echo "Database already exists"
else
    echo "Database does not exist. Creating now.."
    psql "$PROTOCOL$DB_URL" -tAc "CREATE DATABASE \"$DB_NAME\";"
fi
