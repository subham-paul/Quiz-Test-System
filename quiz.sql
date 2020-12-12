-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 08, 2020 at 03:35 AM
-- Server version: 5.5.20
-- PHP Version: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `quiz`
--

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `SL_NO` int(10) NOT NULL AUTO_INCREMENT,
  `Uname` varchar(50) NOT NULL,
  `F_Date` varchar(20) NOT NULL,
  `MSG` text NOT NULL,
  PRIMARY KEY (`SL_NO`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`SL_NO`, `Uname`, `F_Date`, `MSG`) VALUES
(1, 'suman.g.84@gmail.com', '2019-09-23 08:07:05', 'Very Nice.'),
(2, 'suman@aptechkolkata.com', '2020-02-08 08:48:40', 'It is a good system to check my oding skills. Thanks...');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `Uname` varchar(100) NOT NULL,
  `Pwd` varchar(8) NOT NULL,
  `Fname` text NOT NULL,
  `Mob` varchar(15) NOT NULL,
  `Status` int(2) NOT NULL,
  PRIMARY KEY (`Uname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Uname`, `Pwd`, `Fname`, `Mob`, `Status`) VALUES
('souvikd772@gmail.com', '12345', 'souvik ghosh', '7001781583', 1),
('subham2paul@gmail.com', '123456', 'Subham Paul', '6290377130', 0),
('suman.g.84@gmail.com', '2020', 'Suman Ghosh', '9051919772', 0),
('suman@aptechkolkata.com', '1234', 'Suman Ghosh', '8777703989', 1);

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE IF NOT EXISTS `question` (
  `Qno` int(3) NOT NULL AUTO_INCREMENT,
  `Sub` text NOT NULL,
  `Qstn` text NOT NULL,
  `Option1` text NOT NULL,
  `Option2` text NOT NULL,
  `Option3` text NOT NULL,
  `Option4` text NOT NULL,
  `Ans` text NOT NULL,
  `C_ANS` int(2) DEFAULT NULL,
  PRIMARY KEY (`Qno`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`Qno`, `Sub`, `Qstn`, `Option1`, `Option2`, `Option3`, `Option4`, `Ans`, `C_ANS`) VALUES
(1, 'PYTHON', '>>>"a"+"bc"', '1.a', '2.bc', '3.bca', '4.abc', 'Answer::4\r\nExplanation:: + operator is concatenation operator.', 4),
(2, 'PYTHON', '>>>What is the type of inf?', '1.Boolean', '2.Integer', '3.Float', '4.Complex', 'Answer::3.Float\r\nExplanation:: infinity is a special case of floating point numbers.It can be obtained by float("inf").', 3),
(3, 'PYTHON', '>>>What is the output  when we execute list("hello")?', '1.[''h'',''e'',''l'',''l'',''o'']', '2.[''hello'']', '3.[''llo'']', '4.[''olleh'']', 'Answer:: 1.[''h'',''e'',''l'',''l'',''o'']\r\nExplanation:: Execute in the shell to varify.', 1),
(4, 'PYTHON', '>>>Suppose list1 is [1,5,9], what is sum(list1)?', '1. 1', '2. 9', '3. 15', '4. Error', 'Answer:: 3. 15\r\nExplanation:: Sum returns the sum of all elements in the list.', 3),
(5, 'JAVA', '>>>What is the extension of java code files?', '1. .class', '2. .java', '3. .txt', '4. .js', 'Answer:: 2. .java\r\nExplanation:: java files have .java extension.', 2),
(6, 'JAVA', '>>>What is the extension of compiled java classes?', '1. .class', '2. .java', '3. .txt', '4. .js', 'Answer:: 1. .class\r\nExplanation:: The compiled java files have .class extension.', 1),
(7, 'JAVA', '>>>What is the extension of compiled java classes?', '1. .class', '2. .java', '3. .txt', '4. .js', 'Answer:: 1. .class\r\nExplanation:: The compiled java files have .class extension.', 1),
(8, 'JAVA', '>>>How many types of Acess Specifier?', '1.one type', '2.two type', '3.three type', '4.four type', 'Answer:: 4.four type\r\nExplanation:: There are four types.\r\n1.Public 2.Private 3.Protected 4.Default\r\n ', 4),
(9, 'PYTHON', '>>>Which module use for random number generation?', '1. Rand', '2. Random', '3. random', '4. ran', 'Answer:: 3. random', 3),
(10, 'C', 'Identify the wrong keyword?', '1. void', '2. volatile', '3. virtual', '4. None of these', 'Answer:: 3. virtual\r\nExplanation:: It is used in C++ only.', 3),
(11, 'C', 'How to declare a pointer?', 'int *p;', 'int &p;', 'int p;', 'None of these', 'Ans:: 1', 1),
(12, 'C', 'The symbols are used in pointer notation', '* and +', '* and &', '+ and /', 'Ans:: 2', 'None of these', 2),
(13, 'C', 'To print memory address we use', '%d', '%ld', '%u', 'None of these', 'Ans:: 3', 3),
(14, 'C', 'To declare a function pointer of:\r\nvoid add(int,int);\r\nWe use which of the following?', 'void (*fp)(int,int);', 'void *fp(int,int);', '(void *)fp(int,int);', 'None of these', 'Ans:: 1', 1),
(15, 'JAVA', 'Identify the block name we use in Exception handling', 'try', 'catch', 'finally', 'All of these', 'Ans:: 4', 4);

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE IF NOT EXISTS `result` (
  `SL_NO` int(10) NOT NULL AUTO_INCREMENT,
  `Uname` varchar(50) NOT NULL,
  `DOE` varchar(25) NOT NULL,
  `Sub` text NOT NULL,
  `C_Ans` int(3) NOT NULL,
  `Marks` int(4) NOT NULL,
  PRIMARY KEY (`SL_NO`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`SL_NO`, `Uname`, `DOE`, `Sub`, `C_Ans`, `Marks`) VALUES
(1, 'subham2paul@gmail.com', '2019-09-20 16:03:46', 'PYTHON', 4, 20),
(2, 'subham2paul@gmail.com', '2019-09-20 16:11:20', 'PYTHON', 3, 15),
(3, 'subham2paul@gmail.com', '2019-09-20 16:12:36', 'PYTHON', 2, 10),
(4, 'subham2paul@gmail.com', '2019-09-20 16:13:49', 'PYTHON', 2, 10),
(5, 'subham2paul@gmail.com', '2019-09-20 16:14:14', 'PYTHON', 1, 5),
(6, 'subham2paul@gmail.com', '2019-09-21 19:35:05', 'PYTHON', 0, 0),
(7, 'subham2paul@gmail.com', '2019-09-22 10:55:24', 'PYTHON', 0, 0),
(8, 'subham2paul@gmail.com', '2019-09-22 11:00:41', 'PYTHON', 0, 0),
(9, 'subham2paul@gmail.com', '2019-09-22 11:02:54', 'PYTHON', 2, 10),
(10, 'subham2paul@gmail.com', '2019-09-22 11:04:13', 'PYTHON', 2, 10),
(11, 'souvikd772@gmail.com', '2019-09-23 15:02:51', 'PYTHON', 1, 5),
(12, 'suman@aptechkolkata.com', '2020-02-08 08:34:17', 'PYTHON', 3, 15),
(13, 'suman@aptechkolkata.com', '2020-02-08 08:42:02', 'PYTHON', 5, 25);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
