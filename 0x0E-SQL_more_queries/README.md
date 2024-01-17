SQL, or Structured Query Language, is a programming language used to manage and manipulate relational databases. Here are summaries of some common SQL queries:

SELECT: Extracts data from a database. The data returned is stored in a result table, called the “result-set.”
Example: SELECT column1, column2 FROM table_name;

INSERT INTO: Inserts new data into a database. The data to be inserted is written as a value list, inside parentheses and separated by commas.
Example: INSERT INTO table_name (column1, column2) VALUES (value1, value2);

UPDATE: Modifies data in a database. The SET keyword is used to modify the values of specified columns, and the WHERE keyword is used to specify which rows to update.
Example: UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;

DELETE: Deletes data from a database. The WHERE keyword is used to specify which rows to delete.
Example: DELETE FROM table_name WHERE condition;

CREATE: Creates a new database, table, or view in a database.
Example: CREATE TABLE table_name (column1 datatype, column2 datatype, ...);

ALTER: Modifies an existing database table in a database.
Example: ALTER TABLE table_name ADD column_name datatype;

DROP: Deletes a table, view, or other database object in a database.
Example: DROP TABLE table_name;

GROUP BY: Groups rows that have the same values in specified columns into aggregated data.
Example: SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;

HAVING: Similar to WHERE, but allows for filtering on grouped data.
Example: SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name HAVING COUNT(*) > value;

ORDER BY: Orders the result-set by one or more columns, in ascending or descending order.
Example: SELECT column_name FROM table_name ORDER BY column_name ASC|DESC;

These are some of the most common SQL queries, and understanding them is essential for working with relational databases.
Author: Faith Oputa.
