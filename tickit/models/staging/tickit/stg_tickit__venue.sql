SELECT
    venueid as venue_id
    , venuename as venue_name
    , venuecity as venue_city
    , venuestate as venue_state
    , venueseats as venue_seats
FROM
    {{ ref('venue_pipe') }}
