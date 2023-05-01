CREATE TABLE `reportsignals` (
  `uuid` uuid NOT NULL,
  `accountnumber` smallint(5) unsigned NOT NULL,
  `signaltimestamp` datetime NOT NULL,
  `eventdefinition` char(1),
  `fromip` inet6 DEFAULT NULL,
  `fromport` smallint(5) unsigned DEFAULT NULL,
  `receivedat` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `minutesago` smallint(5) unsigned NOT NULL,
  `rawmessage` varchar(256) NOT NULL,
  PRIMARY KEY (`uuid`),
  INDEX `idx_signaltimestamp` (`signaltimestamp`),
  INDEX `idx_accountnumber` (`accountnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `messages` (
  `index` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` uuid NOT NULL,
  `fieldtype` char(1),
  `qualifier` char(1),
  `identifier` varchar(16),
  `text` varchar(256),
  PRIMARY KEY (`index`),
  INDEX `idx_uuid` (`uuid`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
