SELECT
    catid as category_id
    , catgroup as category_group
    , catname as category_name
    , catdesc as category_description
FROM
    {{ ref('category_pipe') }}
