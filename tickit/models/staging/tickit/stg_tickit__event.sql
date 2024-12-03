SELECT
    eventid as event_id
    , venueid as venue_id
    , catid as category_id
    , dateid as date_id
    , eventname as event_name
    , starttime as start_time
FROM
    {{ ref('allevents_pipe') }}
