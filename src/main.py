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


def post_controller(action, key=None, data=None):
    action_map = {
        'get_key': lambda: get_key(),
        'encrypt': lambda: encrypt(key, data),
        'decrypt': lambda: decrypt(key, data)
    }
    return {'data': action_map[action]()}


def main(request):
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        request_json = request.get_json(silent=True)
        allowed_actions = ('get_key', 'encrypt', 'decrypt')

        if not request_json:
            return jsonify({'error': 'No JSON payload'}), 400
        try:
            data = request_json.get('data')
            action = request_json.get('action')
            key = request_json.get('key')
            if action not in allowed_actions:
                return jsonify({'error': f'Action not in allowed actions: {allowed_actions}'}), 400
            return jsonify(post_controller(action, key, data))
        except Exception as err:
            str_err = str(err)
            if not str_err:
                str_err = 'Encryption/Decryption function failed. Might be because of invalid key!'
            return jsonify({'error': str_err}), 400
    return jsonify({'error': 'Method not supported'}), 400
