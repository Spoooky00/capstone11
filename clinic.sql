-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2024 at 02:20 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_management`
--

CREATE TABLE `account_management` (
  `AM_User_name` varchar(100) NOT NULL,
  `AM_Email` varchar(100) NOT NULL,
  `AM_Role` varchar(100) NOT NULL,
  `Am_ID` int(11) NOT NULL,
  `AM_Password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account_management`
--

INSERT INTO `account_management` (`AM_User_name`, `AM_Email`, `AM_Role`, `Am_ID`, `AM_Password`) VALUES
('asdasd', 'asdas@gmail.com', 'Nurse', 1, '1'),
('555656', 'qweqweqweqwe@gmail.com', 'nurseessss', 2, 'asdasdasdasdasd');

-- --------------------------------------------------------

--
-- Table structure for table `daily_logs`
--

CREATE TABLE `daily_logs` (
  `DL_ID` int(11) NOT NULL,
  `User_NFC_ID` varchar(100) NOT NULL,
  `DL_Concerm` varchar(5000) NOT NULL,
  `DL_Timein` timestamp NULL DEFAULT NULL,
  `DL_Timeout` timestamp NULL DEFAULT NULL,
  `DL_PersonInCharge` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `daily_logs`
--

INSERT INTO `daily_logs` (`DL_ID`, `User_NFC_ID`, `DL_Concerm`, `DL_Timein`, `DL_Timeout`, `DL_PersonInCharge`) VALUES
(4, '0009122165', 'maliit titi', '2024-05-15 06:35:36', '2024-05-15 08:35:36', 1),
(14, '0009158091', 'ok', '2024-05-04 15:36:00', '2024-05-09 15:36:00', 0),
(15, '0009158091', 'asdasdasd', '2024-05-01 07:04:00', '2024-05-23 07:04:00', 0),
(16, '0009122165', 'asdasda123123123', '2024-05-04 07:06:00', '2024-05-18 07:06:00', 0),
(17, '0009158091', 'masakit ulo', '2024-05-03 13:23:00', '2024-05-20 14:26:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `Item_ID` int(11) NOT NULL,
  `Item_name` varchar(100) NOT NULL,
  `Quantity` varchar(100) NOT NULL,
  `Manufacturer` varchar(100) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `Item_code` varchar(100) NOT NULL,
  `Item_expiry` date DEFAULT NULL,
  `Item_type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`Item_ID`, `Item_name`, `Quantity`, `Manufacturer`, `Description`, `Item_code`, `Item_expiry`, `Item_type`) VALUES
(1, 'Biogesic', '50565', 'Unilab', 'Gamot sa sakit sa utak', 'AA20', '2024-05-18', '50565'),
(3, 'Paracetamol', '300', 'Unilab', 'para sa sakit sa utak ', 'AA20', '2024-05-18', 'Medicine ');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Em_ID` varchar(100) NOT NULL,
  `Em_password` varchar(100) NOT NULL,
  `Em_role` varchar(100) NOT NULL,
  `Em_lastlogin` timestamp NOT NULL DEFAULT current_timestamp(),
  `Em_status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Em_ID`, `Em_password`, `Em_role`, `Em_lastlogin`, `Em_status`) VALUES
('123', 'asda', '1', '2024-05-20 02:09:07', 1);

-- --------------------------------------------------------

--
-- Table structure for table `mytable`
--

CREATE TABLE `mytable` (
  `Item Name` varchar(200) NOT NULL,
  `Quantity` varchar(200) NOT NULL,
  `Location` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `patient_permanent_records`
--

CREATE TABLE `patient_permanent_records` (
  `User_NFC_ID` varchar(100) NOT NULL,
  `PMR_Fname` varchar(100) NOT NULL,
  `PMR_Lname` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_permanent_records`
--

INSERT INTO `patient_permanent_records` (`User_NFC_ID`, `PMR_Fname`, `PMR_Lname`) VALUES
('0009122165', 'MC', 'Kulit'),
('0009158091', 'Longhair', 'Lugaw');

-- --------------------------------------------------------

--
-- Table structure for table `pmr`
--

CREATE TABLE `pmr` (
  `User_NFC_ID` varchar(100) NOT NULL,
  `PMR_Fname` varchar(100) NOT NULL,
  `PMR_Lname` varchar(100) NOT NULL,
  `PMR_Section` varchar(100) NOT NULL,
  `PMR_Yr_Lvl` varchar(100) NOT NULL,
  `PMR_DB` date DEFAULT NULL,
  `PMR_Address` varchar(100) NOT NULL,
  `PMR_Gender` varchar(100) NOT NULL,
  `PMR_BT` varchar(100) NOT NULL,
  `PMR_LUD` varchar(100) NOT NULL,
  `PMR_ECN` varchar(100) NOT NULL,
  `PMR_RTTP` varchar(100) NOT NULL,
  `PMR_ECNO` varchar(100) NOT NULL,
  `PMR_HI` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pmr`
--

INSERT INTO `pmr` (`User_NFC_ID`, `PMR_Fname`, `PMR_Lname`, `PMR_Section`, `PMR_Yr_Lvl`, `PMR_DB`, `PMR_Address`, `PMR_Gender`, `PMR_BT`, `PMR_LUD`, `PMR_ECN`, `PMR_RTTP`, `PMR_ECNO`, `PMR_HI`) VALUES
('0009158091', 'klein', 'Matapang', 'qwe', '', '2024-05-10', 'qwe', 'qwe', 'qweqwe', 'qwe', 'qwe', 'qwe', 'qwe', 'qwe'),
('qwe', 'Antoine', 'Liit', 'qweqwe', '', '2024-05-09', 'qweqwe', 'qweqwe', 'qweqwe', 'qwe', 'qwe', 'qwe', 'qwe', 'qwe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_management`
--
ALTER TABLE `account_management`
  ADD PRIMARY KEY (`Am_ID`);

--
-- Indexes for table `daily_logs`
--
ALTER TABLE `daily_logs`
  ADD PRIMARY KEY (`DL_ID`),
  ADD KEY `test` (`User_NFC_ID`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`Item_ID`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`Em_ID`);

--
-- Indexes for table `patient_permanent_records`
--
ALTER TABLE `patient_permanent_records`
  ADD PRIMARY KEY (`User_NFC_ID`);

--
-- Indexes for table `pmr`
--
ALTER TABLE `pmr`
  ADD PRIMARY KEY (`User_NFC_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_management`
--
ALTER TABLE `account_management`
  MODIFY `Am_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `daily_logs`
--
ALTER TABLE `daily_logs`
  MODIFY `DL_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `Item_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `daily_logs`
--
ALTER TABLE `daily_logs`
  ADD CONSTRAINT `daily_logs_ibfk_1` FOREIGN KEY (`USER_NFC_ID`) REFERENCES `patient_permanent_records` (`User_NFC_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `daily_logs_ibfk_2` FOREIGN KEY (`User_NFC_ID`) REFERENCES `patient_permanent_records` (`User_NFC_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
