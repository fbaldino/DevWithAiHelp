from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test')
def test_instructions():
    return Response(
        'Run the test suite in the app container with: docker compose exec app pytest -q\n',
        mimetype='text/plain',
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
