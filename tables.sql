CREATE TABLE audio
(
audio_id BINARY(16),
title TEXT NOT NULL UNIQUE,
content MEDIUMBLOB NOT NULL,
PRIMARY KEY (audio_id)
) COMMENT='this table stores sons';

DELIMITER ;;
CREATE TRIGGER `audio_before_insert` 
BEFORE INSERT ON `audio` FOR EACH ROW 
BEGIN
  IF new.audio_id IS NULL THEN
    SET new.audio_id = UUID_TO_BIN(UUID(), TRUE);
  END IF;
END;;
DELIMITER ;