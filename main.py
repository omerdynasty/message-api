from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Read SECRET_KEY from the .env file
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable not defined!")

messages = {}

def verify_key(key):
    """Verifies if the provided key is valid."""
    return key == SECRET_KEY

@app.route('/send_message/<message_id>', methods=['POST'])
def send_message(message_id):
    """Registers a message with a specific ID."""
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization key is missing or invalid"}), 401

    provided_key = auth_header.split(' ')[1]
    if not verify_key(provided_key):
        return jsonify({"error": "Invalid authorization key"}), 401

    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Message content is missing"}), 400

    messages[message_id] = data['message']
    return jsonify({"message": f"Message with ID '{message_id}' has been recorded"}), 200

@app.route('/get_message/<message_id>', methods=['GET'])
def get_message(message_id):
    """Retrieves and deletes the message with the specified ID."""
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"error": "Authorization key is missing or invalid"}), 401

    provided_key = auth_header.split(' ')[1]
    if not verify_key(provided_key):
        return jsonify({"error": "Invalid authorization key"}), 401

    if message_id in messages:
        message = messages.pop(message_id)
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": f"Message with ID '{message_id}' not found"}), 404

@app.route('/check_message/<message_id>', methods=['HEAD'])
def check_message(message_id):
    """Checks if a message with the specified ID exists without returning its content."""
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return '', 401  # Unauthorized, no body needed

    provided_key = auth_header.split(' ')[1]
    if not verify_key(provided_key):
        return '', 401  # Unauthorized, no body needed

    if message_id in messages:
        return '', 204  # No Content, indicates success (message exists)
    else:
        return '', 404  # Not Found

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
