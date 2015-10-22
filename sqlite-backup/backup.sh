#!/bin/bash

BASEDIR=$(dirname ${0})
BASEDIR=$(readlink -f "${BASEDIR}")

BACKUP_DIR=${BASEDIR}/dump

DB_SOURCE_PATH=..
DB_SOURCE_NAME=blog.db

echo "Backup: ${DB_SOURCE_NAME} ..."
cp ${DB_SOURCE_PATH}/${DB_SOURCE_NAME} ${BACKUP_DIR}/${DB_SOURCE_NAME}_`date +%Y-%m-%d"_"%H_%M_%S`
echo "Backup: Done!"

