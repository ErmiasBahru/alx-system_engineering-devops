# MySQL

This task was aimed at understanding the following concepts:-

* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

## FILES

The following task files were used to help acomplish various tasks testing the concepts.

[4-mysql_configuration_primary](./4-mysql_configuration_primary)

This is a copy of /etc/mysql/mysql.conf.d/mysqld.cnf configuration file after configuring the MySQL primary hosted on web-01. Setup replication set for MySQL database named `tyrell_corp`.

[4-mysql_configuration_replica](./4-mysql_configuration_replica)

This is a copy of /etc/mysql/mysql.conf.d/mysqld.cnf configuration file after configuring the MySQL replica hosted on web-02. Setup replication set for MySQL database named `tyrell_corp`.

[5-mysql_backup](./5-mysql_backup)

Script that generates a MySQL dump and creates a compressed archive out of it.
