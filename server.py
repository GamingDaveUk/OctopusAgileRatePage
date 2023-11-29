from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

current_rate = "Initial Current Rate"
next_rate = "Initial Next Rate"

@app.route('/')
def index():
    return render_template('index.html', current_rate=current_rate, next_rate=next_rate)

# Modify the 'update_rates' event to 'update' in server.py
@socketio.on('update_rates')
def handle_update_rates(data):
    global current_rate, next_rate
    current_rate = data['current_rate']
    next_rate = data['next_rate']
    emit('update', {'current_rate': current_rate, 'next_rate': next_rate}, broadcast=True)
    print('Emitted update event:', {'current_rate': 99, 'next_rate': 88})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')
