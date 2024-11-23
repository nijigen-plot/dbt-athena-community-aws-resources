SELECT
    d.year
    , d.month
    , SUM(commission) as commission
FROM
    {{ ref('stg_tickit__sales') }} as s
INNER JOIN
    {{ ref('stg_tickit__date') }} as d
ON
    s.date_id = d.date_id
GROUP BY
    1,2
