import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="home@1234",
        database="GadgetHub"
    )

# testing
if __name__ == "__main__":
    try:
        conn=get_connection()
        print("Database connected")
        conn.close()
    except Exception as e:
        print("Database connected failed",e)