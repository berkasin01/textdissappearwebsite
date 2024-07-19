from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
import threading
from flask_wtf.csrf import CSRFProtect
import time
import random

story_prompts = [
    "A young girl discovers she has the ability to control the weather, but must learn to harness her powers before a massive storm destroys her town.",
    "In a world where dreams can be shared, a group of friends embarks on a quest to find a lost city that only exists in their dreams.",
    "A detective who can communicate with ghosts teams up with a spirit to solve a century-old murder mystery.",
    "A spaceship crash lands on a mysterious planet where time flows differently, and the crew must find a way to escape before they age decades in a matter of days.",
    "A librarian finds an ancient book that transports them to a magical realm where they must save a kingdom from an evil sorcerer.",
    "After a global blackout, a small town discovers that they are the only place on Earth with electricity, leading to mysterious and dangerous events.",
    "A young artist's paintings come to life, but she soon realizes that her creations have minds of their own and are starting to take over her world.",
    "In a dystopian future, a rebel group fights against a tyrannical government that controls society through a network of mind-controlling implants.",
    "A time traveler accidentally alters history, creating a world where technology never advanced past the medieval era. They must find a way to fix the timeline before it’s too late.",
    "Two siblings discover a hidden portal in their attic that leads to different dimensions, each with its own unique challenges and adventures."
]

app = Flask(__name__)
bs = Bootstrap5(app)
app.config["SECRET_KEY"] = 'secretkey'
csrf = CSRFProtect(app)

user_is_typing = False
typing_timer = None


class TextBox(FlaskForm):
    text_box = StringField("", render_kw={"class": "write_box"})

    def set_text(self, text):
        self.text_box.data = text


def reset_timer():
    global typing_timer
    if typing_timer:
        typing_timer.cancel()
    typing_timer = threading.Timer(5.0, clear_text_box)
    typing_timer.start()


def clear_text_box():
    # This function is called after 5 seconds of inactivity
    print("User has stopped typing for 5 seconds")


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/generate-prompt")
def prompt():
    rand_prompt = random.choice(story_prompts)
    return render_template("prompt.html", prompt_text=rand_prompt)


@app.route("/write")
def write(prompt_in=""):
    prompt_in = request.args.get('prompt_in', '')
    form = TextBox()
    if len(prompt_in)>0:
        form.set_text(prompt_in)
    return render_template('write.html', form=form)


@app.route('/update_text', methods=['POST'])
def update_text():
    text = request.form.get('text')
    print("Received text:", text)
    reset_timer()
    return '', 204  # No Content


@app.route('/check_typing_status', methods=['GET'])
def check_typing_status():
    global typing_timer
    if typing_timer and typing_timer.is_alive():
        return jsonify({'reset': False}), 200
    else:
        return jsonify({'reset': True}), 200


if __name__ == "__main__":
    app.run(debug=True)
