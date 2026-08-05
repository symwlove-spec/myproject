import sqlite3
import hashlib
import datetime

DB_NAME = "myproject.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """테이블 생성 (users, learning_history)"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. users 테이블
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # 2. learning_history 테이블
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS learning_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid TEXT NOT NULL,
        m1 INTEGER, m2 INTEGER, m3 INTEGER, m4 INTEGER, m5 INTEGER,
        m6 INTEGER, m7 INTEGER, m8 INTEGER, m9 INTEGER, m10 INTEGER,
        score INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (userid) REFERENCES users(userid)
    )
    """)
    
    conn.commit()
    conn.close()

# 비밀번호 해싱
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 회원가입
def register_user(userid, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (userid, password) VALUES (?, ?)", 
                       (userid, hash_password(password)))
        conn.commit()
        return True, "회원가입이 완료되었습니다."
    except sqlite3.IntegrityError:
        return False, "이미 존재하는 계정 ID입니다."
    finally:
        conn.close()

# 로그인 검증
def login_user(userid, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE userid = ? AND password = ?", 
                   (userid, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# 평가 이력 저장
def save_quiz_result(userid, user_answers, score):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO learning_history (userid, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, score)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    params = [userid] + user_answers + [score]
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# 평가 이력 조회
def get_user_history(userid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM learning_history WHERE userid = ? ORDER BY created_at DESC", (userid,))
    rows = cursor.fetchall()
    conn.close()
    return rows