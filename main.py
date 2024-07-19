from flask import Flask, jsonify, request
from utils.credentials import USERNAME, PASSWORD, GROQ_KEY
from groq import Groq

app = Flask(__name__)

class AuthenticationError(Exception):
    pass

class GroqError(Exception):
    pass

def authenticate(username, password):
    if username != USERNAME or password != PASSWORD:
        raise AuthenticationError("Usuário ou senha inválidos")

@app.route('/', methods=['POST'])
def index():
    return jsonify({"status": 200})

@app.route('/groq-generator', methods=['POST'])
def generate_text():
    try:
        if not request.json or 'username' not in request.json or 'password' not in request.json or 'message' not in request.json:
            return jsonify({"error": "Username, Password e Message são requeridos.", "status": 400})
        authenticate(request.json["username"], request.json["password"])
        client = Groq(api_key=GROQ_KEY)
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": request.json["message"]}],
            model="llama3-8b-8192",
        )
        return jsonify({"text": chat_completion.choices[0].message.content})
    except AuthenticationError as e:
        return jsonify({"error": str(e), "status": 401})
    except GroqError as e:
        return jsonify({"error": str(e), "status": 500})

if __name__ == '__main__':
    app.run(port=5000)