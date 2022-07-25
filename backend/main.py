from flask import Flask, render_template, make_response, jsonify, request
from physics_calculator import calculate_info

app = Flask(__name__, template_folder='../frontend/templates/',
            static_folder='../frontend/templates/static/')

HOST = "0.0.0.0"
PORT = 3200


@app.route("/")
def home():
    data = {'hit_position': 0.0, 'hit_velocity': 0.0, 'hit_angle': 0.0}
    return render_template('index.html', data=data)


@app.route('/calculate')
def calculate():
    if request.args:
        response = {
            'initialspeed': request.args['initialspeed'],
            'initialangle': request.args['initialangle'],
            'initialheight': request.args['initialheight']
        }

        data = calculate_info(
            starting_velocity=response['initialspeed'], starting_angle=response['initialangle'], starting_height=response['initialheight'])
        return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
