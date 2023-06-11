from flask import Flask, render_template, request, jsonify
from privateGPT.gpt import gpt, run

app = Flask(__name__)

conversation = []
qa = gpt()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def handle_query():
    query = request.form["query"]
    conversation.append(('user', query))
    response = run(qa, query)  # Replace with your Python function that generates a response
    conversation.append(('bot', response))

    return jsonify({'response': response})

def process_query(query):
    # Replace this function with your actual query processing logic
    # This is just a placeholder
    return "You said: " + query

if __name__ == "__main__":
    app.run()
