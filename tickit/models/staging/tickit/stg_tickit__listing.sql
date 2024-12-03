SELECT
    listid as list_id
    , sellerid as seller_id
    , eventid as event_id
    , dateid as date_id
    , numtickets as available_tickets
    , priceperticket as price_per_ticket
    , totalprice as total_price
    , listtime as list_time
FROM
    {{ ref('listings_pipe') }}
