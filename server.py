from multiprocessing import Queue
from multiprocessing.managers import SyncManager

class CreateDistributeProcessServer:
    QueueMaxSize = 3
    def make_queue_manager(self, host:str, port:int, authkey:str):
        q = Queue(CreateDistributeProcessServer.QueueMaxSize)
        class QueueManager(SyncManager):
            pass 
        manager = QueueManager(address=(host,port), authkey= bytes(authkey, 'utf-8'))
        s = manager.get_server()
        s.serve_forever()