import sqlite3,sys,os.path

if len(sys.argv)>1:
    database_path = sys.argv[1]
else:
    database_path = input("Database Path")
if os.path.exists(database_path):
    try :
        conn = sqlite3.connect(database_path)
        c=conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for table in c.fetchall():
            if table[0] == "User":
                print("This database maybe 3.4 or later")
                exit()
        c.execute("create table User (Account CLOB,Password CLOB);")
        c.execute("create table Note (Note1 CLOB,Note2 CLOB);")
        c.execute("insert into User values('admin','admin');")
        c.execute("insert into Note values('Version','3.4');")
        conn.commit()
        del c,conn
        print("Succ")
        os.system("pause")
    except IOError:
        print(IOError)
else:
    print("File isn't exists!")
