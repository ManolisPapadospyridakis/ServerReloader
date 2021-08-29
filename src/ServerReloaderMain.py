import sys
import os
import signal
from ServerReloader import ServerReloader

serverReloader = None

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    if serverReloader != None:
        serverReloader.killServerProcesses()
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f'<script> <folder for monitoring> <command> <interval>')
        sys.exit()

    if not os.path.exists(sys.argv[1]):
        print('The path that you provide does not exists.')
        sys.exit()

    folder = sys.argv[1]
    command = sys.argv[2]
    try:
        interval = float(sys.argv[3])
    except ValueError:
        print('Interval must be a float number, e.g, 0.5')
        sys.exit()

    serverReloader = ServerReloader(folder=folder, command=command, interval=interval)
    signal.signal(signal.SIGINT, signal_handler)

    serverReloader.restartServerOnFolderChanges()