from datetime import datetime

import psycopg2
from flask import Flask, request, jsonify

# create table users(
# 	id serial primary key,
# 	username varchar(50) unique not null,
# 	password varchar(50) not null,
# 	email varchar(50) unique not null,
# 	first_name varchar(50),
# 	last_name varchar(50),
# 	bdate date default now()
# );

postgres_params = {
    "user": "postgres",
    "password": "postgres",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "exercises"
}

app = Flask(__name__)


def create_user(request):
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    bdate = datetime.strptime(request.json.get('bdate'), '%d-%m-%Y')

    query = """
    INSERT INTO users(username, password, email, first_name, last_name, bdate) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (username, password, email, first_name, last_name, bdate)

    conn = psycopg2.connect(**postgres_params)
    cur = conn.cursor()
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()


def get_users(request):
    query = f"""
        SELECT * FROM  users 
        WHERE { " AND ".join([f"{k} = '{v}'" for k, v in request.args.items()])} 
        """ if request.args else """SELECT * FROM  users"""

    conn = psycopg2.connect(**postgres_params)
    cur = conn.cursor()
    cur.execute(query)
    users = cur.fetchall()
    cur.close()
    conn.close()

    return users


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        create_user(request)
        return '', 201
    else:
        return jsonify({'users': get_users(request)}), 200


if __name__ == '__main__':
    app.run(port=8000, debug=True)