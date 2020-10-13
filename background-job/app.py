from flask import Flask, render_template, request, jsonify
import redis
import os
import pickle
from flask_cors import CORS
from secrets import token_urlsafe


# Configure app and connection to redis. By default this will connect 
# to localhost redis, however you can define a REDIS_URL in your
# environment variable
app = Flask(__name__)
CORS(app)
r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))


@app.route('/job', methods=['POST'])
def job():
    """Creates a new Redis job and sends it to the queue so that
    it can be processed in the background"""
    
    print('[app] Creating a new job in redis...')

    # Get data from POST request
    value = request.form['value']

    # Generate a unique token used to track progress of download job
    job_id = token_urlsafe(11)

    # Pickle it to preserve data types for redis
    data = {"job_id": job_id, "value": value}
    p_data = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)

    # Publish a new job to the redis worker so that it can
    # process it in the background asyncrynously
    r.publish(f'job_{job_id}', p_data)

    # return jobId to user
    return jsonify({'jobId': job_id})


@app.route('/')
def index():
    """Render demo index page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')