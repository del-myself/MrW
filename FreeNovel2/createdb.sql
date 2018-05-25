-- CREATE DATABASE IF NOT EXISTS `Novel`;
-- USE `Novel`;


CREATE TABLE IF NOT EXISTS `novels` (
	`title_id` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '小说id主键',
	`title` VARCHAR(50) COMMENT '小说名称',
	`title_url` VARCHAR(512) COMMENT '小说链接',
	`novel_img` VARCHAR(512) COMMENT '小说封面图',
	`word_count` INT(9) NOT NULL DEFAULT 0 COMMENT '小说大小',
	`category` VARCHAR(20) COMMENT '小说分类',
	`author` VARCHAR(20) COMMENT '小说作者',
	`novel_info` TEXT COMMENT '小说简介',
	`update_at` DATE COMMENT '更新日期',
	`total_ck` INT(8) NOT NULL DEFAULT 0 COMMENT '总点击',
	`mon_ck` INT(6) NOT NULL DEFAULT 0 COMMENT '月点击',
	`collect_counts` INT(6) NOT NULL DEFAULT 0 COMMENT '收藏数',
	`recommend` INT(5) NOT NULL DEFAULT 0 COMMENT '总推荐',
	`mon_reco` INT(4) NOT NULL DEFAULT 0 COMMENT '月推荐',
	PRIMARY KEY (`title_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '小说总览';

CREATE TABLE IF NOT EXISTS `chapters` (
	`tc_id` VARCHAR(32) NOT NULL DEFAULT 0 COMMENT 'id主键',
	`chapter_id` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '章节id',
	`title_id` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '小说id',
	`chapter_title` VARCHAR(50) COMMENT '章节名称',
	`chapter_url` VARCHAR(512) COMMENT '章节链接',
	`chapter_content` TEXT COMMENT '章节内容',
	PRIMARY KEY (`tc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '章节信息表';
