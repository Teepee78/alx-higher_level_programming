-- List all genres not linked to show 'Dexter'
SELECT `g.name`
FROM `tv_genres` AS 'g'
WHERE `g.name` NOT IN (
    SELECT `g.name`
    FROM `tv_genres` AS 'g'
    INNER JOIN `tv_show_genres` AS 'm'
    ON `g.id` = `m.genre_id`
    INNER JOIN `tv_shows` AS 's'
    ON `m.show_id` = `s.id`
    WHERE `s.title` = 'Dexter'
)
ORDER BY `g.name`;
