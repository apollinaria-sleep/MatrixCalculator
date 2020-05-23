import requests
import argparse
from config import INPUT, DEFAULT_HOST, DEFAULT_PORT, COMMANDS, EXIT


def create_main_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default=DEFAULT_HOST)
    parser.add_argument('--port', default=DEFAULT_PORT, type=int)
    return parser


def graceful_exit():
    ack = input(EXIT['QUESTION'])
    if ack == EXIT['YES']:
        print(EXIT['ANSWER_FIRST'])
        exit()
    elif ack == EXIT['NO']:
        print(EXIT['ANSWER_SECOND'])
    else:
        print(EXIT['ANSWER_THIRD'])


def amount(main_args, SERVER_CONNECTION):
    result = requests.get(SERVER_CONNECTION + '/' + COMMANDS['GET_FIRST'], params=dict(
    )).text
    print(result)


def difference(main_args, SERVER_CONNECTION):
    result = requests.get(SERVER_CONNECTION + '/' + COMMANDS['GET_SECOND'], params=dict(
    )).text
    print(result)


def multiplication(main_args, SERVER_CONNECTION):
    result = requests.get(SERVER_CONNECTION + '/' + COMMANDS['GET_THIRD'], params=dict(
    )).text
    print(result)


def ask_amount(argument_name):
    print(f'Please, enter {argument_name}:')
    user_input = input()
    if not user_input:
          raise TypeError(INPUT['ERROR'])
    else:
        try:
            return int(user_input)
        except ValueError:
            raise TypeError(INPUT['ERROR'])


def ask_matrix(argument_name):
    print(f'Please, enter {argument_name}:')
    matrix = input()
    return matrix


def add_matrix(main_args, SERVER_CONNECTION):
    try:
        print(requests.post(SERVER_CONNECTION + '/' + COMMANDS['POST_FIRST'], params=dict(
            first_rows=ask_amount('number of rows'),
            first_col=ask_amount('number of columns'),
            first_matrix=ask_matrix('first matrix'),
            second_rows=ask_amount('number of rows'),
            second_col=ask_amount('number of columns'),
            second_matrix=ask_matrix('second matrix')
        )).text)
    except TypeError as e:
        print(e)
        return


def main():
    main_parser = create_main_parser()
    main_args = main_parser.parse_args()
    SERVER_CONNECTION=f'http://{main_args.host}:{main_args.port}'

    while True:
        try:
            cmd = input(INPUT['COMMAND'])
            if cmd == COMMANDS['POST_FIRST']:
                add_matrix(main_args, SERVER_CONNECTION)
            elif cmd == COMMANDS['GET_FIRST']:
                amount(main_args, SERVER_CONNECTION)
            elif cmd == COMMANDS['GET_SECOND']:
                difference(main_args, SERVER_CONNECTION)
            elif cmd == COMMANDS['GET_THIRD']:
                multiplication(main_args, SERVER_CONNECTION)
            elif cmd == COMMANDS['EXIT']:
                graceful_exit()
            else:
                print(f'Unknown command: {cmd}')
        except KeyboardInterrupt:
            graceful_exit()


if __name__ == '__main__':
    main()

