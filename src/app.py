from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configuración de la conexión a PostgreSQL
DB_HOST = 'db'  # Nombre del servicio de la base de datos en el archivo docker-compose.yml
DB_PORT = '5432'  # Puerto de PostgreSQL
DB_NAME = 'postgres'  # Nombre de la base de datos
DB_USER = 'postgres'  # Usuario de PostgreSQL
DB_PASSWORD = 'example'  # Contraseña de PostgreSQL

# Función para conectar a la base de datos
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Ruta para obtener todos los registros de la tabla "users"
@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        conn.close()
        return jsonify({'users': rows})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para crear un nuevo usuario en la tabla "users"
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        name = data['name']
        email = data['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
        conn.commit()
        conn.close()

        return jsonify({'message': 'User created successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

