import sqlite3,os,base64

if __name__ == "__main__":
    if not os.path.exists("Database.db"):
        print("Database.db isn't exists!")
        os.system('pause')
        exit()
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('select Address,Account,Password,Date from Data;')
    b_data=c.fetchall()

    conn = sqlite3.connect('New_Database.db')
    c = conn.cursor()
    c.execute('create table Data ("Address" TEXT,"Account" TEXT,"Password" TEXT,"Date" TEXT,"Text" TEXT);')
    conn.commit()
    for item in b_data:
        c.execute('insert into Data values("' + \
            base64.b64encode(item[0].encode()).decode() + '","'+\
            base64.b64encode(item[1].encode()).decode() + '","'+\
            base64.b64encode(item[2].encode()).decode() + '","'+\
            base64.b64encode(item[3].encode()).decode() + '","'+\
            "ZnJvbSBvbGQgZGF0YWJhc2U=" + '");')
    conn.commit()
    print("Finish")
    os.system("pause")