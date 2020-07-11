-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 11, 2020 at 07:53 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `userentery`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `email`, `password`) VALUES
('admin', 'admin@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `entery`
--

CREATE TABLE `entery` (
  `uid` varchar(13) NOT NULL,
  `name` varchar(20) NOT NULL,
  `gender` varchar(7) NOT NULL,
  `yob` int(4) NOT NULL,
  `gname` varchar(20) NOT NULL,
  `co` varchar(20) NOT NULL,
  `house` varchar(100) NOT NULL,
  `street` varchar(100) NOT NULL,
  `vtc` varchar(100) NOT NULL,
  `po` varchar(100) NOT NULL,
  `dist` varchar(20) NOT NULL,
  `subdist` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pc` int(6) NOT NULL,
  `dob` varchar(11) NOT NULL,
  `date` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `entery`
--

INSERT INTO `entery` (`uid`, `name`, `gender`, `yob`, `gname`, `co`, `house`, `street`, `vtc`, `po`, `dist`, `subdist`, `state`, `pc`, `dob`, `date`) VALUES
('454354', 'njhgjh', 'jgjhgjh', 5435, 'jgjkgjhgj', 'jgjhghjghf', 'mhvnhvn', 'hhghf', 'hhjvh', 'vvhjgvngv', 'vvngvg', 'hvhvhgv', 'vgvhvn', 545465, '22/33/4444', '2020-07-11'),
('uid', 'name', 'gender', 0, 'gname', 'co', 'house', 'street', 'vtc', 'po', 'dist', 'subdist', 'state', 0, 'dob', 'today');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `entery`
--
ALTER TABLE `entery`
  ADD PRIMARY KEY (`uid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
