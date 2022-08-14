from config.sql_config import engine
import pandas as pd

## GET
def get_everything ():
    query = (f"""SELECT *FROM Speeches.tablename;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET one President's list of speeches from the data base
def get_everything_from_president(name):
    query = (f"""SELECT * FROM Speeches.tablename WHERE President = "{name}";""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET one Party's list of speeches in the data base
def get_everything_from_party(name):
    query = (f"""SELECT * FROM Speeches.tablename WHERE Party = "{name}";""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET list of all presidents in the data base
def list_all_presidents():
    query = (f"""SELECT President FROM Speeches.tablename GROUP BY President ORDER BY President ASC;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET list of all parties in the data base
def list_all_parties():
    query = (f"""SELECT Party FROM Speeches.tablename GROUP BY Party ORDER BY Party ASC;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## POST
def insert_new_speech (Year, Date, President, Party, Title, Summary, Transcript, URL):

    engine.execute(f"""
    INSERT INTO Speeches.tablename (Year, Date, President, Party, Title, Summary, Transcript, URL)
    VALUES ({Year}, '{Date}', '{President}', '{Party}', '{Title}', '{Summary}', '{Transcript}, '{URL}');
    """)
    
    return f"Correctly introduced: {Year}, {Date}, {President}, {Party}, '{Title}, '{Summary}, {Transcript}, {URL}"
