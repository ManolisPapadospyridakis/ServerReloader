import subprocess
import time

from ProcessUtils import ProcessUtils
from Folder import Folder


class ServerReloader:
    def __init__(self, folder, command, interval):
        self.folder = folder 
        self.command = command
        self.interval = interval


    def killServerProcesses(self):
        childrenProcesses = ProcessUtils.findChildrenProcesses()
        (gone, still_alive) = ProcessUtils.killProcesses(childrenProcesses)

        print(f'Children processes: ')
        print(*childrenProcesses, sep='\n')
        print(f'Killed processes: {len(gone)}, Still alive: {len(still_alive)}')


    def restartServerOnFolderChanges(self):
        try:
            prev = Folder.getFolderSnapshot(self.folder)
            subprocess.Popen(self.command, shell=True)
            
            while(True):
                time.sleep(self.interval)
                curr = Folder.getFolderSnapshot(self.folder)
                if Folder.folderHasChanges(prevSnapShot=prev, currSnapshot=curr):
                    self.killServerProcesses()
                    subprocess.Popen(self.command, shell=True)
                    prev = curr
        except Exception:
            print('restartServerOnFolderChanges exception')

    