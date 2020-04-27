-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: covid.cng0ove8fvph.us-east-1.rds.amazonaws.com    Database: covid
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `counties`
--

DROP TABLE IF EXISTS `counties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `counties` (
  `data_date` date NOT NULL,
  `county` varchar(90) NOT NULL,
  `state` varchar(90) NOT NULL,
  `fips` int(11) NOT NULL,
  `cases` int(11) NOT NULL DEFAULT '0',
  `deaths` int(11) NOT NULL DEFAULT '0',
  `cases_diff` int(11) NOT NULL DEFAULT '0',
  `deaths_diff` int(11) NOT NULL DEFAULT '0',
  `cases_per_1k` int(11) NOT NULL DEFAULT '0',
  `deaths_per_1k` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`state`,`county`,`data_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `counties_census_data`
--

DROP TABLE IF EXISTS `counties_census_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `counties_census_data` (
  `sumlev` int(11) NOT NULL DEFAULT '0',
  `state` int(11) NOT NULL DEFAULT '0',
  `county` int(11) NOT NULL DEFAULT '0',
  `state_name` varchar(90) NOT NULL DEFAULT '',
  `county_name` varchar(90) NOT NULL DEFAULT '',
  `data_year` int(11) NOT NULL DEFAULT '0',
  `agegrp` int(11) NOT NULL DEFAULT '0',
  `tot_pop` int(11) NOT NULL DEFAULT '0',
  `tot_male` int(11) NOT NULL DEFAULT '0',
  `tot_female` int(11) NOT NULL DEFAULT '0',
  `wa_male` int(11) NOT NULL DEFAULT '0',
  `wa_female` int(11) NOT NULL DEFAULT '0',
  `ba_male` int(11) NOT NULL DEFAULT '0',
  `ba_female` int(11) NOT NULL DEFAULT '0',
  `ia_male` int(11) NOT NULL DEFAULT '0',
  `ia_female` int(11) NOT NULL DEFAULT '0',
  `aa_male` int(11) NOT NULL DEFAULT '0',
  `aa_female` int(11) NOT NULL DEFAULT '0',
  `na_male` int(11) NOT NULL DEFAULT '0',
  `na_female` int(11) NOT NULL DEFAULT '0',
  `tom_male` int(11) NOT NULL DEFAULT '0',
  `tom_female` int(11) NOT NULL DEFAULT '0',
  `wac_male` int(11) NOT NULL DEFAULT '0',
  `wac_female` int(11) NOT NULL DEFAULT '0',
  `bac_male` int(11) NOT NULL DEFAULT '0',
  `bac_female` int(11) NOT NULL DEFAULT '0',
  `iac_male` int(11) NOT NULL DEFAULT '0',
  `iac_female` int(11) NOT NULL DEFAULT '0',
  `aac_male` int(11) NOT NULL DEFAULT '0',
  `aac_female` int(11) NOT NULL DEFAULT '0',
  `nac_male` int(11) NOT NULL DEFAULT '0',
  `nac_female` int(11) NOT NULL DEFAULT '0',
  `nh_male` int(11) NOT NULL DEFAULT '0',
  `nh_female` int(11) NOT NULL DEFAULT '0',
  `nhwa_male` int(11) NOT NULL DEFAULT '0',
  `nhwa_female` int(11) NOT NULL DEFAULT '0',
  `nhba_male` int(11) NOT NULL DEFAULT '0',
  `nhba_female` int(11) NOT NULL DEFAULT '0',
  `nhia_male` int(11) NOT NULL DEFAULT '0',
  `nhia_female` int(11) NOT NULL DEFAULT '0',
  `nhaa_male` int(11) NOT NULL DEFAULT '0',
  `nhaa_female` int(11) NOT NULL DEFAULT '0',
  `nhna_male` int(11) NOT NULL DEFAULT '0',
  `nhna_female` int(11) NOT NULL DEFAULT '0',
  `nhtom_male` int(11) NOT NULL DEFAULT '0',
  `nhtom_female` int(11) NOT NULL DEFAULT '0',
  `nhwac_male` int(11) NOT NULL DEFAULT '0',
  `nhwac_female` int(11) NOT NULL DEFAULT '0',
  `nhbac_male` int(11) NOT NULL DEFAULT '0',
  `nhbac_female` int(11) NOT NULL DEFAULT '0',
  `nhiac_male` int(11) NOT NULL DEFAULT '0',
  `nhiac_female` int(11) NOT NULL DEFAULT '0',
  `nhaac_male` int(11) NOT NULL DEFAULT '0',
  `nhaac_female` int(11) NOT NULL DEFAULT '0',
  `nhnac_male` int(11) NOT NULL DEFAULT '0',
  `nhnac_female` int(11) NOT NULL DEFAULT '0',
  `h_male` int(11) NOT NULL DEFAULT '0',
  `h_female` int(11) NOT NULL DEFAULT '0',
  `hwa_male` int(11) NOT NULL DEFAULT '0',
  `hwa_female` int(11) NOT NULL DEFAULT '0',
  `hba_male` int(11) NOT NULL DEFAULT '0',
  `hba_female` int(11) NOT NULL DEFAULT '0',
  `hia_male` int(11) NOT NULL DEFAULT '0',
  `hia_female` int(11) NOT NULL DEFAULT '0',
  `haa_male` int(11) NOT NULL DEFAULT '0',
  `haa_female` int(11) NOT NULL DEFAULT '0',
  `hna_male` int(11) NOT NULL DEFAULT '0',
  `hna_female` int(11) NOT NULL DEFAULT '0',
  `htom_male` int(11) NOT NULL DEFAULT '0',
  `htom_female` int(11) NOT NULL DEFAULT '0',
  `hwac_male` int(11) NOT NULL DEFAULT '0',
  `hwac_female` int(11) NOT NULL DEFAULT '0',
  `hbac_male` int(11) NOT NULL DEFAULT '0',
  `hbac_female` int(11) NOT NULL DEFAULT '0',
  `hiac_male` int(11) NOT NULL DEFAULT '0',
  `hiac_female` int(11) NOT NULL DEFAULT '0',
  `haac_male` int(11) NOT NULL DEFAULT '0',
  `haac_female` int(11) NOT NULL DEFAULT '0',
  `hnac_male` int(11) NOT NULL DEFAULT '0',
  `hnac_female` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `data_date` date NOT NULL,
  `state` varchar(90) NOT NULL,
  `fips` int(11) NOT NULL,
  `cases` int(11) NOT NULL DEFAULT '0',
  `deaths` int(11) NOT NULL DEFAULT '0',
  `cases_diff` int(11) NOT NULL DEFAULT '0',
  `deaths_diff` int(11) NOT NULL DEFAULT '0',
  `cases_per_100k` int(11) NOT NULL DEFAULT '0',
  `deaths_per_100k` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `states1`
--

DROP TABLE IF EXISTS `states1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states1` (
  `data_date` datetime NOT NULL,
  `state` varchar(90) NOT NULL,
  `fips` int(11) NOT NULL,
  `cases` int(11) NOT NULL,
  `deaths` int(11) NOT NULL,
  `load_date` date NOT NULL DEFAULT '0000-00-00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `us_counties`
--

DROP TABLE IF EXISTS `us_counties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `us_counties` (
  `state` varchar(90) NOT NULL,
  `county` varchar(90) NOT NULL,
  `fips` int(11) NOT NULL DEFAULT '0',
  `population` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`state`,`county`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `us_states`
--

DROP TABLE IF EXISTS `us_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `us_states` (
  `state` varchar(90) NOT NULL,
  `population` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`state`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `us_totals`
--

DROP TABLE IF EXISTS `us_totals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `us_totals` (
  `data_date` date NOT NULL,
  `cases` int(11) NOT NULL DEFAULT '0',
  `deaths` int(11) NOT NULL DEFAULT '0',
  `cases_diff` int(11) NOT NULL DEFAULT '0',
  `deaths_diff` int(11) NOT NULL DEFAULT '0',
  `death_rate` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`data_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `vi_counties`
--

DROP TABLE IF EXISTS `vi_counties`;
/*!50001 DROP VIEW IF EXISTS `vi_counties`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_counties` AS SELECT 
 1 AS `data_date`,
 1 AS `county`,
 1 AS `state`,
 1 AS `fips`,
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `cases_state`,
 1 AS `cases_total`,
 1 AS `deaths_state`,
 1 AS `deaths_total`,
 1 AS `cases_diff`,
 1 AS `deaths_diff`,
 1 AS `death_rate`,
 1 AS `cases_pct_state`,
 1 AS `deaths_pct_state`,
 1 AS `cases_pct_total`,
 1 AS `deaths_pct_total`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_states`
--

DROP TABLE IF EXISTS `vi_states`;
/*!50001 DROP VIEW IF EXISTS `vi_states`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_states` AS SELECT 
 1 AS `state`,
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `cases_total`,
 1 AS `deaths_total`,
 1 AS `population`,
 1 AS `data_date`,
 1 AS `cases_diff`,
 1 AS `deaths_diff`,
 1 AS `death_rate`,
 1 AS `cases_pct_total`,
 1 AS `deaths_pct_total`,
 1 AS `cases_per_100k`,
 1 AS `deaths_per_100k`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_states_base`
--

DROP TABLE IF EXISTS `vi_states_base`;
/*!50001 DROP VIEW IF EXISTS `vi_states_base`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_states_base` AS SELECT 
 1 AS `state`,
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `population`,
 1 AS `data_date`,
 1 AS `death_rate`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_totals`
--

DROP TABLE IF EXISTS `vi_totals`;
/*!50001 DROP VIEW IF EXISTS `vi_totals`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_totals` AS SELECT 
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `population`,
 1 AS `data_date`,
 1 AS `cases_pct`,
 1 AS `cases_diff`,
 1 AS `deaths_diff`,
 1 AS `death_rate`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_us_states`
--

DROP TABLE IF EXISTS `vi_us_states`;
/*!50001 DROP VIEW IF EXISTS `vi_us_states`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_us_states` AS SELECT 
 1 AS `state`,
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `data_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vi_counties`
--

/*!50001 DROP VIEW IF EXISTS `vi_counties`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_counties` AS select `c1`.`data_date` AS `data_date`,`c1`.`county` AS `county`,`c1`.`state` AS `state`,`c1`.`fips` AS `fips`,`c1`.`cases` AS `cases`,`c1`.`deaths` AS `deaths`,`s1`.`cases` AS `cases_state`,`s1`.`cases_total` AS `cases_total`,`s1`.`deaths` AS `deaths_state`,`s1`.`deaths_total` AS `deaths_total`,(`c1`.`cases` - `c3`.`cases`) AS `cases_diff`,(`c1`.`deaths` - `c3`.`deaths`) AS `deaths_diff`,(`c1`.`deaths` / `c1`.`cases`) AS `death_rate`,(`c1`.`cases` / `s1`.`cases`) AS `cases_pct_state`,(`c1`.`deaths` / `s1`.`deaths`) AS `deaths_pct_state`,(`c1`.`cases` / `s1`.`cases_total`) AS `cases_pct_total`,(`c1`.`deaths` / `s1`.`deaths_total`) AS `deaths_pct_total` from (((`counties` `c1` join (select `counties`.`state` AS `state`,`counties`.`county` AS `county`,max(`counties`.`data_date`) AS `data_date` from `counties` group by `counties`.`state`,`counties`.`county`) `c2`) join `counties` `c3`) join `vi_states` `s1`) where ((`c1`.`state` = `c2`.`state`) and (`c1`.`county` = `c2`.`county`) and (`c1`.`data_date` = `c2`.`data_date`) and (`c1`.`state` = `c3`.`state`) and (`c1`.`county` = `c3`.`county`) and (`c3`.`data_date` = (`c1`.`data_date` - interval 1 day)) and (`s1`.`state` = `c1`.`state`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_states`
--

/*!50001 DROP VIEW IF EXISTS `vi_states`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_states` AS select `s1`.`state` AS `state`,`s1`.`cases` AS `cases`,`s1`.`deaths` AS `deaths`,`t1`.`cases` AS `cases_total`,`t1`.`deaths` AS `deaths_total`,`s1`.`population` AS `population`,`s1`.`data_date` AS `data_date`,`s2`.`cases_diff` AS `cases_diff`,`s2`.`deaths_diff` AS `deaths_diff`,`s1`.`death_rate` AS `death_rate`,(`s1`.`cases` / `t1`.`cases`) AS `cases_pct_total`,(`s1`.`deaths` / `t1`.`deaths`) AS `deaths_pct_total`,`s2`.`cases_per_100k` AS `cases_per_100k`,`s2`.`deaths_per_100k` AS `deaths_per_100k` from ((`vi_states_base` `s1` join `states` `s2`) join (select sum(`vi_states_base`.`cases`) AS `cases`,sum(`vi_states_base`.`deaths`) AS `deaths` from `vi_states_base`) `t1`) where ((`s1`.`state` = `s2`.`state`) and (`s2`.`data_date` = `s1`.`data_date`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_states_base`
--

/*!50001 DROP VIEW IF EXISTS `vi_states_base`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_states_base` AS select `s1`.`state` AS `state`,`s1`.`cases` AS `cases`,`s1`.`deaths` AS `deaths`,`s2`.`population` AS `population`,`s1`.`data_date` AS `data_date`,(`s1`.`deaths` / `s1`.`cases`) AS `death_rate` from (`vi_us_states` `s1` join `us_states` `s2`) where (`s1`.`state` = `s2`.`state`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_totals`
--

/*!50001 DROP VIEW IF EXISTS `vi_totals`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_totals` AS select sum(`vi_states`.`cases`) AS `cases`,sum(`vi_states`.`deaths`) AS `deaths`,sum(`vi_states`.`population`) AS `population`,max(`vi_states`.`data_date`) AS `data_date`,(sum(`vi_states`.`cases`) / sum(`vi_states`.`population`)) AS `cases_pct`,sum(`vi_states`.`cases_diff`) AS `cases_diff`,sum(`vi_states`.`deaths_diff`) AS `deaths_diff`,(sum(`vi_states`.`deaths`) / sum(`vi_states`.`cases`)) AS `death_rate` from `vi_states` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_us_states`
--

/*!50001 DROP VIEW IF EXISTS `vi_us_states`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_us_states` AS select `states`.`state` AS `state`,max(`states`.`cases`) AS `cases`,max(`states`.`deaths`) AS `deaths`,max(`states`.`data_date`) AS `data_date` from `states` group by `states`.`state` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-19 11:57:02
-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: covid.cng0ove8fvph.us-east-1.rds.amazonaws.com    Database: covid
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `counties`
--

DROP TABLE IF EXISTS `counties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `counties` (
  `data_date` date NOT NULL,
  `county` varchar(90) NOT NULL,
  `state` varchar(90) NOT NULL,
  `fips` int(11) NOT NULL,
  `cases` int(11) NOT NULL DEFAULT '0',
  `deaths` int(11) NOT NULL DEFAULT '0',
  `cases_diff` int(11) NOT NULL DEFAULT '0',
  `deaths_diff` int(11) NOT NULL DEFAULT '0',
  `cases_per_1k` float NOT NULL DEFAULT '0',
  `deaths_per_1k` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`state`,`county`,`data_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `counties_census_data`
--

DROP TABLE IF EXISTS `counties_census_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `counties_census_data` (
  `sumlev` int(11) NOT NULL DEFAULT '0',
  `state` int(11) NOT NULL DEFAULT '0',
  `county` int(11) NOT NULL DEFAULT '0',
  `state_name` varchar(90) NOT NULL DEFAULT '',
  `county_name` varchar(90) NOT NULL DEFAULT '',
  `data_year` int(11) NOT NULL DEFAULT '0',
  `agegrp` int(11) NOT NULL DEFAULT '0',
  `tot_pop` int(11) NOT NULL DEFAULT '0',
  `tot_male` int(11) NOT NULL DEFAULT '0',
  `tot_female` int(11) NOT NULL DEFAULT '0',
  `wa_male` int(11) NOT NULL DEFAULT '0',
  `wa_female` int(11) NOT NULL DEFAULT '0',
  `ba_male` int(11) NOT NULL DEFAULT '0',
  `ba_female` int(11) NOT NULL DEFAULT '0',
  `ia_male` int(11) NOT NULL DEFAULT '0',
  `ia_female` int(11) NOT NULL DEFAULT '0',
  `aa_male` int(11) NOT NULL DEFAULT '0',
  `aa_female` int(11) NOT NULL DEFAULT '0',
  `na_male` int(11) NOT NULL DEFAULT '0',
  `na_female` int(11) NOT NULL DEFAULT '0',
  `tom_male` int(11) NOT NULL DEFAULT '0',
  `tom_female` int(11) NOT NULL DEFAULT '0',
  `wac_male` int(11) NOT NULL DEFAULT '0',
  `wac_female` int(11) NOT NULL DEFAULT '0',
  `bac_male` int(11) NOT NULL DEFAULT '0',
  `bac_female` int(11) NOT NULL DEFAULT '0',
  `iac_male` int(11) NOT NULL DEFAULT '0',
  `iac_female` int(11) NOT NULL DEFAULT '0',
  `aac_male` int(11) NOT NULL DEFAULT '0',
  `aac_female` int(11) NOT NULL DEFAULT '0',
  `nac_male` int(11) NOT NULL DEFAULT '0',
  `nac_female` int(11) NOT NULL DEFAULT '0',
  `nh_male` int(11) NOT NULL DEFAULT '0',
  `nh_female` int(11) NOT NULL DEFAULT '0',
  `nhwa_male` int(11) NOT NULL DEFAULT '0',
  `nhwa_female` int(11) NOT NULL DEFAULT '0',
  `nhba_male` int(11) NOT NULL DEFAULT '0',
  `nhba_female` int(11) NOT NULL DEFAULT '0',
  `nhia_male` int(11) NOT NULL DEFAULT '0',
  `nhia_female` int(11) NOT NULL DEFAULT '0',
  `nhaa_male` int(11) NOT NULL DEFAULT '0',
  `nhaa_female` int(11) NOT NULL DEFAULT '0',
  `nhna_male` int(11) NOT NULL DEFAULT '0',
  `nhna_female` int(11) NOT NULL DEFAULT '0',
  `nhtom_male` int(11) NOT NULL DEFAULT '0',
  `nhtom_female` int(11) NOT NULL DEFAULT '0',
  `nhwac_male` int(11) NOT NULL DEFAULT '0',
  `nhwac_female` int(11) NOT NULL DEFAULT '0',
  `nhbac_male` int(11) NOT NULL DEFAULT '0',
  `nhbac_female` int(11) NOT NULL DEFAULT '0',
  `nhiac_male` int(11) NOT NULL DEFAULT '0',
  `nhiac_female` int(11) NOT NULL DEFAULT '0',
  `nhaac_male` int(11) NOT NULL DEFAULT '0',
  `nhaac_female` int(11) NOT NULL DEFAULT '0',
  `nhnac_male` int(11) NOT NULL DEFAULT '0',
  `nhnac_female` int(11) NOT NULL DEFAULT '0',
  `h_male` int(11) NOT NULL DEFAULT '0',
  `h_female` int(11) NOT NULL DEFAULT '0',
  `hwa_male` int(11) NOT NULL DEFAULT '0',
  `hwa_female` int(11) NOT NULL DEFAULT '0',
  `hba_male` int(11) NOT NULL DEFAULT '0',
  `hba_female` int(11) NOT NULL DEFAULT '0',
  `hia_male` int(11) NOT NULL DEFAULT '0',
  `hia_female` int(11) NOT NULL DEFAULT '0',
  `haa_male` int(11) NOT NULL DEFAULT '0',
  `haa_female` int(11) NOT NULL DEFAULT '0',
  `hna_male` int(11) NOT NULL DEFAULT '0',
  `hna_female` int(11) NOT NULL DEFAULT '0',
  `htom_male` int(11) NOT NULL DEFAULT '0',
  `htom_female` int(11) NOT NULL DEFAULT '0',
  `hwac_male` int(11) NOT NULL DEFAULT '0',
  `hwac_female` int(11) NOT NULL DEFAULT '0',
  `hbac_male` int(11) NOT NULL DEFAULT '0',
  `hbac_female` int(11) NOT NULL DEFAULT '0',
  `hiac_male` int(11) NOT NULL DEFAULT '0',
  `hiac_female` int(11) NOT NULL DEFAULT '0',
  `haac_male` int(11) NOT NULL DEFAULT '0',
  `haac_female` int(11) NOT NULL DEFAULT '0',
  `hnac_male` int(11) NOT NULL DEFAULT '0',
  `hnac_female` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `data_date` date NOT NULL,
  `state` varchar(90) NOT NULL,
  `fips` int(11) NOT NULL,
  `cases` int(11) NOT NULL DEFAULT '0',
  `deaths` int(11) NOT NULL DEFAULT '0',
  `cases_diff` int(11) NOT NULL DEFAULT '0',
  `deaths_diff` int(11) NOT NULL DEFAULT '0',
  `cases_per_100k` float NOT NULL DEFAULT '0',
  `deaths_per_100k` float NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `states1`
--

DROP TABLE IF EXISTS `states1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states1` (
  `data_date` datetime NOT NULL,
  `state` varchar(90) NOT NULL,
  `fips` int(11) NOT NULL,
  `cases` int(11) NOT NULL,
  `deaths` int(11) NOT NULL,
  `load_date` date NOT NULL DEFAULT '0000-00-00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `us_counties`
--

DROP TABLE IF EXISTS `us_counties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `us_counties` (
  `state` varchar(90) NOT NULL,
  `county` varchar(90) NOT NULL,
  `fips` int(11) NOT NULL DEFAULT '0',
  `population` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`state`,`county`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `us_states`
--

DROP TABLE IF EXISTS `us_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `us_states` (
  `state` varchar(90) NOT NULL,
  `population` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`state`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `us_totals`
--

DROP TABLE IF EXISTS `us_totals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `us_totals` (
  `data_date` date NOT NULL,
  `cases` int(11) NOT NULL DEFAULT '0',
  `deaths` int(11) NOT NULL DEFAULT '0',
  `cases_diff` int(11) NOT NULL DEFAULT '0',
  `deaths_diff` int(11) NOT NULL DEFAULT '0',
  `death_rate` float NOT NULL DEFAULT '0',
  `population` int(11) NOT NULL DEFAULT '331819637',
  `cases_per_1m` float NOT NULL DEFAULT '0',
  `deaths_per_1m` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`data_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `vi_counties`
--

DROP TABLE IF EXISTS `vi_counties`;
/*!50001 DROP VIEW IF EXISTS `vi_counties`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_counties` AS SELECT 
 1 AS `data_date`,
 1 AS `county`,
 1 AS `state`,
 1 AS `fips`,
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `cases_state`,
 1 AS `cases_total`,
 1 AS `deaths_state`,
 1 AS `deaths_total`,
 1 AS `cases_diff`,
 1 AS `deaths_diff`,
 1 AS `death_rate`,
 1 AS `cases_pct_state`,
 1 AS `deaths_pct_state`,
 1 AS `cases_pct_total`,
 1 AS `deaths_pct_total`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_states`
--

DROP TABLE IF EXISTS `vi_states`;
/*!50001 DROP VIEW IF EXISTS `vi_states`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_states` AS SELECT 
 1 AS `state`,
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `cases_total`,
 1 AS `deaths_total`,
 1 AS `population`,
 1 AS `data_date`,
 1 AS `cases_diff`,
 1 AS `deaths_diff`,
 1 AS `death_rate`,
 1 AS `cases_pct_total`,
 1 AS `deaths_pct_total`,
 1 AS `cases_per_100k`,
 1 AS `deaths_per_100k`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_states_base`
--

DROP TABLE IF EXISTS `vi_states_base`;
/*!50001 DROP VIEW IF EXISTS `vi_states_base`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_states_base` AS SELECT 
 1 AS `state`,
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `population`,
 1 AS `data_date`,
 1 AS `death_rate`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_totals`
--

DROP TABLE IF EXISTS `vi_totals`;
/*!50001 DROP VIEW IF EXISTS `vi_totals`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_totals` AS SELECT 
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `population`,
 1 AS `data_date`,
 1 AS `cases_pct`,
 1 AS `cases_diff`,
 1 AS `deaths_diff`,
 1 AS `death_rate`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_us_states`
--

DROP TABLE IF EXISTS `vi_us_states`;
/*!50001 DROP VIEW IF EXISTS `vi_us_states`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_us_states` AS SELECT 
 1 AS `state`,
 1 AS `cases`,
 1 AS `deaths`,
 1 AS `data_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vi_counties`
--

/*!50001 DROP VIEW IF EXISTS `vi_counties`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_counties` AS select `c1`.`data_date` AS `data_date`,`c1`.`county` AS `county`,`c1`.`state` AS `state`,`c1`.`fips` AS `fips`,`c1`.`cases` AS `cases`,`c1`.`deaths` AS `deaths`,`s1`.`cases` AS `cases_state`,`s1`.`cases_total` AS `cases_total`,`s1`.`deaths` AS `deaths_state`,`s1`.`deaths_total` AS `deaths_total`,(`c1`.`cases` - `c3`.`cases`) AS `cases_diff`,(`c1`.`deaths` - `c3`.`deaths`) AS `deaths_diff`,(`c1`.`deaths` / `c1`.`cases`) AS `death_rate`,(`c1`.`cases` / `s1`.`cases`) AS `cases_pct_state`,(`c1`.`deaths` / `s1`.`deaths`) AS `deaths_pct_state`,(`c1`.`cases` / `s1`.`cases_total`) AS `cases_pct_total`,(`c1`.`deaths` / `s1`.`deaths_total`) AS `deaths_pct_total` from (((`counties` `c1` join (select `counties`.`state` AS `state`,`counties`.`county` AS `county`,max(`counties`.`data_date`) AS `data_date` from `counties` group by `counties`.`state`,`counties`.`county`) `c2`) join `counties` `c3`) join `vi_states` `s1`) where ((`c1`.`state` = `c2`.`state`) and (`c1`.`county` = `c2`.`county`) and (`c1`.`data_date` = `c2`.`data_date`) and (`c1`.`state` = `c3`.`state`) and (`c1`.`county` = `c3`.`county`) and (`c3`.`data_date` = (`c1`.`data_date` - interval 1 day)) and (`s1`.`state` = `c1`.`state`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_states`
--

/*!50001 DROP VIEW IF EXISTS `vi_states`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_states` AS select `s1`.`state` AS `state`,`s1`.`cases` AS `cases`,`s1`.`deaths` AS `deaths`,`t1`.`cases` AS `cases_total`,`t1`.`deaths` AS `deaths_total`,`s1`.`population` AS `population`,`s1`.`data_date` AS `data_date`,`s2`.`cases_diff` AS `cases_diff`,`s2`.`deaths_diff` AS `deaths_diff`,`s1`.`death_rate` AS `death_rate`,(`s1`.`cases` / `t1`.`cases`) AS `cases_pct_total`,(`s1`.`deaths` / `t1`.`deaths`) AS `deaths_pct_total`,`s2`.`cases_per_100k` AS `cases_per_100k`,`s2`.`deaths_per_100k` AS `deaths_per_100k` from ((`vi_states_base` `s1` join `states` `s2`) join (select sum(`vi_states_base`.`cases`) AS `cases`,sum(`vi_states_base`.`deaths`) AS `deaths` from `vi_states_base`) `t1`) where ((`s1`.`state` = `s2`.`state`) and (`s2`.`data_date` = `s1`.`data_date`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_states_base`
--

/*!50001 DROP VIEW IF EXISTS `vi_states_base`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_states_base` AS select `s1`.`state` AS `state`,`s1`.`cases` AS `cases`,`s1`.`deaths` AS `deaths`,`s2`.`population` AS `population`,`s1`.`data_date` AS `data_date`,(`s1`.`deaths` / `s1`.`cases`) AS `death_rate` from (`vi_us_states` `s1` join `us_states` `s2`) where (`s1`.`state` = `s2`.`state`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_totals`
--

/*!50001 DROP VIEW IF EXISTS `vi_totals`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_totals` AS select sum(`vi_states`.`cases`) AS `cases`,sum(`vi_states`.`deaths`) AS `deaths`,sum(`vi_states`.`population`) AS `population`,max(`vi_states`.`data_date`) AS `data_date`,(sum(`vi_states`.`cases`) / sum(`vi_states`.`population`)) AS `cases_pct`,sum(`vi_states`.`cases_diff`) AS `cases_diff`,sum(`vi_states`.`deaths_diff`) AS `deaths_diff`,(sum(`vi_states`.`deaths`) / sum(`vi_states`.`cases`)) AS `death_rate` from `vi_states` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_us_states`
--

/*!50001 DROP VIEW IF EXISTS `vi_us_states`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`admin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_us_states` AS select `states`.`state` AS `state`,max(`states`.`cases`) AS `cases`,max(`states`.`deaths`) AS `deaths`,max(`states`.`data_date`) AS `data_date` from `states` group by `states`.`state` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-19 12:29:54
