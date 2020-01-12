import sqlite3
from sqlite3 import Error


# from .models import College
# from colleges.models import College

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_task(conn):
    cur = conn.cursor()
    # sql = "select * from university_colleges" .""
    cur.execute("select * from university_colleges")

    rows = cur.fetchall()
    # resp = []
    # for row in rows:
    #     # resp['college_name'] = row[2].replace("\n", "")
    #     # resp['address'] = row[3].replace("\n", "")
    #     # resp['state'] = row[4]
    #     # resp['university_name'] = row[10]
    #     # resp['city'] = row[11]
    #     resp[0] = row[11].replace("\n", "")
    #     resp.append(resp)

    return rows
        # print(row[11].replace("\n", ""), '\n')

        # print(sys.path)
        # exit()

def main():
    datatabe = r"/Users/justincletus/Documents/SmartUniversity/main.db"

    conn = create_connection(datatabe)
    with conn:
        return select_all_task(conn)

if __name__ == '__main__':
    main()
