--  a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.title FROM tv_shows t INNER JOIN tv_show_genres g ON t.id = g.show_id
INNER JOIN tv_genres s ON s.id = g.genre_id WHERE s.name = 'Comedy'
ORDER BY t.title ASC;
