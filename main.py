from flask import Flask, request
import psycopg2
import json

app = Flask(__name__)

@app.route('/')
def Start():
    return "hello server~!!"

@app.route('/getChat', methods=['GET'])
def getChat():
    cur = conn.cursor()
    cur.execute('SELECT name, message FROM chat;')
    dict = cur.fetchall()

    result = json.dumps(dict, indent=2, ensure_ascii=False)
    cur.close()
    return result


@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    name = request.args.get("name")
    message = request.args.get("message")

    cur = conn.cursor()
    cur.execute(f'INSERT INTO chat (name, message) VALUES (\'{name}\',\'{message}\');')
    conn.commit()
    cur.close()

    dict_message = {}
    dict_message[str(name)] = str(message)
    return dict_message


if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        database="ias",
        user='postgres',
        password='123')

    app.run(host='127.0.0.1', port='8000')
    conn.close()