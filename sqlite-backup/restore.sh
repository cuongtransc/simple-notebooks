#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./restore.sh file_backup"
    exit 1
fi

FILE_BACKUP=$1
FILE_BACKUP=$(readlink -f "${FILE_BACKUP}")

DB_SOURCE_PATH=..
DB_SOURCE_NAME=blog.db

echo "Backup: ${DB_SOURCE_NAME} ..."
cp ${FILE_BACKUP} ${DB_SOURCE_PATH}/${DB_SOURCE_NAME}
echo "Backup: Done!"

