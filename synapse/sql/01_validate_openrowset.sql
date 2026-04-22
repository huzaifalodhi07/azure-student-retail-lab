USE retail_serverless;
GO

SELECT TOP 10 *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/orders/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO

SELECT TOP 10 *
FROM OPENROWSET(
    BULK 'https://<storage-account>.dfs.core.windows.net/retaildatalake/curated/order_items/*.parquet',
    FORMAT = 'PARQUET'
) AS rows;
GO
