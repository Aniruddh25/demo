  CREATE DATABASE Hospital;
  USE Hospital;
    CREATE USER revotester for login revotester

  GRANT ALL TO revotester

  exec sp_addrolemember 'db_owner', 'revotester'
exec sp_addrolemember 'db_ddladmin', 'revotester'
exec sp_addrolemember 'db_accessadmin', 'revotester'
exec sp_addrolemember 'db_datareader', 'revotester'
exec sp_addrolemember 'db_datawriter', 'revotester'
exec sp_addsrvrolemember @loginame= 'revotester', @rolename = 'sysadmin'  