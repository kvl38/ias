from flask import Flask, request
import psycopg2
import json

app = Flask(__name__)

@app.route('/getChat', methods=['GET'])
def getChat():
    cur = conn.cursor()
    cur.execute('SELECT * FROM chat;')
    chat = cur.fetchall()  #[(2, 'vlad', 'priv'), (4, 'Pasha', 'Hello'), (5, 'Semen', '123456')]
    cur.close()

    list_chat = []
    for i in chat:
        dict_chat = {}
        dict_chat[i[1]] = i[2]
        list_chat.append(dict_chat)

    tuple_chat = tuple(list_chat)
    print(tuple_chat)
    return


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