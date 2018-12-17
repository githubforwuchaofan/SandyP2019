# -*- coding: utf-8 -*-

"""
Author: create by wuchaofan
Date: 2017-04-25 09:05
Email: wuchaofan@txcap.com
"""

import queue
import threading

import time


class Worker(threading.Thread):
    def __init__(self, work_queue, result_queue, **kwds):
        threading.Thread.__init__(self, **kwds)
        self.setDaemon(True)
        self.workQueue = work_queue
        self.resultQueue = result_queue
        self.lock = threading.Lock()

    def run(self):

        while True:
            try:
                task_request, args, kwds = self.workQueue.get(False)
                res = task_request(*args, **kwds)
                self.resultQueue.put(res)
            except queue.Empty:
                break


# 线程池管理\创建
class WorkManager:
    def __init__(self, num_of_workers):
        print(self.__dict__)

        # 请求队列
        self.workQueue = queue.Queue()
        # 输出结果的队列
        self.resultQueue = queue.Queue()
        self.workers = []
        self.recruit_threads(num_of_workers)

    def recruit_threads(self, num_of_workers):

        for i in range(num_of_workers):
            # 创建工作线程
            worker = Worker(self.workQueue, self.resultQueue)
            # 加入到线程队列
            self.workers.append(worker)

    def start(self):
        for w in self.workers:
            w.start()

    def wait_for_complete(self):

        while len(self.workers):

            # 从池中取出一个线程处理请求
            worker = self.workers.pop()
            worker.join()

            if worker.isAlive() and not self.workQueue.empty():
                # 重新加入线程池中
                self.workers.append(worker)

    def add_job(self, task_request, *args, **kwds):

        # 向工作队列中加入请求
        self.workQueue.put((task_request, args, kwds))

    def get_result(self, *args, **kwds):

        return self.resultQueue.get(*args, **kwds)


# 多线程执行主方法
def thread_main(method, args, counts):
    wm = WorkManager(counts)
    for arg in args:
        if isinstance(arg, dict):
            wm.add_job(method, **arg)
        elif isinstance(arg, tuple):
            wm.add_job(method, *arg)
        else:
            wm.add_job(method, arg)

    wm.start()
    wm.wait_for_complete()


if __name__ == "__main__":
    def func_add(x, y, z):
        print(x ^ y + y ^ x + y ^ z)


    args_list = [(x, y, z) for x in range(1, 10) for y in range(10, 20) for z in range(20, 30)]
    params_list = [{"x": x} for x in range(1000)]


    def func_params(x):
        print("x:", x)


    # thread_main(func_add, args_list, 20)
    thread_main(func_add, args_list, 50)
