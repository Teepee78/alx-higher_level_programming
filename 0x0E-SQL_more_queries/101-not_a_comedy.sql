-- List all shows without genre 'Comedy' in 'hbtn_0d_tvshows'
SELECT `s.title`
FROM `tv_shows` AS 's'
WHERE `s.title` NOT IN (
    SELECT `s.title`
    FROM `tv_shows` AS 's'
    INNER JOIN `tv_show_genres` AS 'm'
    ON `s.id` = `m.show_id`
    INNER JOIN `tv_genres` AS 'g'
    ON `m.genre_id` = `g.id`
    WHERE `g.name` = 'Comedy'
)
ORDER BY `s.title`;
