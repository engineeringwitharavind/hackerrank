SELECT
      CAST(SUM(LAT_N) AS DECIMAL(7,2)),
      CAST(SUM(LONG_W) AS DECIMAL(7,2))
FROM STATION;