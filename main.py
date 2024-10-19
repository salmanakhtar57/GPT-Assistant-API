from flask import Flask, jsonify, request
import openai

app = Flask(__name__)

openai.api_key = "sk-xxx"

ASSISTANT_ID = "asst_xxx"

def get_assistant_response(user_question):
    try:
        response = openai.ChatCompletion.create(
            model=ASSISTANT_ID,
            messages=[
                {"role": "user", "content": user_question}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/data', methods=['POST'])
def get_data_response():
    user_question = request.json.get('question', "Please provide your query.")
    latest_message = get_assistant_response(user_question)

    response = {
        "response": latest_message
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

