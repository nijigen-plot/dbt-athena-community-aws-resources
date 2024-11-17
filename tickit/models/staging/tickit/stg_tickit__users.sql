SELECT
    userid as user_id
    , username as user_name
    , firstname as first_name
    , lastname as last_name
    , (firstname || lastname) as full_name
    , city
    , state
    , email
    , phone as phone_number
    , likesports as like_sports
    , liketheatre as like_theatre
    , likeconcerts as like_concerts
    , likejazz as like_jazz
    , likeclassical as like_classical
    , likeopera as like_opera
    , likerock as like_rock
    , likevegas as like_vegas
    , likebroadway as like_broadway
    , likemusicals as like_musicals
FROM
    {{ source('tickit','users')}}
