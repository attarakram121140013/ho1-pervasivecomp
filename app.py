from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db
import os

app = Flask(__name__)

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate("./ho1-pervasivecomp-firebase-adminsdk-bs96q-986a11f667.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ho1-pervasivecomp-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Referensi ke node 'cpu_usage' di Firebase
ref = db.reference('cpu_usage')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    snapshot = ref.order_by_key().limit_to_last(10).get()  # Ambil 10 data terakhir
    data = [{'cpu': value['cpu'], 'timestamp': value['timestamp']} for key, value in snapshot.items()]
    return jsonify(data)

# Tidak perlu app.run() karena Vercel yang akan mengurus servernya