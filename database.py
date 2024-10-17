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
            Field("ID", "int primary key"),
            Field("nickname", "text"),
            Field("squad_rank", "int"),
            Field("team_id", "int"),
            Field("real_name", "text"),
        )))

        self.execute(create_table("teams", (
            Field("ID", "int primary key"),
            Field("name", "text"),
        )))
        
        self.execute(create_table("matches", (
            Field("ID", "int primary key"),
            Field("datetime", "datetime"),
            Field("mvp", "int"),
            Field("winning_team", "int"),
            Field("map", "text"),
        )))

        self.execute(create_table("stats", (
            Field("ID", "int primary key"),
            Field("team_id", "int"),
            Field("match_id", "int"),
            Field("kills", "int"),
        )))

    def execute(self, command):
        self.database.execute(command)
        self.database.commit()
