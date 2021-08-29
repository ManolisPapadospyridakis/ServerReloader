import os

class Folder():
    @staticmethod
    def getFolderSnapshot(folder):
        filesDict = dict()
        for root, dirs, files in os.walk(folder):
            for file in files:
                filepath = os.path.join(root,file)
                modification_time = os.path.getmtime(filepath)
                filesDict[filepath] = modification_time
        return filesDict

    @staticmethod
    def folderHasChanges(prevSnapShot, currSnapshot):
        newFiles = []
        modifiedFiles = []

        for file, timestamp in currSnapshot.items():
            try:
                prev_timestamp = prevSnapShot[file]
                if prev_timestamp != timestamp:
                    modifiedFiles.append(file)
            except KeyError:
                newFiles.append(file)

        if len(newFiles) > 0: print('New files:')
        for file in newFiles: print(f'\t{file}')

        if len(modifiedFiles) > 0: print('Modified files:')
        for file in modifiedFiles: print(f'\t{file}')

        return newFiles != [] or modifiedFiles != []