

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

FAQS = {
    "hello": "Hello! Welcome to our support chatbot. How can I help you?",
    "hi": "Hi there! What would you like to know?",
    "hours": "Our customer support is available Monday to Friday, 9 AM to 6 PM.",
    "price": "Please tell me which product or service you are interested in.",
    "payment": "We accept common online payment methods. Contact support for payment assistance.",
    "refund": "For a refund, please share your order details with our support team.",
    "contact": "You can contact our support team at support@example.com.",
    "services": "We provide customer support, product information, and order assistance.",
    "thanks": "You're welcome! Let me know if you need anything else.",
    "bye": "Goodbye! Have a great day."
}


def get_response(message):
    message = message.lower().strip()

    if not message:
        return "Please type a question so I can help you."

    # Match common words and phrases in the user's question.
    for keyword, response in FAQS.items():
        if keyword in message:
            return response

    return (
        "Sorry, I don't have an answer for that yet. "
        "Please try asking about our services, prices, "
        "payment, refunds, support hours, or contact details."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({"error": "Message must be text."}), 400

    if len(message) > 1000:
        return jsonify({"error": "Message is too long."}), 400

    response = get_response(message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
