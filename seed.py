from sqlite3 import connect

DBPATH = "final_project.db"

# password b'$2b$12$GkymxjhVREpNCCaBBlkNtO3QJ8vjDNuddoF0v/fNqDlbIoeMPD776'
# INSERT INTO scans (ip_address, ports, services)VALUES ("127.0.0.1","22", "ssh")


def seed(dbpath=DBPATH):
    with connect(dbpath) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO np_accounts (
                pk,
                company_name,
                username,
                password_hash
                ) VALUES (
                1,
                "non_profit",
                "user",
                "b'$2b$12$GkymxjhVREpNCCaBBlkNtO3QJ8vjDNuddoF0v/fNqDlbIoeMPD776'"
                ) ;"""
        cursor.execute(SQL,)

        SQL = """INSERT INTO shipper_accounts (
                pk,
                company_name,
                username,
                password_hash
                ) VALUES (
                1,
                "shipper",
                "user",
                "b'$2b$12$GkymxjhVREpNCCaBBlkNtO3QJ8vjDNuddoF0v/fNqDlbIoeMPD776'"
                ) ;"""
        cursor.execute(SQL,)

        SQL = """ INSERT INTO routes (
                pk,
                shipper_account_id,
                departure_location,
                departure_date,
                arrival_location,
                arrival_date,
                total_containers,
                available_containers
                ) VALUES (
                1,
                1,
                "NYC",
                1578700800,
                "Miami",
                1580342400,
                10,
                10
        );"""
        cursor.execute(SQL,)

        SQL = """ INSERT INTO routes (
                pk,
                shipper_account_id,
                departure_location,
                departure_date,
                arrival_location,
                arrival_date,
                total_containers,
                available_containers
                ) VALUES (
                2,
                1,
                "Miami",
                1578700800,
                "NYC",
                1580342400,
                10,
                10
        );"""
        cursor.execute(SQL,)

        SQL = """ INSERT INTO routes (
                pk,
                shipper_account_id,
                departure_location,
                departure_date,
                arrival_location,
                arrival_date,
                total_containers,
                available_containers
                ) VALUES (
                3,
                1,
                "NYC",
                1578700800,
                "Berlin",
                1580342400,
                10,
                10
        );"""
        cursor.execute(SQL,)


seed()
