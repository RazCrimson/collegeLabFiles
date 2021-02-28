import sys

args = sys.argv
host = "0.0.0.0"
port = 11055

if len(args) == 2 and args[1][0] == 's':
    from module.server import TCPServer

    server = TCPServer(host, port)
    server.handle_clients()

else:
    from module.client import TCPClient

    client = TCPClient(host, port)
    client.start_interactive_mode()