
# main.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Echo Request Information</h1>
    <form action="/echo" method="post">
        <label for="headers">Headers:</label>
        <textarea id="headers" name="headers"></textarea><br>

        <label for="method">Method:</label>
        <input id="method" name="method" type="text"><br>

        <label for="body">Body:</label>
        <textarea id="body" name="body"></textarea><br>

        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/echo', methods=['POST'])
def echo():
    headers = request.headers
    method = request.method
    body = request.get_data()

    response = 'Headers:\n'
    for key, value in headers.items():
        response += f'{key}: {value}\n'

    response += f'\nMethod: {method}\n\nBody: {body.decode("utf-8")}'
    return response

if __name__ == '__main__':
    app.run(debug=True)
