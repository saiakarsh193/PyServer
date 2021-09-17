import threading

class sharedMem:
    def __init__(self, val):
        self.mutex = threading.Lock()
        self.val = val

    def lock(self):
        self.mutex.acquire()
    
    def unlock(self):
        self.mutex.release()

    def __len__(self):
        if(isinstance(self.val, list)):
            return len(self.val)
        else:
            return -1

    def __getitem__(self, key):
        if(isinstance(self.val, list)):
            return self.val[key]
        else:
            return -1
    
    def __str__(self):
        return str(self.val)