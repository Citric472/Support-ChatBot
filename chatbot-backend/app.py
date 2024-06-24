from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello, this is the chatbot backend!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_message = generate_response(user_message)
    return jsonify({"response": response_message})

def generate_response(message):
    # Implement simple logic to generate automated responses
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What can I assist you with today?",
        "how are you": "I'm just a bot, but I'm here to help!",
        "bye": "Goodbye! Have a nice day!",
        "order status": "You can check your order status in the Orders section of our website.",
        "product availability": "Our products are available on the website. Please visit the Products section for more details.",
        "delivery time": "Deliveries usually take 1-2 business days. You will receive a notification once your order is dispatched.",
        "payment options": "We accept various payment methods including credit/debit cards, mobile money, and bank transfers.",
        "technical support": "For technical support, please describe the issue you're facing, and we'll assist you.",
        "account issue": "For account-related issues, please contact our support team at support@twigafoods.com.",
        "reset password": "To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions to reset your password.",
        "contact support": "You can reach our support team at support@twigafoods.com or call +254-700-000-000.",
        "business hours": "Our business hours are Monday to Friday, 8 AM to 6 PM.",
        # Add more predefined responses as needed
    }

    # Simple keyword matching for demo purposes
    for key in responses:
        if key in message.lower():
            return responses[key]

    return "I'm sorry, I don't understand. Can you rephrase?"

if __name__ == '__main__':
    app.run(debug=True)
