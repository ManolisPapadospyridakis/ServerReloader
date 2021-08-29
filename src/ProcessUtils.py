import psutil

class ProcessUtils:
    @staticmethod
    def findChildrenProcesses():
        currentProcess = psutil.Process()
        childrenProcesses= currentProcess.children(recursive=True)
        return childrenProcesses

    @staticmethod
    def killProcesses(processes):
        for process in processes:
            process.kill()
        gone, still_alive = psutil.wait_procs(processes, timeout=5)
        return (gone, still_alive)