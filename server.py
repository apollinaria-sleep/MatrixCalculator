import flask
import lib


default_port = 8000

app = flask.Flask('matrix_calculator')
last_matrix = lib.LastMatrix()


@app.route('/add_matrix', methods=['POST'])
def add_matrix():
    args = {
        item: flask.request.args[item]
        for item in last_matrix.POSSIBLE_ITEMS
        if item in flask.request.args
    }
    return last_matrix.add_matrix(**args)


@app.route('/amount', methods=['GET'])
def amount():
    amount = last_matrix.amount()
    return amount


@app.route('/difference', methods=['GET'])
def difference():
    difference = last_matrix.difference()
    return difference


@app.route('/multiplication', methods=['GET'])
def multiplication():
    multiplication = last_matrix.multiplication()
    return multiplication


def main():
    app.run('::', port=default_port, debug=True)


if __name__ == '__main__':
    main()

