from flask import Flask, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def run_tests():
    result = subprocess.run(['pytest', '-q'], capture_output=True, text=True)
    output = result.stdout + result.stderr
    return Response(output, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
