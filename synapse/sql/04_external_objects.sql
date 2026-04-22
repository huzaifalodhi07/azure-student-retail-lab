USE retail_serverless;
GO

CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'ChangeThisStrongPassword!234';
GO

CREATE DATABASE SCOPED CREDENTIAL WorkspaceIdentity
WITH IDENTITY = 'Managed Identity';
GO

CREATE EXTERNAL DATA SOURCE RetailLake
WITH (
    LOCATION = 'https://<storage-account>.dfs.core.windows.net/retaildatalake',
    CREDENTIAL = WorkspaceIdentity
);
GO

CREATE EXTERNAL FILE FORMAT ParquetFormat
WITH (FORMAT_TYPE = PARQUET);
GO
