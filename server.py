from flask import jsonify
from flask import Flask
import instaloader

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
app = Flask(__name__)


@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)


@app.route('/person/<string:name>/')
def hello(name):
    # Loading a profile from an Instagram handle
    handle_name = str(name)
    profile = instaloader.Profile.from_username(bot.context, handle_name)
    print("Username: ", profile.username)
    print("Number of Posts: ", profile.mediacount)
    print("Followers Count: ", profile.followers)
    print("Following Count: ", profile.followees)
    return jsonify({'followers': profile.followers})


if __name__ == '__main__':
    app.run(host='10.0.0.111', port=5000, debug=True, threaded=False)
