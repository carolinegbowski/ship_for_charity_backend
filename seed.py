from sqlite3 import connect

DBPATH = "final_project.db"

# password b'$2b$12$GkymxjhVREpNCCaBBlkNtO3QJ8vjDNuddoF0v/fNqDlbIoeMPD776'
# INSERT INTO scans (ip_address, ports, services)VALUES ("127.0.0.1","22", "ssh")


def seed(dbpath=DBPATH):
    with connect(dbpath) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO np_accounts (pk, company_name, username, password_hash) VALUES (1, "company", "user", "b'$2b$12$GkymxjhVREpNCCaBBlkNtO3QJ8vjDNuddoF0v/fNqDlbIoeMPD776'") ;"""
        cursor.execute(SQL,)


seed()
