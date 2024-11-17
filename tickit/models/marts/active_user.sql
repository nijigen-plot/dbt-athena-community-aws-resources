SELECT
    d.calendar_date
    , COUNT(distinct u.user_id) as user_count
FROM
    {{ ref('stg_tickit__sales') }} as s
INNER JOIN
    {{ ref('stg_tickit__users')}} as u
ON
    s.buyer_id = u.user_id
INNER JOIN
    {{ ref('stg_tickit__date') }} as d
ON
    s.date_id = d.date_id
GROUP BY
    1
