-- CREATE DATABASE IF NOT EXISTS `Novel`;
-- USE `Novel`;


CREATE TABLE IF NOT EXISTS `novels` (
	`title_id` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'С˵id����',
	`title` VARCHAR(50) COMMENT 'С˵����',
	`title_url` VARCHAR(512) COMMENT 'С˵����',
	`novel_img` VARCHAR(512) COMMENT 'С˵����ͼ',
	`word_count` INT(9) NOT NULL DEFAULT 0 COMMENT 'С˵��С',
	`category` VARCHAR(20) COMMENT 'С˵����',
	`author` VARCHAR(20) COMMENT 'С˵����',
	`novel_info` TEXT COMMENT 'С˵���',
	`update_at` DATE COMMENT '��������',
	`total_ck` INT(8) NOT NULL DEFAULT 0 COMMENT '�ܵ��',
	`mon_ck` INT(6) NOT NULL DEFAULT 0 COMMENT '�µ��',
	`collect_counts` INT(6) NOT NULL DEFAULT 0 COMMENT '�ղ���',
	`recommend` INT(5) NOT NULL DEFAULT 0 COMMENT '���Ƽ�',
	`mon_reco` INT(4) NOT NULL DEFAULT 0 COMMENT '���Ƽ�',
	PRIMARY KEY (`title_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT 'С˵����';

CREATE TABLE IF NOT EXISTS `chapters` (
	`tc_id` VARCHAR(32) NOT NULL DEFAULT 0 COMMENT 'id����',
	`chapter_id` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '�½�id',
	`title_id` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'С˵id',
	`chapter_title` VARCHAR(50) COMMENT '�½�����',
	`chapter_url` VARCHAR(512) COMMENT '�½�����',
	`chapter_content` TEXT COMMENT '�½�����',
	PRIMARY KEY (`tc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '�½���Ϣ��';
