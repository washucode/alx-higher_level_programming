-- a script that lists all shows, and all genres linked to that show, 
-- from the database hbtn_0d_tvshows
SELECT t.title, g.name FROM tv_shows t LEFT JOIN tv_show_genres s ON t.id = s.show_id
LEFT JOIN tv_genres g ON g.id = s.genre_id ORDER BY t.title, g.name ASC;
