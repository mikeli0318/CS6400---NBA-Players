use NBA;
drop table Player;
create table Player(
	Season VARCHAR(7) NOT NULL,
	ID  INTEGER  NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Pos VARCHAR(5) NOT NULL,
    Age INTEGER NOT NULL,
    Team VARCHAR(5) NOT NULL,
    Games INTEGER NOT NULL,
    GS INTEGER NOT NULL,
    MP INTEGER NOT NULL,
    FG INTEGER NOT NULL,
    FGA INTEGER NOT NULL,
    FGP NUMERIC(4,3),
    3P INTEGER NOT NULL,
    3PA INTEGER NOT NULL,
    3PP NUMERIC(4,3),
    2P INTEGER NOT NULL,
    2PA INTEGER NOT NULL,
    2PP NUMERIC(4,3),
    EPGP NUMERIC(4,3),
    FT INTEGER NOT NULL,
    FTA INTEGER NOT NULL,
    FTP NUMERIC(4,3),
    ORB INTEGER NOT NULL,
    DRB INTEGER NOT NULL,
    TRB INTEGER NOT NULL,
    AST INTEGER NOT NULL,
    STL INTEGER NOT NULL,
    BLK INTEGER NOT NULL,
    TOV INTEGER NOT NULL,
    PF INTEGER NOT NULL,
    PTS INTEGER NOT NULL,
    Primary Key(ID, Season, Team)
);