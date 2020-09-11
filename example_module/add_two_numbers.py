import simppl.command_line_tool
from simppl.command_line_tool import command_line_tool


@command_line_tool
def run(argv):
    """
    adds to numbers and prints the results
    """
    parser = simppl.command_line_tool.get_parser(argv[0], __doc__)
    parser.add_argument('first_number', type=float)
    parser.add_argument('second_number', type=float)
    args = parser.parse_args(argv[1:])

    print(args.first_number + args.second_number)
