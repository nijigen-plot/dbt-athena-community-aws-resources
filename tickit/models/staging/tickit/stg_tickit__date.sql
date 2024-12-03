SELECT
    dateid as date_id
    , caldate as calendar_date
    , day
    , week
    , month
    , qtr as quarter
    , year
    , holiday
FROM
    {{ ref('date2008_pipe') }}
