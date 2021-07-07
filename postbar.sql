/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : postbar

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2021-07-07 13:52:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for app1_loginmodel
-- ----------------------------
DROP TABLE IF EXISTS `app1_loginmodel`;
CREATE TABLE `app1_loginmodel` (
  `uid` varchar(64) NOT NULL,
  `password` varchar(128) NOT NULL,
  `identity` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of app1_loginmodel
-- ----------------------------
INSERT INTO `app1_loginmodel` VALUES ('62178451', '123456', 'user');
INSERT INTO `app1_loginmodel` VALUES ('62178452', '123456', 'user');
INSERT INTO `app1_loginmodel` VALUES ('62178453', '123456', 'admin');
INSERT INTO `app1_loginmodel` VALUES ('62178454', 'pbkdf2_sha256$260000$XAjm0xuIydhbe7dx4TPTOy$fxZlHDCVhVAuINRrCoR/9msf+TIPJwNVm3jO2v+HzDY=', 'user');
INSERT INTO `app1_loginmodel` VALUES ('62178455', 'pbkdf2_sha256$260000$fE3FiUeZ7rXFuOMGXmY0Ap$8D43y/vh8Zb88IdYfdlKmJU3hdexcmv0ib3cPBN7rtA=', 'user');

-- ----------------------------
-- Table structure for app1_postmodel
-- ----------------------------
DROP TABLE IF EXISTS `app1_postmodel`;
CREATE TABLE `app1_postmodel` (
  `postid` int NOT NULL AUTO_INCREMENT,
  `topic` varchar(255) NOT NULL,
  `uid` varchar(64) NOT NULL,
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `posttime` varchar(32) NOT NULL,
  `recent` int NOT NULL,
  `number` int NOT NULL,
  `text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`postid`),
  KEY `2` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of app1_postmodel
-- ----------------------------
INSERT INTO `app1_postmodel` VALUES ('14', '真是服了 雇人给宁白打工呢？', '62178451', '洛特的腿毛', '2021-06-24 22:32:13', '0', '0', '新cd dz幻化差个肩膀 自己搭了很久 上周基本一周都在围绕那身幻化 想着这周不出就再起个dz小号\r\n要刷的是萨墓dz肩膀 职业限定只能用dz 我dz是小号 自知dps不够 进了个团 都是安苏的 应该是朋友认识\r\n打之前我就问了不要再组人吗？');
INSERT INTO `app1_postmodel` VALUES ('15', '有什么职业，三只怪，五只怪，10只怪，爆发aoe。长时间aoe都还不错的，除了狂暴战', '62178451', '洛特的腿毛', '2021-06-25 23:25:05', '2', '2', '趁计生寺的没来我赶紧推荐一手踏风，就一个字，强无敌！');
INSERT INTO `app1_postmodel` VALUES ('16', '这是一条恶意信息！', '62178451', '洛特的腿毛', '2021-06-28 16:36:18', '0', '0', '恶意信息内容！！！');
INSERT INTO `app1_postmodel` VALUES ('17', '这是第二条恶意信息！', '62178451', '洛特的腿毛', '2021-06-28 16:54:18', '0', '0', '恶意信息内容！！！');
INSERT INTO `app1_postmodel` VALUES ('18', '测试跨站脚本XSS漏洞', '62178451', '洛特的腿毛', '2021-07-01 20:10:59', '4', '3', '回复留言中插入script脚本，alert(\"这是XSS脚本攻击!\")');
INSERT INTO `app1_postmodel` VALUES ('19', '这是一条恶意信息！（跨站请求伪造）', '62178451', '洛特的腿毛', '2021-07-02 17:13:26', '0', '0', '恶意信息内容！！！');
INSERT INTO `app1_postmodel` VALUES ('20', '这是一条恶意信息！（跨站请求伪造）', '62178451', '洛特的腿毛', '2021-07-02 17:17:58', '0', '0', '恶意信息内容！！！');
INSERT INTO `app1_postmodel` VALUES ('21', 'HTTP Header注入', '62178452', '落单先生', '2021-07-02 17:40:11', '0', '0', '修改http header的参数信息，以其他用户的身份发布帖子');
INSERT INTO `app1_postmodel` VALUES ('22', '这是一条恶意信息！（跨站请求伪造）', '62178451', '洛特的腿毛', '2021-07-03 12:03:47', '2', '2', '恶意信息内容！！！');
INSERT INTO `app1_postmodel` VALUES ('23', '用户62178452发布的帖子', '62178452', '落单先生', '2021-07-04 22:57:07', '0', '0', '1111');
INSERT INTO `app1_postmodel` VALUES ('24', '用户62178451发布的帖子', '62178451', '洛特的腿毛', '2021-07-04 22:58:15', '0', '0', '2222');
INSERT INTO `app1_postmodel` VALUES ('25', '用户62178451发布的帖子', '62178451', '洛特的腿毛', '2021-07-04 22:59:17', '0', '0', '3333');
INSERT INTO `app1_postmodel` VALUES ('26', '用户62178452的帖子，用于测试删除', '62178451', '洛特的腿毛', '2021-07-04 23:30:15', '1', '1', '1111');
INSERT INTO `app1_postmodel` VALUES ('27', '用户62178452的帖子，用于测试62178451删除', '62178452', '落单先生', '2021-07-04 23:34:35', '3', '1', '111');
INSERT INTO `app1_postmodel` VALUES ('28', '123', '62178451', '洛特的腿毛', '2021-07-05 14:38:58', '0', '0', '11111');
INSERT INTO `app1_postmodel` VALUES ('29', '模拟62178452发布的帖子', '62178452', '落单先生', '2021-07-05 21:56:01', '0', '0', '1111');
INSERT INTO `app1_postmodel` VALUES ('30', '该算法的耕地上', '62178451', '洛特的腿毛', '2021-07-05 22:26:04', '0', '0', '水电费广东省');
INSERT INTO `app1_postmodel` VALUES ('31', '这是一条恶意信息！（跨站请求伪造）', '62178451', '洛特的腿毛', '2021-07-05 23:03:27', '2', '2', '恶意信息内容！！！');
INSERT INTO `app1_postmodel` VALUES ('32', '<script>alert(\"存储型XSS！！！\");</script>', '62178451', '洛特的腿毛', '2021-07-07 01:41:47', '0', '0', '11111');
INSERT INTO `app1_postmodel` VALUES ('33', '这是一条恶意信息！（跨站请求伪造）', '62178451', '洛特的腿毛', '2021-07-07 02:27:31', '0', '0', '恶意信息内容！！！');
INSERT INTO `app1_postmodel` VALUES ('34', '模拟用户62178452', '62178452', '落单先生', '2021-07-07 13:20:39', '0', '0', '1111');

-- ----------------------------
-- Table structure for app1_replymodel
-- ----------------------------
DROP TABLE IF EXISTS `app1_replymodel`;
CREATE TABLE `app1_replymodel` (
  `replyid` int NOT NULL AUTO_INCREMENT,
  `postid` int NOT NULL,
  `uid` varchar(64) NOT NULL,
  `username` varchar(64) NOT NULL,
  `time` varchar(32) NOT NULL,
  `delete` int NOT NULL,
  `order` int NOT NULL,
  `content` varchar(255) NOT NULL,
  PRIMARY KEY (`replyid`),
  KEY `12` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of app1_replymodel
-- ----------------------------
INSERT INTO `app1_replymodel` VALUES ('15', '14', '62178453', '雷格西尔', '2021-06-24 22:35:07', '1', '1', '建议做个上马宏刷他\r\n另外，化身cd周末应该还是有人打的');
INSERT INTO `app1_replymodel` VALUES ('16', '14', '62178451', '洛特的腿毛', '2021-06-24 22:35:29', '1', '2', '看到关键字就该退了，能自己挂集合石等着也不进这种队');
INSERT INTO `app1_replymodel` VALUES ('17', '14', '62178453', '雷格西尔', '2021-06-24 22:35:45', '1', '3', '去风纪区挂他吧，这里貌似不让挂人的。');
INSERT INTO `app1_replymodel` VALUES ('18', '14', '62178451', '洛特的腿毛', '2021-06-24 22:37:40', '1', '4', '森岛帆高');
INSERT INTO `app1_replymodel` VALUES ('19', '15', '62178451', '洛特的腿毛', '2021-06-25 23:26:02', '0', '1', '上版本玩战士玩了两个大版本，这版本想玩个能毛过战士的');
INSERT INTO `app1_replymodel` VALUES ('20', '15', '62178453', '雷格西尔', '2021-06-25 23:28:05', '0', '2', '我们车队武僧t太拉跨了，扛不住几下就疯狂掉血。元素体验太差了');
INSERT INTO `app1_replymodel` VALUES ('21', '18', '62178451', '洛特的腿毛', '2021-07-02 10:47:30', '1', '1', 'alert(\"这是XSS脚本攻击!\")');
INSERT INTO `app1_replymodel` VALUES ('22', '18', '62178451', '洛特的腿毛', '2021-07-02 10:47:50', '0', '2', '<script>alert(\"这是XSS脚本攻击!\")</script>');
INSERT INTO `app1_replymodel` VALUES ('23', '18', '62178451', '洛特的腿毛', '2021-07-02 11:12:30', '0', '3', '<script>alert(\"这是XSS脚本攻击!\")</script>');
INSERT INTO `app1_replymodel` VALUES ('24', '18', '62178451', '洛特的腿毛', '2021-07-02 11:12:49', '0', '4', 'alert(\"这是XSS脚本攻击!\")');
INSERT INTO `app1_replymodel` VALUES ('25', '22', '62178451', '洛特的腿毛', '2021-07-04 11:54:21', '0', '1', '<script>alert(\"XSS攻击\")</script>');
INSERT INTO `app1_replymodel` VALUES ('26', '22', '62178451', '洛特的腿毛', '2021-07-04 11:54:59', '0', '2', 'alert(\"xss\")');
INSERT INTO `app1_replymodel` VALUES ('27', '26', '62178451', '洛特的腿毛', '2021-07-04 23:30:39', '0', '1', '2222');
INSERT INTO `app1_replymodel` VALUES ('28', '26', '62178451', '洛特的腿毛', '2021-07-04 23:30:49', '1', '2', '3333');
INSERT INTO `app1_replymodel` VALUES ('29', '26', '62178451', '洛特的腿毛', '2021-07-04 23:30:55', '1', '3', '4444');
INSERT INTO `app1_replymodel` VALUES ('30', '27', '62178452', '落单先生', '2021-07-04 23:34:42', '1', '1', '121');
INSERT INTO `app1_replymodel` VALUES ('31', '27', '62178452', '落单先生', '2021-07-04 23:34:47', '1', '2', '131');
INSERT INTO `app1_replymodel` VALUES ('32', '27', '62178452', '落单先生', '2021-07-04 23:34:51', '0', '3', '141');
INSERT INTO `app1_replymodel` VALUES ('33', '27', '62178451', '洛特的腿毛', '2021-07-05 21:27:34', '1', '4', 'alert(\"xss\")');
INSERT INTO `app1_replymodel` VALUES ('34', '27', '62178451', '洛特的腿毛', '2021-07-05 21:28:01', '1', '5', '<script>alert(\"xss\")</script>');
INSERT INTO `app1_replymodel` VALUES ('35', '29', '62178451', '洛特的腿毛', '2021-07-05 22:13:53', '1', '1', '<script>alert(\"xss\")</script>');
INSERT INTO `app1_replymodel` VALUES ('36', '29', '62178451', '洛特的腿毛', '2021-07-05 22:14:35', '1', '2', 'alert(\"xss\")');
INSERT INTO `app1_replymodel` VALUES ('37', '31', '62178451', '洛特的腿毛', '2021-07-07 02:13:58', '0', '1', '<script>alert(\"反射型XSS！！！\");</script>');
INSERT INTO `app1_replymodel` VALUES ('38', '31', '62178451', '洛特的腿毛', '2021-07-07 02:14:30', '0', '2', '<script>alert(\"反射型XSS！！！\");</script>');

-- ----------------------------
-- Table structure for app1_usermodel
-- ----------------------------
DROP TABLE IF EXISTS `app1_usermodel`;
CREATE TABLE `app1_usermodel` (
  `uid` varchar(64) NOT NULL,
  `intime` varchar(64) DEFAULT NULL,
  `username` varchar(64) DEFAULT NULL,
  `birthday` varchar(32) DEFAULT NULL,
  `edress` varchar(32) DEFAULT NULL,
  `gender` varchar(4) DEFAULT NULL,
  `location` varchar(32) DEFAULT NULL,
  `occupation` varchar(32) DEFAULT NULL,
  `phone` varchar(32) DEFAULT NULL,
  `sign` varchar(64) DEFAULT NULL,
  `userintro` varchar(64) DEFAULT NULL,
  `filename` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of app1_usermodel
-- ----------------------------
INSERT INTO `app1_usermodel` VALUES ('62178451', '2020.1.1', '洛特的腿毛', '2008-06-10', '1798679559@qq.com', '女', '华北电力大学（北京）', '学生', '110', '</textarea><script>alert(\"XSS\")</script><textarea>', '无', '62178451.png');
INSERT INTO `app1_usermodel` VALUES ('62178452', '2020.1.2', '落单先生', null, null, null, null, null, '120', null, null, null);
INSERT INTO `app1_usermodel` VALUES ('62178453', null, '雷格西尔', '2009-01-04', '2436585474@qq.com', '男', '北京', '学生', '13831754215', 'None', 'None', null);
INSERT INTO `app1_usermodel` VALUES ('62178454', null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `app1_usermodel` VALUES ('62178455', null, null, null, null, null, null, null, null, null, null, null);

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add login', '7', 'add_login');
INSERT INTO `auth_permission` VALUES ('26', 'Can change login', '7', 'change_login');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete login', '7', 'delete_login');
INSERT INTO `auth_permission` VALUES ('28', 'Can view login', '7', 'view_login');
INSERT INTO `auth_permission` VALUES ('29', 'Can add login model', '7', 'add_loginmodel');
INSERT INTO `auth_permission` VALUES ('30', 'Can change login model', '7', 'change_loginmodel');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete login model', '7', 'delete_loginmodel');
INSERT INTO `auth_permission` VALUES ('32', 'Can view login model', '7', 'view_loginmodel');
INSERT INTO `auth_permission` VALUES ('33', 'Can add post model', '8', 'add_postmodel');
INSERT INTO `auth_permission` VALUES ('34', 'Can change post model', '8', 'change_postmodel');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete post model', '8', 'delete_postmodel');
INSERT INTO `auth_permission` VALUES ('36', 'Can view post model', '8', 'view_postmodel');
INSERT INTO `auth_permission` VALUES ('37', 'Can add reply model', '9', 'add_replymodel');
INSERT INTO `auth_permission` VALUES ('38', 'Can change reply model', '9', 'change_replymodel');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete reply model', '9', 'delete_replymodel');
INSERT INTO `auth_permission` VALUES ('40', 'Can view reply model', '9', 'view_replymodel');
INSERT INTO `auth_permission` VALUES ('41', 'Can add user model', '10', 'add_usermodel');
INSERT INTO `auth_permission` VALUES ('42', 'Can change user model', '10', 'change_usermodel');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete user model', '10', 'delete_usermodel');
INSERT INTO `auth_permission` VALUES ('44', 'Can view user model', '10', 'view_usermodel');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('7', 'app1', 'loginmodel');
INSERT INTO `django_content_type` VALUES ('8', 'app1', 'postmodel');
INSERT INTO `django_content_type` VALUES ('9', 'app1', 'replymodel');
INSERT INTO `django_content_type` VALUES ('10', 'app1', 'usermodel');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2021-06-20 17:11:12.799322');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2021-06-20 17:11:13.865231');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2021-06-20 17:11:14.140002');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2021-06-20 17:11:14.152675');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2021-06-20 17:11:14.163673');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2021-06-20 17:11:14.311997');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2021-06-20 17:11:14.396610');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2021-06-20 17:11:14.428938');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2021-06-20 17:11:14.442019');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2021-06-20 17:11:14.527416');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2021-06-20 17:11:14.533587');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2021-06-20 17:11:14.544379');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2021-06-20 17:11:14.628301');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2021-06-20 17:11:14.725503');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0010_alter_group_name_max_length', '2021-06-20 17:11:14.752174');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0011_update_proxy_permissions', '2021-06-20 17:11:14.764444');
INSERT INTO `django_migrations` VALUES ('17', 'auth', '0012_alter_user_first_name_max_length', '2021-06-20 17:11:14.850312');
INSERT INTO `django_migrations` VALUES ('18', 'sessions', '0001_initial', '2021-06-20 17:11:14.904910');
INSERT INTO `django_migrations` VALUES ('19', 'app1', '0001_initial', '2021-06-20 17:12:34.738682');
INSERT INTO `django_migrations` VALUES ('20', 'app1', '0002_rename_login_loginmodel', '2021-06-20 17:39:20.669807');
INSERT INTO `django_migrations` VALUES ('21', 'app1', '0003_postmodel_replymodel', '2021-06-20 18:10:17.525992');
INSERT INTO `django_migrations` VALUES ('22', 'app1', '0004_usermodel', '2021-06-20 18:14:07.156528');
INSERT INTO `django_migrations` VALUES ('23', 'app1', '0005_auto_20210621_0214', '2021-06-20 18:15:09.878380');
INSERT INTO `django_migrations` VALUES ('24', 'app1', '0006_rename_password_usermodel_intime', '2021-06-20 18:16:19.696122');
INSERT INTO `django_migrations` VALUES ('25', 'app1', '0007_postmodel_content', '2021-06-22 09:34:36.171185');
INSERT INTO `django_migrations` VALUES ('26', 'app1', '0008_remove_postmodel_content', '2021-06-22 09:34:36.476643');
INSERT INTO `django_migrations` VALUES ('27', 'app1', '0009_postmodel_text', '2021-06-22 09:38:21.068024');
INSERT INTO `django_migrations` VALUES ('28', 'app1', '0010_auto_20210623_0110', '2021-06-22 17:10:50.687775');
INSERT INTO `django_migrations` VALUES ('29', 'app1', '0011_auto_20210624_2157', '2021-06-24 13:58:59.156410');
INSERT INTO `django_migrations` VALUES ('30', 'app1', '0012_auto_20210624_2200', '2021-06-24 14:14:43.641125');
INSERT INTO `django_migrations` VALUES ('31', 'app1', '0013_auto_20210624_2201', '2021-06-24 14:14:43.888845');
INSERT INTO `django_migrations` VALUES ('32', 'app1', '0014_auto_20210624_2205', '2021-06-24 14:14:44.152228');
INSERT INTO `django_migrations` VALUES ('33', 'app1', '0015_auto_20210624_2212', '2021-06-24 14:14:44.181675');
INSERT INTO `django_migrations` VALUES ('34', 'app1', '0016_auto_20210624_2218', '2021-06-24 14:18:53.091379');
INSERT INTO `django_migrations` VALUES ('35', 'app1', '0017_auto_20210624_2231', '2021-06-24 14:31:16.853890');
INSERT INTO `django_migrations` VALUES ('36', 'app1', '0018_usermodel_filename', '2021-06-30 05:00:31.185652');
INSERT INTO `django_migrations` VALUES ('37', 'app1', '0019_alter_loginmodel_password', '2021-07-01 03:00:01.166475');
INSERT INTO `django_migrations` VALUES ('38', 'app1', '0020_alter_replymodel_postid', '2021-07-01 03:04:06.294676');
INSERT INTO `django_migrations` VALUES ('39', 'app1', '0021_loginmodel_identity', '2021-07-05 07:38:40.068923');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of django_session
-- ----------------------------
DROP TRIGGER IF EXISTS `new_user`;
DELIMITER ;;
CREATE TRIGGER `new_user` AFTER INSERT ON `app1_loginmodel` FOR EACH ROW insert into app1_usermodel(uid)
values(new.uid)
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `add_post_number`;
DELIMITER ;;
CREATE TRIGGER `add_post_number` AFTER INSERT ON `app1_replymodel` FOR EACH ROW update app1_postmodel
set app1_postmodel.number=app1_postmodel.number+1
where app1_postmodel.postid=new.postid
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `add_post_recent`;
DELIMITER ;;
CREATE TRIGGER `add_post_recent` AFTER INSERT ON `app1_replymodel` FOR EACH ROW update app1_postmodel
set app1_postmodel.recent=new.order
where app1_postmodel.postid=new.postid
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `update_post`;
DELIMITER ;;
CREATE TRIGGER `update_post` AFTER UPDATE ON `app1_usermodel` FOR EACH ROW update app1_postmodel
set app1_postmodel.username=new.username
where app1_postmodel.uid=new.uid
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `update_reply`;
DELIMITER ;;
CREATE TRIGGER `update_reply` AFTER UPDATE ON `app1_usermodel` FOR EACH ROW update app1_replymodel
set app1_replymodel.username = new.username
where app1_replymodel.uid=new.uid
;;
DELIMITER ;
