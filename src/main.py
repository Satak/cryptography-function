"""
Function to encrypt and decrypt data
deploy:
gcloud beta functions deploy cryptography --entry-point main --runtime python37 --trigger-http --project $project --region europe-west1 --source ./src
"""

from cryptography.fernet import Fernet
from flask import jsonify, render_template


def get_key():
    return Fernet.generate_key().decode()


def encrypt(key, data):
    f = Fernet(key.encode())
    return f.encrypt(data.encode()).decode()


def decrypt(key, data):
    f = Fernet(key.encode())
    return f.decrypt(data.encode()).decode()


def main(request):
    if request.method == 'POST':
        request_json = request.get_json(silent=True)
        if not request_json:
            return jsonify({'error': 'No JSON payload'}), 400
        try:
            data = request_json.get('data')
            action = request_json.get('action')
            key = request_json.get('key')
            if action == 'get_key':
                return jsonify({'data': str(get_key())})
            if action == 'encrypt':
                return jsonify({'data': str(encrypt(key, data))})
            if action == 'decrypt':
                return jsonify({'data': str(decrypt(key, data))})
        except Exception as err:
            return jsonify({'error': str(err)}), 400
    return render_template('index.html')
