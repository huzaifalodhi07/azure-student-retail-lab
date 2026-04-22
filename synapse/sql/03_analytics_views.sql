USE retail_serverless;
GO

CREATE OR ALTER VIEW serving.vw_sales_daily AS
SELECT
    CAST(o.order_date AS date) AS sales_date,
    o.sales_channel,
    COUNT(DISTINCT o.order_id) AS orders,
    COUNT(DISTINCT o.customer_id) AS customers,
    SUM(CAST(oi.quantity AS float) * CAST(oi.unit_price AS float) * (1 - CAST(oi.discount_pct AS float))) AS total_revenue
FROM ext.vw_orders o
JOIN ext.vw_order_items oi
  ON o.order_id = oi.order_id
WHERE o.order_status <> 'Cancelled'
GROUP BY CAST(o.order_date AS date), o.sales_channel;
GO

CREATE OR ALTER VIEW serving.vw_customer_360 AS
SELECT
    o.customer_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(CAST(oi.quantity AS float) * CAST(oi.unit_price AS float) * (1 - CAST(oi.discount_pct AS float))) AS total_revenue,
    MAX(CAST(o.order_date AS date)) AS last_order_date
FROM ext.vw_orders o
JOIN ext.vw_order_items oi
  ON o.order_id = oi.order_id
WHERE o.order_status <> 'Cancelled'
GROUP BY o.customer_id;
GO

CREATE OR ALTER VIEW serving.vw_product_performance AS
SELECT
    oi.product_id,
    COUNT(DISTINCT oi.order_id) AS order_count,
    SUM(CAST(oi.quantity AS float)) AS units_sold,
    SUM(CAST(oi.quantity AS float) * CAST(oi.unit_price AS float) * (1 - CAST(oi.discount_pct AS float))) AS total_revenue
FROM ext.vw_order_items oi
GROUP BY oi.product_id;
GO
