#!/bin/bash
set -e

# DB作成
psql -v ON_ERROR_STOP=1 <<-EOSQL
    CREATE DATABASE "$ENVNAME";
EOSQL
