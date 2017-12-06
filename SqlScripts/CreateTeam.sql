use NBA;
drop table Team;
create table Team(
	Franchise VARCHAR(50) NOT NULL PRIMARY KEY,
    Abbr VARCHAR(5) NOT NULL,
    League VARCHAR(10) NOT NULL,
    FromYear INTEGER,
    ToYear INTEGER,
    Years INTEGER,
    Games INTEGER,
    WINS INTEGER,
    LOSSES INTEGER,
    WLP NUMERIC(4,3),
    Playoffs INTEGER,
    DivisionFirst INTEGER,
    ConferenceChampion INTEGER,
    Champion INTEGER
);