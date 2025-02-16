from flask import Flask, request, jsonify

app = Flask(__name__)

# REST Endpoint for adding two numbers
@app.route('/add', methods=['GET'])
def add():
    """Add two numbers provided as query parameters."""
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = num1 + num2
    return jsonify({"result": result})

if __name__ == '__main__':
    # Start the REST server
    app.run(host='0.0.0.0', port=5000)
    print("REST service running on http://0.0.0.0:5000")