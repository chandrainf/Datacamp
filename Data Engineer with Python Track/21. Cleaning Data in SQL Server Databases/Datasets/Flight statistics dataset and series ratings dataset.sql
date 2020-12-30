CREATE DATABASE CleaningData;
GO
USE CleaningData;
GO

DROP TABLE IF EXISTS series;
GO
CREATE TABLE series (
    id int IDENTITY(1,1) PRIMARY KEY,
	name varchar(max) NULL,
	premiered date NULL,
	official_site varchar(max) NULL,
	contact_number varchar(12) NULL,
	rating FLOAT NULL,
	num_ratings INT NOT NULL,
	is_adult BIT NOT NULL,
	min_age INT NOT NULL,
	summary varchar(max) NULL);
GO


DROP TABLE IF EXISTS episodes;
GO
CREATE TABLE episodes (
    episode_id int IDENTITY(1,1) PRIMARY KEY,
	series_id varchar(10) NULL,
	name varchar(500) NULL,
	season int NULL,
	number varchar(5) NULL,
	airdate date,
	runtime int NULL);
GO

INSERT INTO series VALUES
('Adventure Time', '2010/04/05', 'wwq.cartoonnetwork.com/video/adventuretime/', '555-906-8845', 8.4, 5200, 0, 10, 'Adventure Time''s unlikely heroes Finn and Jake are buddies who traverse the mystical Land of Ooo and encounter its colorful inhabitants.'),
('Dexter', '2006/01/10', 'ww.sho.com/sho/dexter/home', '555-156-8845', 8.6, 4036, 1, 16, 'Dexter is a crime drama series based around the main character, a serial killer named Dexter Morgan. Dexter only kills other killers and criminals and works in blood splatter analysis at crime scenes.'),
('Futurama', '1999/03/28', 'www.cc.com/shows/futurama', '555-210-9951', 9.2, 5012, 0, 13, 'Futurama follows pizza guy Philip J. Fry, who reawakens in 31st century New New York after a cryonics lab accident. Now part of the Planet Express delivery crew, Fry travels to the farthest reaches of the universe with his robot buddy Bender and cyclopsian love interest Leela, discovering freaky mutants, intergalactic conspiracies and other strange stuff.'),
('Game of Thrones', '2011/04/17', 'www.hbo.com/game-of-thrones', '555-abc-6641', 9.3, 2590, 1, 14, 'Based on the bestselling book series A Song of Ice and Fire by George R.R. Martin, this sprawling new HBO drama is set in a world where summers span decades and winters can last a lifetime. From the scheming south and the savage eastern lands, to the frozen north and ancient Wall that protects the realm from the mysterious darkness beyond, the powerful families of the Seven Kingdoms are locked in a battle for the Iron Throne. This is a story of duplicity and treachery, nobility and honor, conquest and triumph. In the Game of Thrones, you either win or you die.'),
('Homeland', '2011/10/02', 'www.sho.com/sho/homeland/home', '555-985-6314', 8.3, 4102, 0, 17, 'The winner of 6 Emmy Awards including Outstanding Drama Series, Homeland is an edge-of-your-seat sensation. Marine Sergeant Nicholas Brody is both a decorated hero and a serious threat. CIA officer Carrie Mathison is tops in her field despite being bipolar. The delicate dance these two complex characters perform, built on lies, suspicion, and desire, is at the heart of this gripping, emotional thriller in which nothing short of the fate of our nation is at stake.'),
('Westworld', '2016/10/02', 'www.hbo.com/westworld', '555-456-1234', 8.6, 4120, 1, 18, 'Westworld is a dark odyssey about the dawn of artificial consciousness and the evolution of sin. Set at the intersection of the near future and the reimagined past, it explores a world in which every human appetite, no matter how noble or depraved, can be indulged.'),
('Silicon Valley', '2014/04/06', 'www.hbo.com/silicon-valley/', '555-604-1234', 11.4, 3012, 0, 16, 'In the high-tech gold rush of modern Silicon Valley, the people most qualified to succeed are the least capable of handling success. From Mike Judge comes this satire about a programmer whose game-changing algorithm becomes the subject of a valley-wide bidding war.'),
('The Big Bang Theory', '2007/09/24', 'www.cbs.com/shows/big_bang_theory/', '555-607-1274', 8, 1504, 0, 14, 'The Big Bang Theory is a comedy about brilliant physicists, Leonard and Sheldon, who are the kind of \"beautiful minds\" that understand how the universe works. But none of that genius helps them interact with people, especially women. All this begins to change when a free-spirited beauty named Penny moves in next door. Sheldon, Leonard''s roommate, is quite content spending his nights playing Klingon Boggle with their socially dysfunctional friends, fellow Cal Tech scientists Wolowitz and Koothrappali. However, Leonard sees in Penny a whole new universe of possibilities... including love.'),
('Paw Patrol', '2013/08/27', 'www.nickjr.com/paw-patrol/videos/', '555-930-1274', 11, 3104, 0, 3, 'Paw Patrol stars a pack of six heroic rescue pups - Chase, Marshall, Rocky, Rubble, Zuma and Skye - who are led by a tech-savvy boy named Ryder. Together they work hard to protect the Adventure Bay community believing, \"no job is too big, no pup is too small!\" The series features a curriculum that focuses on citizenship, social skills and problem-solving.'),
('The Good Doctor', '2017/09/25', 'www.abc.go.com/shows/the-good-doctor', '000-930-1274', 7.8, -1, 0, 14, 'Shaun Murphy, a young surgeon with autism and savant syndrome, relocates from a quiet country life to join a prestigious hospital''s surgical unit. Alone in the world and unable to personally connect with those around him, Shaun uses his extraordinary medical gifts to save lives and challenge the skepticism of his colleagues.'),
('Black Mirror', '2011/11/04', 'www.netflix.com/title/70264888', '555-401-4522', 8.8, 1250, 1, 18, 'Over the last ten years, technology has transformed almost every aspect of our lives before we''ve had time to stop and question it. In every home; on every desk; in every palm - a plasma screen; a monitor; a smartphone--a black mirror of our 21st Century existence. Black Mirror is a contemporary British re-working of The Twilight Zone with stories that tap into the collective unease about our modern world.'),
('Better Call Saul', '2015/02/18', 'www.amc.com/shows/better-call-saul', '555-744-8014', 8.7, 4874, 0, 16, 'Better Call Saul is the prequel to the award-winning series Breaking Bad, set six years before Saul Goodman became Walter White''s lawyer. When we meet him, the man who will become Saul Goodman is known as Jimmy McGill, a small-time lawyer searching for his destiny, and, more immediately, hustling to make ends meet.'),
('Breaking Bad', '2008/01/20', 'www.amc.com/shows/breaking-bad', '555-123-3210', 9.3, 1501, 0, 14, 'Breaking Bad follows protagonist Walter White, a chemistry teacher who lives in New Mexico with his wife and teenage son who has cerebral palsy.')

INSERT INTO episodes VALUES
(1, 'Slumber Party Panic', 1, 1, '2010-04-05', 15),
(1, 'Trouble in Lumpy Space', 1, 2, '2010-04-05', 15),
(1, 'Prisoners of Love', 1, 3, '2010-04-12', 15),
(1, 'Tree Trunks', 1, 4, '2010-04-12', 15),
(1, 'The Enchiridion!', 1, 5, '2010-04-19', 15),
(1, 'The Jiggler', 1, 6, '2010-04-19',  15),
(1, 'Ricardio the Heart Guy', 1, 7, '2010-04-26', 15),
(1, 'Business Time', 1, 8, '2010-04-26', 15),
(1, 'My Two Favorite People', 1, 9, '2010-05-03', 15),
(1, 'Memories of Boom Boom Mountain', 1, 10, '2010-05-03', 15),
(1, 'Finn the Wizard', 1, 11, '2010-05-10', 15),
(1, 'Evicted!', 1, 12, '2010-05-17', 15),
(1, 'City of Thieves', 1, 13, '2010-05-24', 15),
(1, 'The Witch''s Garden', 1, 14, '2010-06-07', 15),
(1, 'What is Life?', 1, 15, '2010-06-14', 15),
(1, 'Ocean of Fear', 1, 16, '2010-06-21', 15),
(1, 'When Wedding Bells Thaw', 1, 17, '2010-06-28', 15),
(1, 'Dungeon', 1, 18, '2010-07-12', 15),
(1, 'The Duke', 1, 19, '2010-07-19', 15),
(1, 'Freak City', 1, 20, '2010-07-26', 15),
(1, 'Donny', 1, 21, '2010-08-09', 15),
(1, 'Henchman', 1, 22, '2010-08-23', 15),
(1, 'Rainy Day Daydream', 1, 23, '2010-09-06', 15),
(1, 'What Have You Done?', 1, 24, '2010-09-13', 15),
(1, 'Finn Meets His Hero', 1, 25, '2010-09-20', 15),
(1, 'The Gut Grinder', 1, 26, '2010-09-27', 15),
(2, 'Dexter', 1, 1, '2006-10-01', 60),
(2, 'Crocodile', 1, 2, '2006-10-08', 60),
(2, 'Popping Cherry', 1, 3, '2006-10-15', 60),
(2, 'Let''s Give the Boy a Hand', 1, 4, '2010-04-12', 60),
(2, 'Love American Style', 1, 5, '2006-10-29', 60),
(2, 'Return to Sender', 1, 6, '2006-11-05',  60),
(2, 'Circle of Friends', 1, 7, '2006-11-12', 60),
(2, 'Shrink Wrap', 1, 8, '2006-11-19', 60),
(2, 'Father Knows Best', 1, 9, '2006-12-03', 60),
(2, 'Seeing Red', 1, 10, '2010-05-03', 60),
(2, 'Truth Be Told', 1, 11, '2006-12-10', 60),
(2, 'Born Free', 1, 12, '2006-12-17', 60),
(3, 'Space Pilot 3000', 1, 1, '1999-03-28', 30),
(3, 'The Series Has Landed', 1, 2, '1999-04-04', 30),
(3, 'I, Roommate', 1, 3, '1999-04-06', 30),
(3, 'Love''s Labors Lost in Space', 1, 4, '1999-04-13', 30),
(3, 'Fear of a Bot Planet', 1, 5, '1999-04-20', 30),
(3, 'A Fishful of Dollars', 1, 6, '1999-04-27',  30),
(3, 'My Three Suns', 1, 7, '1999-05-04', 30),
(3, 'A Big Piece of Garbage', 1, 8, '1999-05-11', 30),
(3, 'Hell Is Other Robots', 1, 9, '1999-05-18', 30),
(4, 'Winter is Coming', 1, 1, '2011-04-17', 60),
(4, 'The Kingsroad', 1, 2, '2011-04-24', 60),
(4, 'Lord Snow', 1, 3, '2011-05-01', 60),
(4, 'Cripples, Bastards, and Broken Things', 1, 4, '2011-05-08', 60),
(4, 'The Wolf and the Lion', 1, 5, '2011-05-15', 60),
(4, 'A Golden Crown', 1, 6, '2011-05-22',  60),
(4, 'You Win or You Die', 1, 7, '2011-05-29', 60),
(4, 'The Pointy End', 1, 8, '2011-06-05', 60),
(4, 'Baelor', 1, 9, '2011-06-12', 60),
(4, 'Fire and Blood', 1, 10, '2011-06-19', 60),
(5, 'Pilot', 1, 1, '2010-10-02', 60),
(5, 'Grace', 1, 2, '2011-10-09', 60),
(5, 'Clean Skin', 1, 3, '2011-10-16', 60),
(5, 'Semper I"', 1, 4, '2011-10-23', 60),
(5, 'Blind Spot', 1, 5, '2011-10-30', 60),
(5, 'The Good Soldier', 1, 6, '2011-10-30',  60),
(5, 'The Weekend', 1, 7, '2011-11-13', 60),
(5, 'Achilles Heel', 1, 8, '2011-11-20', 60),
(5, 'Crossfire', 1, 9, '2011-11-27', 60),
(5, 'Representative Brody', 1, 10, '2011-12-04', 60),
(5, 'The Vest', 1, 11, '2011-12-11', 60),
(5, 'Marine One', 1, 12, '2011-12-18', 60),
(6, 'The Original', 1, 1, '2015-10-02', 68),
(6, 'Chestnut', 1, 2, '2016-10-09', 60),
(6, 'The Stray', 1, 3, '2016-10-16', 60),
(6, 'Dissonance Theory', 1, 4, '2016-10-23', 60),
(6, 'Contrapasso', 1, 5, '2015-10-30', 60),
(6, 'The Adversary', 1, 6, '2016-11-06',  60),
(6, 'Trompe L''Oeil', 1, 7, '2016-11-13', 60),
(6, 'Trace Decay', 1, 8, '2016-11-20', 60),
(6, 'The Well-Tempered Clavier', 1, 9, '2016-11-27', 60),
(6, 'The Bicameral Mind', 1, 10, '2016-12-04', 90)

DROP TABLE IF EXISTS airports;
GO

CREATE TABLE airports(
	airport_code varchar(10) NULL,
	airport_name varchar(70) NULL,
	airport_city varchar(20) NULL,
	airport_state varchar(20) NULL);
GO

DROP TABLE IF EXISTS carriers;
GO

CREATE TABLE carriers(
	code nchar(100) NULL,
	name nchar(100) NULL);
GO

DROP TABLE IF EXISTS flight_statistics;
GO

CREATE TABLE flight_statistics(
    registration_code varchar(9) not null,
	airport_code varchar(10) NULL,
	carrier_code varchar(10) NULL,
	canceled int NULL,
	on_time int NULL,
	delayed int NULL,
	diverted int NULL,
	statistician_name nvarchar(500) NULL,
	statistician_surname nvarchar(500) NULL,
	registration_date varchar(10) NULL);
GO

DROP TABLE IF EXISTS pilots;
GO

CREATE TABLE pilots(
    pilot_code int IDENTITY(1,1) PRIMARY KEY,
	pilot_name nvarchar(500) NULL,
	pilot_surname nvarchar(500) NULL,
	carrier_code char(2) NULL,
	entry_date varchar(10) NULL);
GO


INSERT INTO pilots VALUES
('Thomas', 'Peters', 'HA', '2011-10-01'),
('Hiroki', 'Konoe', 'MQ', '2011-01-21'),
('Arturo', 'Montero', 'UA',	'2012-12-28'),
('David', 'Captain', 'US', '2000-10-01'),
('Ainhoa', 'Guerrera', 'VX', '2000-10-05'),
('Alvin', 'Andersen', 'OO',	'2012-01-15'),
('William', 'Champy', 'F9',	'2011-03-15')


INSERT INTO airports VALUES
('MSP', ' Minneapolis-St Paul International   ', 'Minneapolis', 'Minnesota'),
('JFK', ' John F. Kennedy International', 'New York City', 'New York'),
('LAX', ' Los Angeles International', 'Los Angeles', 'California'),
('DFW', '      Dallas/Fort Worth International', 'Dallas/Fort Worth', 'Texas'),
('BOS', 'Logan International    ', 'Boston', 'Massachusetts'),
('SFO', ' San Francisco International ', 'San Francisco', 'Californiaa'),
('ATL', ' Hartsfield-Jackson Atlanta International   ', 'Atlanta', 'Georgia'),
('LGA', ' LaGuardia', 'nyc', 'New York'),
('DTW', ' Detroit Metro Wayne County', 'Detroit', 'Michigan'),
('SAN', ' San Diego International   ', 'San Diego', 'Caalifornia'),
('IAH', 'George Bush Intercontinental/Houston', 'Houston', 'Tejas'),
('LAS', 'McCarran International', 'Las Vegas', 'Nevada'),
('ORD', '    Chicago O''Hare International', 'ch', 'Illinois'),
('MDW', '    Chicago Midway International', 'Chicago', 'Ilynois'),
('PDX', '    Portland International    ', 'Portland', 'Oregon'),
('MIA', 'Miami International', 'Miami', 'fl'),
('PHX', '    Phoenix Sky Harbor International', 'Phoenix', 'Arizona'),
('DEN', '    Denver International', 'Denver', 'Colorado'),
('BWI', '    Baltimore/Washington International Thurgood Marshall', 'Baltimore', 'Maryland'),
('EWR', '    Newark Liberty International', 'Newark', 'New Jersey'),
('SEA', 'Seattle/Tacoma International', NULL, NULL),
('PHL', 'Philadelphia International', 'Philadelphia', NULL),
('SLC', 'Salt Lake City International', NULL, 'Utah'),
('MCO', 'Orlando International', 'Orlando', 'Florida'),
('TPA', 'Tampa International', 'Tampa', 'Fl'),
('FLL', 'Fort Lauderdale-Hollywood International', 'Fort Lauderdale', 'FL'),
('CLT', 'Charlotte Douglas International', 'Charlotte', 'North Carolina')


INSERT INTO carriers VALUES
('YV', 'Mesa Airlines Inc.     '),
('AA', '   American Airlines Inc .   '),
('B6', '   JetBlue Airways'),
('DL', '   Delta Air Lines Inc.'),
('HA', '   Hawaiian Airlines Inc. '),
('MQ', '   American Eagle Airlines Inc.    '),
('EV', ' ExpressJet Airlines Inc.'),
('UA', ' United Air Lines Inc.   '),
('US', ' US Airways Inc.'),
('VX', ' Virgin America '),
('FL', 'AirTran Airways Corporation'),
('OO', 'SkyWest Airlines Inc.'),
('F9', 'Frontier Airlines Inc.'),
('WN', 'Southwest Airlines Co.'),
('AS', 'Alaska Airlines Inc.'),
('NK', 'Spirit Air Lines')


INSERT INTO flight_statistics VALUES
('000000119','JFK', 'AA', 74, 819, 233, 13, 'Miriam', 'Smith', '2014-01-31'),
('120','JFK', 'B6', 438, 1865, 1010, 29, 'Myriam', 'Smith', '2014-01-31'),
('000000121','JFK', 'HA', NULL, NULL, NULL, NULL, 'Mirian', 'Smyht', '2014-01-31'),
('122','JFK', 'MQ', NULL, NULL, NULL, NULL, 'Miriam', 'Smyth', '2014-01-31'),
('123','JFK', 'EV', NULL, NULL, NULL, NULL, 'Astrid', 'Harper', '2014-01-31'),
('000000124','JFK', 'UA', 22, 296, 88, 4, 'Dylan', 'Brown', '2014-01-31'),
('000000125','JFK', 'US', 15, 191, 63, 1, 'Dylan', 'Brown', '2014-01-31'),
('000000126','JFK', 'VX', 12, 225, 61, 3, 'Bryan', 'Page', '2014-01-31'),
('000000127','JFK', 'AA', 59, 764, 212, 14, 'Brian', 'Page', '2014-02-28'),
('000000128','JFK', 'B6', 181, 2089, 831, 16, 'Carol', 'York', '2014-02-28'),
('000000129','JFK', 'EV', 18, 63, 23, 0, 'Carol', 'York', '2014-02-28'),
('000000130','JFK', 'HA', NULL, NULL, NULL, NULL, 'Anne', 'Johnson', '2014-02-28'),
('000000131','JFK', 'EV', 18, 63, 23, 0, 'Anne', 'Johnson', '2014-02-28'),
('000000132','MSP', 'YV', 0, 6, 1, 0, 'Michael', 'Andersen', '2013-12-01'),
('000000133','MSP', 'AA', 15, 194, 89, 0, 'Peter', 'Johnson', '2014-01-01'),
('000000134','MSP', 'DL', 61, 3148, 925, 4, 'Anne', 'Johnson', '2014-01-01'),
('000000135','MSP', 'AS', 0, 58, 4, 0, 'Anne', 'Johnson', '2014-01-01'),
('000000136','MSP', 'DL', 61, 3148, 925, 4, 'Bernard', 'Ross', '2014-01-01'),
('000000137','MSP', 'EV', 117, 369, 223, 3, 'Michael', 'Andersen', '2014-01-01'),
('000000138','MSP', 'F9', 0, 60, 36, 0, 'Anne', 'Johnson', '2014-01-01'),
('000000139','MSP', 'FL', 8, 83, 29, 0, 'Anne', 'Johnson', '2014-01-01'),
('000000140','MSP', 'MQ', 20, 67, 24, 0, 'Anne', 'Johnson', '2014-01-01'),
('000000141','MSP', 'OO', 76, 1031, 323, 1, 'Anne', 'Johnson', '2014-01-01'),
('000000142','MSP', 'OO', 76, 1031, 323, 1, 'Anne', 'Johnson', '2014-01-01'),
('000000143','MSP', 'OO', 76, 1031, 323, 1, 'Anne', 'Johnson', '2014-01-01')




DROP TABLE IF EXISTS vendors;
GO

DROP TABLE IF EXISTS clients;
GO

DROP TABLE IF EXISTS paper_shop_daily_sales;
GO

DROP TABLE IF EXISTS paper_shop_monthly_sales;
GO

DROP TABLE IF EXISTS clients_split;
GO

CREATE TABLE vendors(
    vendor_id int IDENTITY(1,1) PRIMARY KEY,
	vendor_name varchar(500) NULL,
	vendor_surname varchar(500) NULL);
GO

CREATE TABLE clients(
	client_id int IDENTITY(1,1) PRIMARY KEY,
	client_name varchar(500) NULL,
	client_surname varchar(500) NULL,
	city varchar(500) NULL,
	state varchar(500) NULL);
GO

CREATE TABLE clients_split(
	client_id int IDENTITY(1,1) PRIMARY KEY,
	client_name varchar(500) NULL,
	client_surname varchar(500) NULL,
	city_state varchar(500) NULL);
GO

CREATE TABLE paper_shop_daily_sales(
	product_name varchar(100) NULL,
	units int NOT NULL,
	year_of_sale varchar(100) NULL,
	month_of_sale varchar(100) NULL,
	day_of_sale varchar(100) NULL,
	vendor_id int NOT NULL,
	client_id int NOT NULL);
GO

CREATE TABLE paper_shop_monthly_sales(
	product_name_units varchar(100) NULL,
	year_of_sale int null,
	month_of_sale int NULL,
	day_of_sale int NULL);
GO

INSERT INTO vendors VALUES
('Eric', 'Mendoza'),   
('Wu', 'Fengmian'),          
('Jaime', 'Furtado'),
('Carol', NULL);

INSERT INTO clients VALUES
('Miriam', 'Antona', 'Las Vegas', 'Nevada'),   
('Astrid', 'Harper', 'Chicago', 'Illinois'),          
('David', 'Madden', 'Phoenix', 'Arizona'),
('Hiroki', 'Konoe', 'Orlando', NULL);

INSERT INTO clients_split VALUES
('Miriam', 'Antona', 'Las Vegas, Nevada'),   
('Astrid', 'Harper', 'Chicago, Illinois'),          
('David', 'Madden', 'Phoenix, Arizona'),
('Hiroki', 'Konoe', 'Orlando, Florida');

INSERT INTO paper_shop_daily_sales VALUES
('notebooks', 2, '2019', '1', '1', 1, 1),
('notebooks', 3, '2019', '5', '12', 1, 2),   
('notebooks', 1, '2019', '8', '31', 1, 3),   
('pencils', 2, '2019', '5', '2', 2, 1),   
('pencils', 5, '2019', '6', '7', 2, 2),   
('pencils', 1, '2019', '9', '11', 3, 3),   
('crayons', 1, '2019', '4', '15', 1, 1),   
('crayons', 5, '2019', '7', '10', 1, 2),   
('crayons', 2, '2019', '12', '20', 1, 3),
('crayons', 2, '2019', '10', NULL, 1, 1);

INSERT INTO paper_shop_monthly_sales VALUES
('notebooks-150', '2018', 1, 1),   
('notebooks-200', '2019', 1, 2),          
('notebooks-30', '2019', 2, 3),          
('pencils-100', '2018', 1, 1),           
('pencils-50', '2018', 2, 2),           
('pencils-130', '2019', 1, 3),           
('crayons-80', '2018', 1, 1),           
('crayons-90', '2019', 1, 2),          
('crayons-80', '2019', 2, 3);  
