from flask import Flask

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Routing untuk halaman utama
@app.route('/')
def home():
    return "Hello, Flask on Koyeb!"

# Menjalankan aplikasi
if __name__ == '__main__':
    # Pastikan aplikasi berjalan di host '0.0.0.0' dan port 5000
    app.run(host='0.0.0.0', port=8000)
