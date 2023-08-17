--  a script that lists all shows without the genre Comedy 
SELECT DISTINCT t.title FROM tv_shows t 
    LEFT JOIN tv_show_genres g 
    ON t.id = g.show_id

    LEFT JOIN tv_genres s
    ON s.id = g.genre_id

    WHERE  t.id NOT IN 
    (SELECT t.id FROM tv_shows t
        INNER JOIN tv_show_genres g 
        ON t.id = g.show_id

        INNER JOIN tv_genres s
        ON s.id = g.genre_id

        WHERE s.name = 'Comedy')
ORDER BY t.title ASC;
