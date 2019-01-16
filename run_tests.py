import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from unittest import defaultTestLoader
from db_fixture import test_data
from HTMLTestRunner.HTMLTestRunner_Chart import HTMLTestRunner

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":
    test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = 'test_result.html'
    fp = open('test_result.html', 'wb+')
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="测试报告",
                      # description="用例执行情况",
                            tester='test01',
                            retry=1,
                            save_last_try=True
                            )
runner.run(testsuit)
fp.close()
