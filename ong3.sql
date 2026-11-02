-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-11-2026 a las 21:42:58
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ong3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencias`
--

CREATE TABLE `asistencias` (
  `id_asistencia` int(11) NOT NULL,
  `id_evento` int(11) NOT NULL,
  `id_voluntario` int(11) NOT NULL,
  `hora_llegada` datetime NOT NULL,
  `hora_salida` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asistencias`
--

INSERT INTO `asistencias` (`id_asistencia`, `id_evento`, `id_voluntario`, `hora_llegada`, `hora_salida`) VALUES
(5, 3, 3, '2025-11-20 11:00:00', '2025-11-20 14:00:00'),
(6, 2, 5, '2025-12-25 06:00:00', '2025-12-25 00:00:00'),
(7, 7, 15, '2025-11-22 08:00:00', '2025-11-22 11:00:00'),
(8, 7, 10, '2025-11-22 08:00:00', '2025-11-22 12:00:00'),
(10, 7, 18, '2025-11-22 10:00:00', '2025-11-22 15:00:00'),
(11, 6, 14, '2015-11-21 08:00:00', '2015-11-21 13:00:00'),
(12, 6, 16, '2025-11-21 08:00:00', '2025-11-21 13:00:00'),
(13, 8, 19, '2026-01-10 09:00:00', '2026-01-10 18:00:00'),
(14, 8, 14, '2026-01-11 09:00:00', '2026-01-11 18:00:00'),
(15, 8, 11, '2026-01-12 09:00:00', '2026-01-12 18:00:00'),
(16, 8, 3, '2026-01-13 09:00:00', '2026-01-13 20:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add asistencia', 7, 'add_asistencia'),
(26, 'Can change asistencia', 7, 'change_asistencia'),
(27, 'Can delete asistencia', 7, 'delete_asistencia'),
(28, 'Can view asistencia', 7, 'view_asistencia'),
(29, 'Can add evento', 8, 'add_evento'),
(30, 'Can change evento', 8, 'change_evento'),
(31, 'Can delete evento', 8, 'delete_evento'),
(32, 'Can view evento', 8, 'view_evento'),
(33, 'Can add inscripcion', 9, 'add_inscripcion'),
(34, 'Can change inscripcion', 9, 'change_inscripcion'),
(35, 'Can delete inscripcion', 9, 'delete_inscripcion'),
(36, 'Can view inscripcion', 9, 'view_inscripcion'),
(37, 'Can add voluntario', 10, 'add_voluntario'),
(38, 'Can change voluntario', 10, 'change_voluntario'),
(39, 'Can delete voluntario', 10, 'delete_voluntario'),
(40, 'Can view voluntario', 10, 'view_voluntario'),
(41, 'Can add bitacora', 11, 'add_bitacora'),
(42, 'Can change bitacora', 11, 'change_bitacora'),
(43, 'Can delete bitacora', 11, 'delete_bitacora'),
(44, 'Can view bitacora', 11, 'view_bitacora'),
(45, 'Can add bloqueo usuario', 12, 'add_bloqueousuario'),
(46, 'Can change bloqueo usuario', 12, 'change_bloqueousuario'),
(47, 'Can delete bloqueo usuario', 12, 'delete_bloqueousuario'),
(48, 'Can view bloqueo usuario', 12, 'view_bloqueousuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$ZRpSQLEDvNEydSDy3lUc5d$Igjz7Vn4YsQxVMxtjrLCKJk5/7irVjjhuOWnFX+FKlM=', '2026-11-02 20:24:38.645596', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2025-11-30 17:28:42.816969'),
(2, 'pbkdf2_sha256$600000$QSfT88WaZdbFvkRnuvorQY$uA9QxAx/AEbPw69y5JRZJAWSUdke8uHVycH8VxOsFNs=', '2026-11-02 18:51:13.605067', 0, 'operador01', 'Alan', 'Brito', 'alanbrito@gmail.com', 1, 1, '2025-11-30 23:00:50.000000'),
(3, 'pbkdf2_sha256$1000000$ue8mTxlOWryxpXXNDczgdM$Oyd9cobjayJb54UET1IYdB2hzTbGPwuWaTMyAv04ztY=', NULL, 0, 'operador02', 'juan', 'marcos', 'juanmarcos@gmail.com', 1, 1, '2025-11-30 23:03:06.000000'),
(4, 'pbkdf2_sha256$1000000$GttEpdvqxyclccKbcapxD8$HV+BCTrlr049Q+ChfgTtLc5ZU9HaXEqTidu/idEPgSc=', NULL, 0, 'operador03', 'Luz', 'Clara', 'LuzClara@gmail.com', 1, 1, '2025-11-30 23:04:47.000000'),
(5, 'pbkdf2_sha256$600000$B5xLES2qBVaFkYsy4DqYB1$mE6DmkMItQsJhVfVqkQcrRj3oSS5FceNY4mir+tmEck=', '2026-11-02 20:22:28.345184', 1, 'admin2', 'ad', 'min', 'admin2@gmail.com', 1, 1, '2025-11-30 23:07:06.000000'),
(6, 'pbkdf2_sha256$600000$pvpOlHmuKv3awpeqJ2aU8O$M3GBcPUe6wgWEYoSc+cDhUu698tj0tB16FuvaR5BXwc=', '2026-11-02 19:28:07.639790', 0, 'UnUsuario', '', '', '', 0, 1, '2026-11-02 19:28:07.044135');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-11-30 23:00:51.561450', '2', 'operador01', 1, '[{\"added\": {}}]', 4, 1),
(2, '2025-11-30 23:02:01.930044', '2', 'operador01', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]', 4, 1),
(3, '2025-11-30 23:03:07.626972', '3', 'operador02', 1, '[{\"added\": {}}]', 4, 1),
(4, '2025-11-30 23:03:30.849669', '3', 'operador02', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]', 4, 1),
(5, '2025-11-30 23:04:48.091330', '4', 'operador03', 1, '[{\"added\": {}}]', 4, 1),
(6, '2025-11-30 23:05:39.960210', '4', 'operador03', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]', 4, 1),
(7, '2025-11-30 23:07:07.540490', '5', 'admin2', 1, '[{\"added\": {}}]', 4, 1),
(8, '2025-11-30 23:07:21.473128', '5', 'admin2', 2, '[{\"changed\": {\"fields\": [\"Email address\", \"Staff status\", \"Superuser status\"]}}]', 4, 1),
(9, '2025-11-30 23:07:46.724250', '5', 'admin2', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 4, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'appong', 'asistencia'),
(8, 'appong', 'evento'),
(9, 'appong', 'inscripcion'),
(10, 'appong', 'voluntario'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(11, 'seguridad', 'bitacora'),
(12, 'seguridad', 'bloqueousuario'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-11-30 17:27:39.725270'),
(2, 'auth', '0001_initial', '2025-11-30 17:27:40.630576'),
(3, 'admin', '0001_initial', '2025-11-30 17:27:40.858016'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-11-30 17:27:40.869542'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-11-30 17:27:40.900729'),
(6, 'appong', '0001_initial', '2025-11-30 17:27:40.908776'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-11-30 17:27:41.093014'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-11-30 17:27:41.206932'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-11-30 17:27:41.247240'),
(10, 'auth', '0004_alter_user_username_opts', '2025-11-30 17:27:41.258216'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-11-30 17:27:41.358801'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-11-30 17:27:41.363344'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-11-30 17:27:41.375646'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-11-30 17:27:41.491016'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-11-30 17:27:41.613331'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-11-30 17:27:41.643860'),
(17, 'auth', '0011_update_proxy_permissions', '2025-11-30 17:27:41.658968'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-11-30 17:27:41.780529'),
(19, 'sessions', '0001_initial', '2025-11-30 17:27:41.854934'),
(20, 'seguridad', '0001_initial', '2026-11-02 18:39:18.534082');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('47pvhcb33x838s3g4wji9djevx89d42s', '.eJxVjDsOwjAQBe_iGlkbx19Kes5g7XodHEC2FCcV4u4QKQW0b2beS0Tc1hK3npc4szgLJU6_G2F65LoDvmO9NZlaXZeZ5K7Ig3Z5bZyfl8P9OyjYy7cGJA2g84iswSbtEhpmz9Znb4Jj5chOPDCMBilNqJVKLgwEmg0Fm8X7A_CTOFU:1vPqXi:6QBRKTgUZvGkfYjC_6nL3GVzbhIhEYC7_q9VcFWXk8w', '2025-12-14 23:09:22.309984'),
('o3hto9c0s7e8dwboff1xvq1ju4gwaat4', '.eJxVjDsOwyAQRO9CHSGw-aZM7zOg3QUHJxFIxq6i3D1GcpGUM-_NvFmAfcthb2kNS2RXJtnlt0OgZyodxAeUe-VUy7YuyLvCT9r4VGN63U737yBDy309K9LGIABa4cak1ZGjIQChEC2ZkWx0ftZaHkBENxiQAr3Xg0BKln2--6c4KQ:1xNxia:ULY0uGILmEk3S4UZ7xPjk3jmeRghfK1xZyGX5KRJeOE', '2026-11-16 19:29:20.903509'),
('ouoryip0h5gmrfw4nupamw1d9p2m6dpf', '.eJxVjDkOwjAURO_iGlneF0r6nMH63wsOIFuKkwpxdxIpBZQz7828SYBtrWEbeQlzIlfCyeW3Q4jP3A6QHtDuncbe1mVGeij0pINOPeXX7XT_DiqMuq-NZAi28ChzBus0qqKsUQW48MzroovgIkHhjqnkcY-ovUuI1kklhSGfL-XbN6k:1xID6u:2hTSu_5agBGEB_KPr4ZPL22DYCe6Blh3xQ-AdjKz_2k', '2026-10-31 22:42:40.135206'),
('r6xgfnns7p984z05n1y2o5i3qp6ot6qe', '.eJxVjDsOwjAQBe_iGlnE8ZeSnjNY6901DiBbipMKcXcSKQW0b2beW0RYlxLXznOcSFzEIE6_WwJ8ct0BPaDem8RWl3lKclfkQbu8NeLX9XD_Dgr0stXZOBMyjaPOwIE9KOMTAGkKxhKh0cjOWQ_oB23VCDb5c9aYrdvKpMTnCwDJOFE:1vPlEm:Yw0TqWnbMsTmzhsKJrJGvoAPNgtaoyLLUPTDwEWViaY', '2025-12-14 17:29:28.064550');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventos`
--

CREATE TABLE `eventos` (
  `id_evento` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `proposito` varchar(200) NOT NULL,
  `fecha_inicio` datetime NOT NULL,
  `fecha_fin` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `eventos`
--

INSERT INTO `eventos` (`id_evento`, `nombre`, `proposito`, `fecha_inicio`, `fecha_fin`) VALUES
(1, 'noche buena en familia', 'reunir familiar de bajos recursos en la noche buena', '2025-12-24 20:00:00', '2025-12-24 23:00:00'),
(2, 'papa noel visita Viacha', 'repartir juguetes a los infantes de Viacha', '2025-12-25 07:30:00', '2025-12-25 08:30:00'),
(3, 'el agua es un recurso valioso', 'dar 3 dias continuos de seminarios  para concientisar sobre la importancia del agua en La Paz', '2025-11-30 20:30:00', '2025-11-30 22:00:00'),
(5, 'la calidad del aire en la paz', 'un seminario que concientiza a los ciudadanos de La Paz', '2025-12-01 18:00:00', '2025-12-01 22:00:00'),
(6, 'Conciencia sobre el medio ambiente', 'Con el proposito de concientizar sobre el medio ambiente y dar un mensaje a todas las personas sobre el estado del acosistema.', '2025-11-21 10:00:00', '2025-11-21 12:00:00'),
(7, 'Curso de Reciclaje', 'Para poder guiar a las personas sobre el correcto metodo de implementación del reciclaje', '2025-11-22 09:00:00', '2025-11-22 12:00:00'),
(8, 'Campaña de utiles escolares', 'Para que los niños puedan iniciar el año con los utiles necesarios para iniciar clases.', '2026-01-10 10:00:00', '2026-01-13 15:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripciones`
--

CREATE TABLE `inscripciones` (
  `id_inscripcion` int(11) NOT NULL,
  `id_evento` int(11) NOT NULL,
  `id_voluntario` int(11) NOT NULL,
  `rol` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inscripciones`
--

INSERT INTO `inscripciones` (`id_inscripcion`, `id_evento`, `id_voluntario`, `rol`) VALUES
(3, 1, 1, 'seguridad'),
(4, 2, 3, 'chofer'),
(5, 3, 5, 'presentador'),
(6, 5, 6, 'seguridad'),
(7, 1, 6, 'chef'),
(8, 7, 15, 'Logistica'),
(9, 7, 10, 'Presentador'),
(11, 7, 18, 'Presentador'),
(12, 6, 14, 'Presentador'),
(13, 6, 16, 'logistica'),
(14, 8, 19, 'Logistica'),
(15, 8, 14, 'logistica'),
(16, 8, 11, 'logistica'),
(17, 8, 3, 'logistica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `seguridad_bitacora`
--

CREATE TABLE `seguridad_bitacora` (
  `id` bigint(20) NOT NULL,
  `usuario` varchar(150) NOT NULL,
  `accion` varchar(30) NOT NULL,
  `tabla` varchar(50) NOT NULL,
  `objeto_id` varchar(50) NOT NULL,
  `detalle` varchar(500) NOT NULL,
  `ip` char(39) DEFAULT NULL,
  `fecha` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `seguridad_bitacora`
--

INSERT INTO `seguridad_bitacora` (`id`, `usuario`, `accion`, `tabla`, `objeto_id`, `detalle`, `ip`, `fecha`) VALUES
(1, 'admin', 'LOGOUT', '', '', '', '127.0.0.1', '2026-11-02 18:50:34.152312'),
(2, 'operador01', 'LOGIN_OK', '', '', '', '127.0.0.1', '2026-11-02 18:51:13.609012'),
(3, 'operador01', 'LOGOUT', '', '', '', '127.0.0.1', '2026-11-02 18:52:59.633110'),
(4, 'admin', 'LOGIN_OK', '', '', '', '127.0.0.1', '2026-11-02 18:53:15.861128'),
(5, 'admin', 'LOGOUT', '', '', '', '127.0.0.1', '2026-11-02 18:55:24.556072'),
(6, 'admin2', 'LOGIN_OK', '', '', '', '127.0.0.1', '2026-11-02 18:55:48.106369'),
(7, 'admin2', 'LOGOUT', '', '', '', '127.0.0.1', '2026-11-02 18:56:14.243963'),
(8, 'admin2', 'LOGIN_FALLIDO', '', '', 'Intento 1 de 3', '127.0.0.1', '2026-11-02 18:56:20.551903'),
(9, 'admin2', 'LOGIN_FALLIDO', '', '', 'Intento 2 de 3', '127.0.0.1', '2026-11-02 18:56:26.017399'),
(10, 'admin2', 'LOGIN_FALLIDO', '', '', 'Intento 3 de 3', '127.0.0.1', '2026-11-02 18:56:29.062849'),
(11, 'admin2', 'CUENTA_BLOQUEADA', '', '', 'Superó el máximo de intentos', '127.0.0.1', '2026-11-02 18:56:29.064850'),
(12, 'admin2', 'LOGIN_RECHAZADO', '', '', 'Cuenta bloqueada', '127.0.0.1', '2026-11-02 18:56:32.196815'),
(13, 'admin', 'LOGIN_OK', '', '', '', '127.0.0.1', '2026-11-02 18:57:45.670572'),
(14, 'admin', 'USUARIO_HABILITADO', 'auth_user', '5', 'Habilitó a admin2', '127.0.0.1', '2026-11-02 18:58:45.541828'),
(15, 'admin', 'CREAR', 'voluntarios', '22', 'asd asda', '127.0.0.1', '2026-11-02 19:15:30.647887'),
(16, 'admin', 'MODIFICAR', 'voluntarios', '22', 'asd asda', '127.0.0.1', '2026-11-02 19:15:54.962853'),
(17, 'admin', 'ELIMINAR', 'voluntarios', '22', 'asd asda', '127.0.0.1', '2026-11-02 19:16:13.240432'),
(18, 'admin', 'CREAR', 'voluntarios', '23', 'aaaaaaa bbbbbb', '127.0.0.1', '2026-11-02 19:17:18.138568'),
(19, 'admin', 'ELIMINAR', 'voluntarios', '23', 'aaaaaaa bbbbbb', '127.0.0.1', '2026-11-02 19:17:46.893740'),
(20, 'admin', 'LOGOUT', '', '', '', '127.0.0.1', '2026-11-02 19:25:52.891961'),
(21, 'asf', 'LOGIN_FALLIDO', '', '', 'Usuario inexistente', '127.0.0.1', '2026-11-02 19:26:02.095194'),
(22, 'asf', 'LOGIN_FALLIDO', '', '', 'Usuario inexistente', '127.0.0.1', '2026-11-02 19:26:06.637723'),
(23, 'asf', 'LOGIN_FALLIDO', '', '', 'Usuario inexistente', '127.0.0.1', '2026-11-02 19:26:09.842128'),
(24, 'asf', 'LOGIN_FALLIDO', '', '', 'Usuario inexistente', '127.0.0.1', '2026-11-02 19:26:13.201641'),
(25, 'asf', 'LOGIN_FALLIDO', '', '', 'Usuario inexistente', '127.0.0.1', '2026-11-02 19:26:19.604141'),
(26, 'UnUsuario', 'LOGOUT', '', '', '', '127.0.0.1', '2026-11-02 19:28:36.968419'),
(27, 'UnUsuario', 'LOGIN_FALLIDO', '', '', 'Intento 1 de 3', '127.0.0.1', '2026-11-02 19:28:49.685561'),
(28, 'UnUsuario', 'LOGIN_FALLIDO', '', '', 'Intento 2 de 3', '127.0.0.1', '2026-11-02 19:28:54.596981'),
(29, 'UnUsuario', 'LOGIN_FALLIDO', '', '', 'Intento 3 de 3', '127.0.0.1', '2026-11-02 19:28:57.026415'),
(30, 'UnUsuario', 'CUENTA_BLOQUEADA', '', '', 'Superó el máximo de intentos', '127.0.0.1', '2026-11-02 19:28:57.030618'),
(31, 'UnUsuario', 'LOGIN_RECHAZADO', '', '', 'Cuenta bloqueada', '127.0.0.1', '2026-11-02 19:29:00.685933'),
(32, 'UnUsuario', 'LOGIN_RECHAZADO', '', '', 'Cuenta bloqueada', '127.0.0.1', '2026-11-02 19:29:05.103391'),
(33, 'admin', 'LOGIN_OK', '', '', '', '127.0.0.1', '2026-11-02 19:29:20.901714'),
(34, 'admin2', 'LOGIN_OK', '', '', '', '192.168.1.2', '2026-11-02 19:37:02.103990'),
(35, 'admin2', 'LOGIN_OK', '', '', '', '192.168.1.2', '2026-11-02 19:37:35.230155'),
(36, 'admin2', 'LOGOUT', '', '', '', '192.168.1.2', '2026-11-02 20:11:58.568462'),
(37, 'admin', 'LOGIN_OK', '', '', '', '192.168.1.2', '2026-11-02 20:12:19.854526'),
(38, 'admin', 'LOGIN_OK', '', '', '', '192.168.1.5', '2026-11-02 20:15:10.844827'),
(39, 'admin', 'LOGIN_OK', '', '', '', '192.168.1.5', '2026-11-02 20:15:30.806438'),
(40, 'admin2', 'LOGIN_OK', '', '', '', '192.168.1.2', '2026-11-02 20:17:07.718105'),
(41, 'admin', 'LOGOUT', '', '', '', '192.168.1.5', '2026-11-02 20:18:38.866602'),
(42, 'admin2', 'LOGOUT', '', '', '', '192.168.1.2', '2026-11-02 20:21:40.015945'),
(43, 'admin2', 'LOGIN_OK', '', '', '', '192.168.1.2', '2026-11-02 20:22:01.500295'),
(44, 'admin2', 'LOGIN_OK', '', '', '', '192.168.1.2', '2026-11-02 20:22:28.350326'),
(45, 'admin', 'LOGIN_OK', '', '', '', '192.168.1.6', '2026-11-02 20:24:38.648446'),
(46, 'admin', 'LOGOUT', '', '', '', '192.168.1.2', '2026-11-02 20:27:27.991350'),
(47, 'admin', 'LOGOUT', '', '', '', '192.168.1.6', '2026-11-02 20:30:09.176465'),
(48, 'admin2', 'LOGOUT', '', '', '', '192.168.1.2', '2026-11-02 20:30:13.166799');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `seguridad_bloqueousuario`
--

CREATE TABLE `seguridad_bloqueousuario` (
  `id` bigint(20) NOT NULL,
  `intentos_fallidos` int(10) UNSIGNED NOT NULL CHECK (`intentos_fallidos` >= 0),
  `bloqueado` tinyint(1) NOT NULL,
  `fecha_bloqueo` datetime(6) DEFAULT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `seguridad_bloqueousuario`
--

INSERT INTO `seguridad_bloqueousuario` (`id`, `intentos_fallidos`, `bloqueado`, `fecha_bloqueo`, `usuario_id`) VALUES
(1, 0, 0, NULL, 5),
(2, 3, 1, '2026-11-02 19:28:57.030618', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `voluntarios`
--

CREATE TABLE `voluntarios` (
  `id_voluntario` int(11) NOT NULL,
  `ci` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `correo` varchar(255) NOT NULL,
  `telefono` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `voluntarios`
--

INSERT INTO `voluntarios` (`id_voluntario`, `ci`, `nombre`, `apellido`, `fecha_nacimiento`, `correo`, `telefono`) VALUES
(1, 11111111, 'jorge', 'rivas perez', '2010-03-21', 'jorgeRivas@hotmail.com', 76576565),
(3, 12312345, 'lucia', 'colque quispe', '2003-02-01', 'luciaColque@gmail.com', 65768688),
(5, 15151515, 'silvia', 'huanca mamani', '1978-05-20', 'silviaHuanca@gmail.com', 66968896),
(6, 14141414, 'joel', 'fernandez', '2008-11-15', 'joelFernandez@gmail.com', 78733221),
(7, 123233332, 'Alan', 'Brito', '2000-10-14', 'AlanBrito@gmail.com', 11133),
(8, 1414532, 'Juana', 'Mariela', '2001-01-11', 'JuanaMa@gmail.com', 77725326),
(9, 9251522, 'Marcos', 'Coaquira', '1998-09-12', 'Matador3000@gmail.com', 77768692),
(10, 14985247, 'Laura', 'Chambi', '2002-11-11', 'LauraLL@gmail.com', 77768256),
(11, 10002325, 'Ramon', 'Valdez', '1992-08-18', 'DonRamon@gmail.com', 66687874),
(12, 11122233, 'Ruth', 'Quispe Mamani', '2001-01-01', 'ruthQuiMa@gmail.com', 1112325),
(13, 1211454, 'Remi', 'Caja Marca', '1998-09-12', 'RemiCM@gmail.com', 66687987),
(14, 10047535, 'Diego', 'Quino Beltran', '2000-08-16', 'DiegoJavier@gmail.com', 60007898),
(15, 1552454, 'Mariela', 'Chura', '2003-01-11', 'MarielaTQ@gmail.com', 14442515),
(16, 251256, 'Juan', 'Mamani Poma', '1989-12-12', 'JuanMamani@gmail.com', 14124555),
(17, 1511332, 'Dalinar', 'Kholin', '2000-01-01', 'SeniorDalinar@gmail.com', 10101024),
(18, 256354, 'Shalland', 'Davar', '1998-04-05', 'Shalland@gmail.com', 14124425),
(19, 16161621, 'Kelsier', 'Thaidakar', '1999-10-11', 'Sobreviviente@hotmail.com', 16161102);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD PRIMARY KEY (`id_asistencia`),
  ADD KEY `id_evento` (`id_evento`),
  ADD KEY `id_voluntario` (`id_voluntario`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `eventos`
--
ALTER TABLE `eventos`
  ADD PRIMARY KEY (`id_evento`);

--
-- Indices de la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD PRIMARY KEY (`id_inscripcion`),
  ADD KEY `id_evento` (`id_evento`),
  ADD KEY `id_voluntario` (`id_voluntario`);

--
-- Indices de la tabla `seguridad_bitacora`
--
ALTER TABLE `seguridad_bitacora`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `seguridad_bloqueousuario`
--
ALTER TABLE `seguridad_bloqueousuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `voluntarios`
--
ALTER TABLE `voluntarios`
  ADD PRIMARY KEY (`id_voluntario`),
  ADD UNIQUE KEY `ci` (`ci`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD UNIQUE KEY `telefono` (`telefono`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  MODIFY `id_asistencia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `eventos`
--
ALTER TABLE `eventos`
  MODIFY `id_evento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  MODIFY `id_inscripcion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `seguridad_bitacora`
--
ALTER TABLE `seguridad_bitacora`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `seguridad_bloqueousuario`
--
ALTER TABLE `seguridad_bloqueousuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `voluntarios`
--
ALTER TABLE `voluntarios`
  MODIFY `id_voluntario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD CONSTRAINT `asistencias_ibfk_1` FOREIGN KEY (`id_evento`) REFERENCES `eventos` (`id_evento`) ON DELETE CASCADE,
  ADD CONSTRAINT `asistencias_ibfk_2` FOREIGN KEY (`id_voluntario`) REFERENCES `voluntarios` (`id_voluntario`) ON DELETE CASCADE;

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD CONSTRAINT `inscripciones_ibfk_1` FOREIGN KEY (`id_evento`) REFERENCES `eventos` (`id_evento`) ON DELETE CASCADE,
  ADD CONSTRAINT `inscripciones_ibfk_2` FOREIGN KEY (`id_voluntario`) REFERENCES `voluntarios` (`id_voluntario`) ON DELETE CASCADE;

--
-- Filtros para la tabla `seguridad_bloqueousuario`
--
ALTER TABLE `seguridad_bloqueousuario`
  ADD CONSTRAINT `seguridad_bloqueousuario_usuario_id_abb0fc44_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
