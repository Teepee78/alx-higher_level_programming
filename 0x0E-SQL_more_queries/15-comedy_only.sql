-- List all Comedy shows in 'hbtn_0d_tvshows'
SELECT `tv_shows.title`
FROM `tv_shows`
INNER JOIN `tv_show_genres` AS 'm'
ON `tv_shows.id` = `m.show_id`
INNER JOIN `tv_genres` AS 'g'
ON `m.genre_id` = `g.id`
WHERE `g.name` = 'Comedy'
ORDER BY `tv_shows.title`;
