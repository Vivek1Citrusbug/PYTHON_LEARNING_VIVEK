import multiprocessing
import multiprocessing.pool
import multiprocessing.process
import os
import threading
import concurrent.futures
import asyncio
import time

# def worker1(name):
#     '''Function runs worker1'''
    
#     print("Worker 1 running ... ")

# def worker2(name):
#     '''Function runs worker2'''
    
#     print("Worker 2 running ... ")

# def sum_of_number(input_array,shared_array,sum_of_value):
#     '''Function gives sum of squares of input array'''

    
#     for idx,value in enumerate(input_array):
#         shared_array[idx] = value * value

#     sum_of_value.value = sum(shared_array)
#     print('In process P3, shared array : ',shared_array)
#     print('In process P3, sum of value : ',sum_of_value.value)

# def insert_element(new_record,records):
#     '''function to insert record in list'''

#     records.append(new_record)
#     print("New record added!\n") 

# def print_server_data(records):
#     '''Function to print data'''

#     for record in records:
#         print(f'Name : {record[0]} Score : {record[1]}')

# def square_list(my_list, my_queue): 
#     """ 
#     function to square a given list 
#     """
#     # append squares of mylist to queue 
#     for num in my_list: 
#         my_queue.put(num * num) 
  
# def print_queue(my_queue): 
#     """ 
#     function to print queue elements 
#     """
#     print("Queue elements:") 
#     while not my_queue.empty(): 
#         print(my_queue.get()) 
#     print("Queue is now empty!")

# def sender(connection,message):
#     for i in message:
#         connection.send(i)
#         print('\nSent : ',i)
#     connection.close()

# def receiver(connection):
#     while True:
#         message = connection.recv()
#         if message == "END":
#             break
#         print('\nReceived : ',message)

# def withdraw(balance,lock):     
#     for _ in range(10000): 
#         lock.acquire()
#         balance.value = balance.value - 1
#         lock.release()
   
# def deposit(balance,lock):     
#     for _ in range(10000): 
#         lock.acquire()
#         balance.value = balance.value + 1
#         lock.release()
  
# def perform_transactions(): 
  
#     balance = multiprocessing.Value('i', 100) 
    
#     lock = multiprocessing.Lock() 

#     p1 = multiprocessing.Process(target=withdraw, args=(balance,lock,)) 
#     p2 = multiprocessing.Process(target=deposit, args=(balance,lock,)) 
  
#     p1.start() 
#     p2.start() 
  
#     p1.join() 
#     p2.join() 
  
#     print("Final balance = {}".format(balance.value)) 

# def square(n):
#     print("\nWorker process id for {0}: {1}".format(n, os.getpid())) 
#     return (n*n) 

# def worker():
#     print("Worker thread started")

# def task1():
#     print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 1: {}".format(os.getpid()))

# def task2():
#     print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 2: {}".format(os.getpid()))

if __name__ == '__main__':
    # p1 = multiprocessing.Process(target=worker1,args=("Worker 1",))
    # p2 = multiprocessing.Process(target=worker2,args=("Worker 2",))
    # print("Parent Process (Main) Id : ",os.getpid())

    # p1.start()
    # p2.start()

    # print("Process ID of worker1 : ",p1.pid)
    # print("Process ID of worker2 : ",p2.pid)

    # p1.join()
    # p2.join()

    # print("Both process finished execution!")

    # print("Is P1 process alive ? ",p1.is_alive())
    # print("Is P2 process alive ? ",p2.is_alive())

    # temp_list = [1,2,3,4]
    # shared_array = multiprocessing.Array('i',4)
    # sum_of_array = multiprocessing.Value('i')

    # p3 = multiprocessing.Process(target=sum_of_number,args=(temp_list,shared_array,sum_of_array,))
    # p3.start()
    # p3.join()
    # print('In main Process, shared array :  ', shared_array)
    # print('In main process, sum of array : ',sum_of_array.value)

    # with multiprocessing.Manager() as manager:
    #     records = manager.list([('Vivek',10),('Mit',20),('Soni',30),('Ahmedabad',40)])
    #     new_record = ('New record',100)
    #     p1 = multiprocessing.Process(target=insert_element,args=(new_record,records,))
    #     p2 = multiprocessing.Process(target=print_server_data,args=(records,))
    #     p1.start()
    #     p2.start()

    #     p1.join()
    #     p2.join()

    #--------- Different ways to communicate between process ---------------
    # Queue :-----

    # my_list = [1,2,3,4] 
  
    # # creating multiprocessing Queue 
    # my_queue = multiprocessing.Queue()
  
    # # creating new processes 
    # p1 = multiprocessing.Process(target=square_list, args=(my_list, my_queue)) 
    # p2 = multiprocessing.Process(target=print_queue, args=(my_queue,)) 
  
    # # running process p1 to square list 
    # p1.start() 
    # p1.join() 
  
    # # running process p2 to get queue elements 
    # p2.start() 
    # p2.join() 

    # Pipe :-----
    # msgs = ["hello", "my", "name", "Vivek", "Soni","END"]
    # first_end,second_end = multiprocessing.Pipe()
    
    # p1 = multiprocessing.Process(target=sender, args=(first_end,msgs)) 
    # p2 = multiprocessing.Process(target=receiver, args=(second_end,)) 
  
    # p1.start() 
    # p2.start() 
  
    # p1.join() 
    # p2.join() 

    # for i in range(10): 
    #     perform_transactions() 

    #Pooling in multiprocessing --------------------
    # my_list = [1,2,3,4,5,6,7,8,9,0]
    # p = multiprocessing.Pool()
    # result = p.map(square,my_list)
    # print(result)

    # pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # pool.submit(worker)
    # pool.submit(worker)
    # pool.shutdown(wait=True)
    # print("main thread continues ... ")

    # print("ID of process running main program: {}".format(os.getpid()))

    # print("Main thread name: {}".format(threading.current_thread().name))

    # t1 = threading.Thread(target=task1, name='thread 1')
    # t2 = threading.Thread(target=task2, name='thread 2')

    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()
    
    # async def download_file(name,duration):
    #     print("\nDownloading file : ",name)
    #     await asyncio.sleep(duration)
    #     print("\nDownload completed, ",name)
    
    # async def main():
        # task1 = asyncio.create_task(download_file("File1",5))
        # task2 = asyncio.create_task(download_file("File2",1))

        # await task1
        # await task2
        # await asyncio.gather(
        #     download_file("File1",4),
        #     download_file("File2",3),
        #     download_file("File3",9),
        #     download_file("File4",3),
        #     download_file("File5",6),
        #     download_file("File6",1)
        # )

    #     print("\nAll downloads completed")

    # asyncio.run(main())

    # async def set_future_result(future):
    #     print("Simulating a task...")
    #     await asyncio.sleep(2)  # Simulate a delay
    #     future.set_result("Task completed!")

    # async def main():
    #     future = asyncio.Future()
    #     asyncio.create_task(set_future_result(future))
        
    #     print("Waiting for the result...")
    #     result = await future  # Wait until the future has a result
    #     print(result)

    # asyncio.run(main())

    # async def async_function():
    #     await asyncio.sleep(1)
    #     return "Async result"

    # def main():
    #     loop = asyncio.get_event_loop()  # Get the running event loop
    #     result = loop.run_until_complete(async_function())
    #     print(result)

    # main()

    # def sync_task(name):
    #     time.sleep(5)
    #     return f"Sync {name}"

    # async def async_task(name):
    #     await asyncio.sleep(1)
    #     return f"Async {name}"

    # async def main():
    #     start_time = time.time()
    #     sync_result = asyncio.to_thread(sync_task, "Task 1")
    #     async_result = async_task("Task 2")

    #     results = await asyncio.gather(sync_result, async_result)
    #     print("Difference : ",time.time()-start_time)
    #     print(results)

    # asyncio.run(main())

