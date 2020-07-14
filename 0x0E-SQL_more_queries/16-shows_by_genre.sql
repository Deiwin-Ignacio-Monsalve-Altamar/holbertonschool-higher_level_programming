-- atabase dump from hbtn_0d_tvshows to your MySQL server: download
SELECT
    tv_shows.title,
    tv_genres.name
FROM
    tv_genres
    RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title,
    tv_genres.name ASC;