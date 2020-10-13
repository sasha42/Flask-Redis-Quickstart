import redis
import pickle
import time
import os


if __name__ == "__main__":
    # Connect to the redis queue
    r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

    # Subscribe to the queue
    p = r.pubsub()
    p.psubscribe('job_*')

    print('[worker] Started listening to queue')

    # Loop over the queue
    while True:
        message = p.get_message()

        # Process message if it actually contains data
        if message and type(message['data']) == bytes:

            # Get the job id out
            data = pickle.loads(message['data'])
            print('[worker] triggered on message')
            #print(data)

            # Run fake background job
            # PUT YOUR BACKGROUND LOGIC HERE
            time.sleep(10)
            print('[worker] Background job completed in 10s')

        time.sleep(1)  # be nice to the system :)
