USE retail_serverless;
GO

CREATE OR ALTER VIEW ext.vw_customers AS
SELECT *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/customers/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW ext.vw_products AS
SELECT *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/products/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW ext.vw_orders AS
SELECT *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/orders/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW ext.vw_order_items AS
SELECT *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/order_items/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW ext.vw_payments AS
SELECT *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/payments/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW ext.vw_returns AS
SELECT *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/returns/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW ext.vw_web_events AS
SELECT *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/web_events/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO
