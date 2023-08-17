-- a script that lists all shows 
-- contained in hbtn_0d_tvshows
SELECT t.title, g.genre_id FROM tv_shows t INNER JOIN tv_show_genres g ON t.id = g.show_id
ORDER BY t.title, g.genre_id ASC ;
