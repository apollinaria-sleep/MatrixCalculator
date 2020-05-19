import requests
import argparse
import sys


def create_main_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8000, type=int)
    return parser


def graceful_exit():
    ack = input('Are you sure you want to leave (Y/N)?\n')
    if ack == 'Y':
        print('Goodbye!')
        exit()
    elif ack == 'N':
        print('OK, let\'s continue')
    else:
        print('Unknown input, but continue')


def amount(main_args):
    result = requests.get(f'http://{main_args.host}:{main_args.port}/amount', params=dict(
    )).text
    print(result)


def difference(main_args):
    result = requests.get(f'http://{main_args.host}:{main_args.port}/difference', params=dict(
    )).text
    print(result)


def multiplication(main_args):
    result = requests.get(f'http://{main_args.host}:{main_args.port}/multiplication', params=dict(
    )).text
    print(result)


def ask_amount(argument_name):
    user_input = input(f'Please, enter {argument_name}:\n')
    if not user_input:
          raise Exception('Incorrect input')
    else:
        try:
            return int(user_input)
        except ValueError:
            raise Exception('Incorrect input')


def ask_matrix(argument_name):
    print(f'Please, enter {argument_name}:')
    matrix = sys.stdin.read()
    return matrix


def add_matrix(main_args):
    try:
        print(requests.post(f'http://{main_args.host}:{main_args.port}/add_matrix', params=dict(
            first_rows=ask_amount('number of rows'),
            first_col=ask_amount('number of columns'),
            first_matrix=ask_matrix('first matrix'),
            second_rows=ask_amount('number of rows'),
            second_col=ask_amount('number of columns'),
            second_matrix=ask_matrix('second matrix')
        )).text)
    except Exception as e:
        print(e)
        return


def main():
    main_parser = create_main_parser()
    main_args = main_parser.parse_args()

    while True:
        try:
            cmd = input('Enter command>\n')
            if cmd == 'add_matrix':
                add_matrix(main_args)
            elif cmd == 'amount':
                amount(main_args)
            elif cmd == 'difference':
                difference(main_args)
            elif cmd == 'composition':
                composition(main_args)
            elif cmd == 'exit':
                graceful_exit()
            else:
                print(f'Unknown command: {cmd}')
        except KeyboardInterrupt:
            graceful_exit()


if __name__ == '__main__':
    main()

