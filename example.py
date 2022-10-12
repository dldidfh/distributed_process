from distributed_process import DistributeProcess
import threading
import time 
def main():
    host = '127.0.0.1'
    port1 = 50001 
    port2 = 50002 
    port3 = 50003

    authkey = "authkey"
    server_manager = DistributeProcess()
    # server_manager.make_queue_manager(host, port1, authkey) #just one manager ( run forever)
    server1 = threading.Thread(target=server_manager.make_queue_manager, args=(host, port1, authkey))
    server2 = threading.Thread(target=server_manager.make_queue_manager, args=(host, port2, authkey))
    server3 = threading.Thread(target=server_manager.make_queue_manager, args=(host, port3, authkey))
    server1.start()
    server2.start()
    server3.start()
    while True:
        time.sleep(300)
        
if __name__ == "__main__":
    main()
