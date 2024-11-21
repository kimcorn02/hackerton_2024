from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

JOB_API_URL = "https://flow.edutrack.kr/api/v1/prediction/0beb8cf8-af68-4779-bfdd-bde54737215a"

def job_query(payload):
    response = requests.post(JOB_API_URL, json=payload, verify=False)
    return response.json()

@app.route('/job', methods=['POST'])
def job_chat():
    user_input = request.json.get('question')
    job_output = job_query({
        'question' : user_input
    })
    print(job_output)
    return jsonify(job_output)

if __name__ == '__main__':
    app.run(debug=True)