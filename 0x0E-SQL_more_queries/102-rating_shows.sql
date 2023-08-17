-- a script that lists all shows  by their rating
SELECT title, SUM(rate) as rating FROM tv_shows t 
    INNER JOIN tv_show_ratings r 
    ON t.id = r.show_id
GROUP BY title
ORDER BY rating DESC;
