import multiprocessing as mp
import time

def func(values):
    for i in range(5):
        print('from func ',values.value)
        values.value+=int(3.3)
                
def func2(values):
    for i in range(5):
        print('from func2 ',values.value)
        values.value+=int(2.4)

if __name__ == "__main__":
    x = mp.Value('i',1)

    p1 = mp.Process(target=func,args=(x,))
    p2 = mp.Process(target=func2,args=(x,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('in main function ',x.value)

