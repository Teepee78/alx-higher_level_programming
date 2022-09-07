-- List all shows and genres linked to show from 'hbtn_0d_tvshows'
SELECT `s.title`, `g.name`
FROM `tv_shows` AS 's'
LEFT JOIN `tv_show_genres` AS 'm'
ON `s.id` = `m.show_id`
LEFT JOIN `tv_genres` AS 'g'
ON `m.genre_id` = `g.id`
ORDER BY `s.title`;
