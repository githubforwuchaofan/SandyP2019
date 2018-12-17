# coding=utf8

"""
_author: wcf
_date: 2018/12/17-上午10:36
_desc: //ToDo
"""
import multiprocessing
import os



def _command(pic_no):
    return 'curl -ik -H "Content-Type:jpg" --data-binary @{0}.jpg ' \
           '"http://192.168.1.158:5104/v1.0/EuclideanDistance/SortResult"'.format(pic_no)

def test_face_search(pic_no):
    response = os.system(_command(pic_no))
    print(response)




if __name__ == "__main__":

    while True:

        # processes: 进程数
        pool = multiprocessing.Pool(processes=20)

        for _ in range(10):
            pool.apply_async(test_face_search, (2,))

        pool.close()
        pool.join()
