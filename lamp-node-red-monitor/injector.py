import random
import time
import mysql.connector
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "iot_user",
    "password": "Iot_pass1!",
    "database": "iot_db",
}

INTERVAL = 10  # seconds


def connect():
    return mysql.connector.connect(**DB_CONFIG)


def insert(conn, temp, humid):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s)",
        (temp, humid),
    )
    conn.commit()
    cursor.close()


def main():
    conn = connect()
    print("injector 시작 — 10초마다 MySQL에 데이터를 삽입합니다. (Ctrl+C 종료)")
    try:
        while True:
            temp = round(random.uniform(0, 50), 1)
            humid = round(random.uniform(0, 100), 1)
            insert(conn, temp, humid)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] temperature={temp}°C  humidity={humid}%")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\n종료합니다.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
