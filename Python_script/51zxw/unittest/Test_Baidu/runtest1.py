import unittest
from HTMLTestRunner import HTMLTestRunner
import time
# 定义测试用例路径
test_dir = './test_case'
discovery = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__ == '__main__':
    # 存放报告文件夹
    report_dir = './test_report'
    # 报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H.%M.%S")
    # 报告文件完整路径
    report_name = report_dir + '/' + now + ' result.html'
    # 打开文件在报告文件写入测试结果
    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title='Test Report', description="Test case Report")

        runner.run(discovery)
    f.close()
