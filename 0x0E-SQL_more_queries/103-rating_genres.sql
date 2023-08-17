-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(r.rate) AS rating FROM tv_genres g 
    INNER JOIN tv_show_genres t 
    ON g.id = t.genre_id

    INNER JOIN tv_shows s
    ON s.id = t.show_id

    INNER JOIN tv_show_ratings r
    ON r.show_id = s.id

GROUP BY g.name
ORDER BY rating DESC;
