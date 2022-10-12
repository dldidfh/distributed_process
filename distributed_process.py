from multiprocessing import Queue
from multiprocessing.managers import SyncManager

class DistributeProcess:
    queue_max_size = 3 
    queue_call_name = 'get_queue' # call name ex) queue = client.get_queue()
    encoding_type = 'utf-8'
    
    @staticmethod
    def make_queue_manager( host:str, port:int, authkey:str):
        q = Queue(DistributeProcess.queue_max_size)
        class QueueManager(SyncManager):
            pass 
        QueueManager.register(DistributeProcess.queue_call_name, callable= lambda : q)
        manager = QueueManager(address=(host,port), authkey= bytes(authkey, DistributeProcess.encoding_type))
        s = manager.get_server()
        s.serve_forever()
        
    @staticmethod
    def make_queue_server_client(host:str, port:int, authkey:str):
        class QueueManager(SyncManager):
            pass 
        QueueManager.register(DistributeProcess.queue_call_name)
        manager = QueueManager(address=(host, port), authkey=bytes(authkey, DistributeProcess.encoding_type))
        manager.connect()
        return manager 
