from flask import Flask, render_template, request, jsonify
import redis
import os
import pickle
from flask_cors import CORS


# Configure app and connection to redis. By default this will connect 
# to localhost redis, however you can define a REDIS_URL in your
# environment variable
app = Flask(__name__)
CORS(app)
r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))


def read():
    """Reads data from redis and returns a dictionary containing keys
    and values from the redis store. Note: data is stored using the
    'pickle' datatype, to preserve integrity of dicts.

    Returns:
        kv (dict): key-value pair from redis"""
    
    try:
        # Get data from redis
        redis_data = r.get('data')

        # Unpickle data
        kv = pickle.loads(redis_data)

        return kv

    except:
        # Return empty dict if no data in redis yet
        return {}


def write(key, value):
    """Writes key and value to the redis store. Note: data is stored 
    using the 'pickle' datatype, to preserve integrity of dicts.

    Args:
        key (str): key that you would like to write to
        value (str): value of the key

    Returns:
        status (bool): success status of write operation"""
    
    try:
        # Read existing key values from redis
        kv = read()

        # Update key-value store with new key-value
        kv.update({key: value})

        # Pickle data
        redis_data = pickle.dumps(kv)

        # Save data in redis
        r.set('data', redis_data)

        # Return True if successfully updated redis    
        return True
    
    except:
        # Return False if there was an error
        return False


@app.route('/data', methods=['GET', 'POST'])
def data():
    """API call to retreive and write data to redis"""
    
    # If there is a GET request on this endpoint
    if request.method == 'GET':
        print('[app] Reading data from redis...')

        # Get data from Redis
        data = read()

        # Return it as a JSON
        return jsonify(data)

    # If there is a POST request, write data 
    if request.method == 'POST':
        print('[app] Writing data to redis...')

        # Get data from POST request
        key = request.form['key']
        value = request.form['value']

        # Write it to Redis
        status = write(key, value)

        # Return success or error message based on status
        if status == True:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'fail'})


@app.route('/')
def index():
    """Render demo index page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')