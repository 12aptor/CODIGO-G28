from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

DATABASE_CONFIG = {
    'dbname': 'flask-postgres',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn

def create_user_table():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(200) NOT NULL,
                email VARCHAR(200) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        print('Table user created successfully')
    except Exception as e:
        print(f'Error creating table: {e}')

create_user_table()

@app.route('/users', methods=['GET', 'POST'])
def users():
    method = request.method
    if method == 'GET':
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users;')

            users_list = [] 
            for row in cursor.fetchall():
                user = {
                    'id': row[0],
                    'name': row[1],
                    'email': row[2],
                    'created_at': str(row[3])
                }
                users_list.append(user)

            return jsonify(users_list), 200
        except Exception as e:
            return jsonify({
                'error': str(e)
            }), 500
    elif method == 'POST':
        try:
            json = request.get_json()
            name = json.get('name')
            email = json.get('email')

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (name, email) VALUES (%s, %s);',
                (name, email)
            )
            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({
                'message': 'User created successfully'
            }), 200
        except Exception as e:
            return jsonify({
                'error': str(e)
            }), 500
        
if __name__ == '__main__':
    app.run(debug=True)