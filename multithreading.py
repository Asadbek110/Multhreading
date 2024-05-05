import threading

import time
#
#
# def fun1():
#     for i in range(7):
#         print(f"number=> {i}")
#         time.sleep(1.5)
#
#
# def fun2():
#     for i in "Thomas":
#         print(f"=====> {i}")
#         time.sleep(1.5)
#
#
# thread1 = threading.Thread(target=fun1)
# thread2 = threading.Thread(target=fun2)
#
#
# start = time.time()
# thread1.start()
#
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# end = time.time()


# print("Process finished in total time => ", {end-start})

def say_hi(name):
    print(f"Hi {name}")
    time.sleep(3)


def func(n):
    for i in range(1, n):
     print(i**2)
     time.sleep(2)


t1 = threading.Thread(target=say_hi, args=("Thomas",))
t2 = threading.Thread(target=func, args=(5,))

t1.start()
t2.start()

t1.join()
t2.join()

