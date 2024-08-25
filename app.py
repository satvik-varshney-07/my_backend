from flask import Flask, request, jsonify

app = Flask(__name__)

# GET method endpoint
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# POST method endpoint
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    if not isinstance(data, list):
        return jsonify({"is_success": False}), 400

    user_id = "satvik_varshney_07012003"  # Replace with your full name and DOB in ddmmyyyy format
    email = "satvik.varshney2021@vitbhopal.ac.in"  # Replace with your college email ID
    roll_number = "21BCE10134"  # Replace with your roll number

    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    # Find the highest lowercase alphabet
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
