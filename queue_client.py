from distribute_manager import DistributeProcess
import cv2 
import numpy as np 
if __name__ == "__main__":
    host = '127.0.0.1'
    port1 = 50001 

    authkey = "authkey"
    manager = DistributeProcess.make_queue_server_client(host, port1, authkey)

    queue = manager.get_queue()
    while True:
        data = queue.get()
        data = data.astype(np.uint8)
        print(data.shape)
        cv2.imshow('image', data)
        cv2.waitKey(1)