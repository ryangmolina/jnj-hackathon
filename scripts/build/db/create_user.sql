-- Creates DB user
CREATE USER communiteerdbuser WITH PASSWORD 'password';
CREATE DATABASE communiteerdb;
GRANT ALL PRIVILEGES ON DATABASE communiteerdb TO communiteerdbuser;

