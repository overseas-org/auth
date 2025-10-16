from flask import Flask, request, jsonify
from flask_cors import CORS
from actions import login_user, logout_user, sinup_user, verify_token, refresh_token

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route("/login", methods=["POST"])
def login():
	data = request.json
	user = data["user"]
	if user["username"] == "" or (("sso_verified" not in user or not user["sso_verified"]) and ("encrypted_password" not in user or user["encrypted_password"] == "")):
		return jsonify("missing credentials"), 400
	try:
		tokens = login_user(user)
		return jsonify(tokens), 200
	except Exception as e:
		return jsonify(str(e)), 401
	

@app.route("/logout", methods=["POST"])
def logout():
	data = request.json
	token = data["token"]
	try:
		logout_user(token)
	except Exception as e:
		return str(e), 400
	return "", 200

@app.route("/verify", methods=["POST"])
def verify():
	data = request.json
	token = data["token"]
	try:
		if verify_token(token):
			return "", 200
		else:
			return "invalid token", 403
	except Exception as e:
		return jsonify(str(e)), 403
	
@app.route("/refresh", methods=["POST"])
def refresh():
	data = request.json
	token = data["token"]
	try:
		tokens = refresh_token(token)
		return jsonify(tokens), 200
	except Exception as e:
		return jsonify(str(e)), 400

@app.route("/signup", methods=["POST"])
def signup():
	data = request.json
	user = data["user"]
	try:
		tokens = sinup_user(user)
		return jsonify(tokens), 200
	except Exception as e:
		return jsonify(str(e)), 500

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=5005)