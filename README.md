# Flask Redis Quickstart
## Templates to do build background magic ✨
Have you ever wanted to process an uploaded file asynronously? Or maybe you want to have a background process that updates data? Or maybe you just you want to have some variables that are shared between several python modules - this is the quickstart template for you!

Some examples of what you can build:

🌧 **Weather app** that pulls weather data in the background

✅ **Visualization platform** which runs large queries in background

🕹 **Programming tool** that programs Arduino's from a background process

## Getting started
**Clone this repository**

Download the git repository onto your computer.
```
git clone https://github.com/sasha42/Flask-Redis-Quickstart.git
cd Flask-Redis-Quickstart
```

**Install requirements**

Set up python dependencies and install redis-server.
```
# Redis and pip on linux
sudo apt-get install redis-server python3-pip

# Redis on mac
brew install redis-server
redis-server

# Python
sudo pip3 install -r requirements.txt
```

*Note: Mac users will need to start redis-server manually, by typing `redis-server` into their terminal after installation*

**Run example**
```
cd basic-example
python app.py
```
You can now try out the example in your browser on [localhost:5000](http://localhost:5000). 

Copy the template into your own project, and get starting building awesome things 🚀

---
️❤️ Made with love in Switzerland