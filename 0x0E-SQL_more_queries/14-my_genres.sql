-- Lists all genres of the show Dexter
SELECT `tv_genres.name`
FROM `tv_genres`
INNER JOIN `tv_show_genres` AS 'm'
ON `tv_genres.id` = `m.genre_id`
INNER JOIN `tv_shows` AS 's'
ON `m.show_id` = `s.id`
WHERE `s.title` = 'Dexter'
ORDER BY `tv_genres.name` ASC;
