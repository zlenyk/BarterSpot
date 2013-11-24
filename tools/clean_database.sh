#!/bin/sh

echo "Make sure that user barterman has privileges to create and drop databases"
echo ""
echo "drop database barterdb;" >> tmp.sql
echo "create database barterdb;" >> tmp.sql

psql -U barterman < tmp.sql

rm tmp.sql
