import sqlite3
from sqlite3.dbapi2 import Cursor

con=sqlite3.connect('utils\db_api\Datebase.db')
cur=con.cursor()

def insert_id(id):
    sql=f"""INSERT INTO Resume (ID_TG) VALUES ({id})"""
    cur.execute(sql)
    con.commit()

def insert_data_reg(id,data):
    sql=f"""UPDATE Resume SET Date_fraim={data} WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_post(id,post):
    sql=f"""UPDATE Resume SET Post='{post}' WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_FIO(id,fio):
    sql=f"""UPDATE Resume SET FIO='{fio}' WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_pmg(id,pmg):
    sql=f"""UPDATE Resume SET PMG='{pmg}' WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_Age(id,age):
    sql=f"""UPDATE Resume SET Age={age} WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_sex(id,sex):
    sql=f"""UPDATE Resume SET Sex={sex} WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_cityzenship(id,city):
    sql=f"""UPDATE Resume SET Cityzenship='{city}' WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_experience(id,exp):
    sql=f"""UPDATE Resume SET Experience='{exp}' WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_employment(id,emp):
    sql=f"""UPDATE Resume SET Employment='{emp}' WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_skills(id,skil):
    sql=f"""UPDATE Resume SET Skills = '{skil}' WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()

def insert_portfolio(id,prt):
    sql=f"""UPDATE Resume SET Portfolio_link = '{prt}' WHERE ID_TG={id}"""
    cur.execute(sql)
    con.commit()
