--  a script that uses the hbtn_0d_tvshows database to list
--   all genres not linked to the show Dexter

SELECT g.name FROM tv_genres g 
    INNER JOIN tv_show_genres t 
    ON g.id = t.genre_id
        INNER JOIN tv_shows s ON s.id = t.show_id 
            WHERE g.name NOT IN 
            (SELECT g.name FROM tv_genres g 
                INNER JOIN tv_show_genres t 
                ON g.id = t.genre_id

                INNER JOIN tv_shows s 
                ON s.id = t.show_id 
                WHERE s.title = 'Dexter')
GROUP BY g.name
ORDER BY g.name ASC;