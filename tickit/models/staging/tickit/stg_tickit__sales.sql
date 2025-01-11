SELECT
    salesid as sales_id
    , listid as list_id
    , sellerid as seller_id
    , buyerid as buyer_id
    , eventid as event_id
    , dateid as date_id
    , qtysold as qtysold
    , pricepaid as price_paid
    , commission
    , saletime as sale_time
FROM
    {{ ref('sales_tab') }}
