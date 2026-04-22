USE retail_serverless;
GO

CREATE EXTERNAL TABLE serving.sales_daily_export
WITH (
    LOCATION = 'serving/sales_daily_export/',
    DATA_SOURCE = RetailLake,
    FILE_FORMAT = ParquetFormat
)
AS
SELECT * FROM serving.vw_sales_daily;
GO

CREATE EXTERNAL TABLE serving.customer_360_export
WITH (
    LOCATION = 'serving/customer_360_export/',
    DATA_SOURCE = RetailLake,
    FILE_FORMAT = ParquetFormat
)
AS
SELECT * FROM serving.vw_customer_360;
GO
