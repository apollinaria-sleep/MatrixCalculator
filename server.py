import flask
import lib
from config import COMMANDS, DEFAULT_PORT


app = flask.Flask('matrix_calculator')
last_matrix = lib.LastMatrix()


@app.route('/' + COMMANDS['POST_FIRST'], methods=['POST'])
def add_matrix():
    args = {
        item: flask.request.args[item]
        for item in last_matrix.POSSIBLE_ITEMS
        if item in flask.request.args
    }
    return last_matrix.add_matrix(**args)


@app.route('/' + COMMANDS['GET_FIRST'], methods=['GET'])
def amount():
    amount = last_matrix.amount()
    return amount


@app.route('/' + COMMANDS['GET_SECOND'], methods=['GET'])
def difference():
    difference = last_matrix.difference()
    return difference


@app.route('/' + COMMANDS['GET_THIRD'], methods=['GET'])
def multiplication():
    multiplication = last_matrix.multiplication()
    return multiplication


def main():
    app.run('::', port=DEFAULT_PORT, debug=True)


if __name__ == '__main__':
    main()

