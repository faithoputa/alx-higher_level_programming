#!/bin/bash

# Create the SQL query
echo "SELECT SCHEMA_NAME FROM Information_schema.SCHEMATA WHERE SCHEMA_NAME NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys');" > list_databases.sql

# Run the SQL query using the MySQL command and output the results
mysql -h localhost -uroot -p < list_databases.sql

