from distribute_manager import DistributeProcess
import time 
import numpy as np 
import random 
if __name__ == "__main__":
    host = '127.0.0.1'
    port1 = 50001 

    authkey = "authkey"
    manager = DistributeProcess.make_queue_server_client(host, port1, authkey)

    queue = manager.get_queue()
    while True:
        hight = random.randint(100,300)
        width = random.randint(100,300)
        image = np.random.randint(0, 255, (hight, width, 3), dtype=np.uint8)
        queue.put(image)
        time.sleep(0.02)