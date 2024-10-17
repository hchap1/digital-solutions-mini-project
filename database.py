# Harrison Chapman

import sqlite3 as sql

class Field:
    def __init__(self, var_name, var_type): # int, text, datetime, ect.
        self.var_name = var_name
        self.var_type = var_type

def create_table(tablename, fields):
    text = f"create table if not exists {tablename} ("
    for field in fields:
        text += f"\n\t{fields.var_name} {field.var_type},"
    text += "\n);"
    return text

class Database:
    filename = "database.db"
    def __init__(self):
        self.database = sql.connect(self.filename)
        self.execute(create_table("players", (
            Field("ID", "int primary key auto increment"),
            Field("nickname", "text"),
            Field("squad_rank", "int"),
            Field("team_id", "int"),
            Field("real_name", "text"),
        )))

        self.execute(create_table("teams", (
            Field("ID", "int primary key auto increment"),
            Field("name", "text"),
        )))
        
        self.execute(create_table("matches", (
            Field("ID", "int primary key auto increment"),
            Field("datetime", "datetime"),
            Field("mvp", "int"),
            Field("winning_team", "int"),
            Field("map", "text"),
        )))

        self.execute(create_table("stats", (
            Field("ID", "int primary key auto increment"),
            Field("team_id", "int"),
            Field("match_id", "int"),
            Field("kills", "int"),
        )))

    def execute(self, command):
        self.database.execute(command)
        self.database.commit()

    def add_team(self, name):
        self.execute(f"insert into teams values('{name}');") 
    
    def get_team_id(self, name):
        cursor = self.database.cursor()
        cursor.execute(f"select id from teams where name='{name}';")
        return int(cursor.fetchall()[0])

    def add_player(self, nickname, squad_rank, team_id, real_name):
        self.execute(f"insert into players values('{nickname}', {squad_rank}, {team_id}, '{real_name}');")

    def add_stats(self, team_id, match_id, kills):
        self.execute(f"insert into stats values({team_id}, {match_id}, {kills});")

    def add_match(self, datetime, mvp, winning_team, map):
        self.execute(f"insert into matches values('{datetime}', {mvp}, {winning_team}, '{map}')")

    def get_players_from_team(self, team_id):
        cursor = self.database.cursor()
        cursor.execute(f"select id from players where team_id={team_id};")
        return [int(x) for x in cursor.fetchall()]
