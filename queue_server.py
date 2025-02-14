from distribute_manager import DistributeProcess
import threading
import time 
def main():
    host = '127.0.0.1'
    port1 = 50001 

    authkey = "authkey"
    server_manager = DistributeProcess()
    server_manager.make_queue_manager(host, port1, authkey)
    print("START MANAGER")
    # server1 = threading.Thread(target=server_manager.make_queue_manager, args=(host, port1, authkey))
    # server1.start()

    # while True:
    #     time.sleep(300)
        
if __name__ == "__main__":
    main()