from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
@app.route('/cryptography', methods=['GET', 'POST'])
def api_cryptography():
    if request.method == 'GET':
        return render_template('index.html')

    json_data = request.get_json(silent=True)
    return jsonify({'data': str(json_data)})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
