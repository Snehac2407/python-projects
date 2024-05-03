import time  #how much time my program is taking to execute
# def doubles(number):
#     for n in number:
#         time.sleep(1)
#         print("Double",2*n)
# def squares(number):
#     for n in number:
#         time.sleep(1)
#         print("squares",n*n)
# numbers = [1,2,3,4,5]
# beginTime = time.time()
# doubles(numbers)
# squares(numbers)
# print("totla time taken",time.time()-beginTime)

#
# import threading
# def doubles(number):
#     for n in number:
#         time.sleep(1)
#         print("Double",2*n)
# def squares(number):
#     for n in number:
#         time.sleep(1)
#         print("squares",n*n)
# numbers = [1,2,3,4,5]
# beginTime = time.time()
# t1 = threading.Thread(target=doubles,args=(numbers,))
# t2 = threading.Thread(target=squares,args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("totla time taken",time.time()-beginTime)


# example of getting the main thread for child processes
# from multiprocessing import current_process
# from multiprocessing import Process
# from threading import main_thread
# def task():
#     process = current_process()   # get the current process
#     thread = main_thread()    # get the main thread for the main process
#     print(f'Process: {process.name}, main thread: {thread}')
# if __name__ == '__main__':
#     children = [Process(target=task) for _ in range(5)]     # create child processes
#     for child in children:    # start child processes
#         child.start()
#     for child in children:    # wait for children processes to terminate
#         child.join()


# wap to set thread name also change mainthread name and get process id and thread id number:-

from threading import Thread,current_thread
import os
def display():
    for i in range(4):
        print("hye sneha choudhary")
def show():
    for i in range(3):
        print("these threading is worst then threading ")
T1=Thread(target=display)
T2=Thread(target=show)
T1.start()
T2.start()
T1.setName("suggesion")
print(T1.name)
current_thread().name="no need"
print(current_thread().name)
print(T1.ident)
print(T1.ident)
print(T1.native_id)
os.getpid()
