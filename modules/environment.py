import os

def run(**args):
    print("[*] In environment module")
    # 获取运行该脚本的系统的系统环境变量
    environ = os.environ

    return str(environ)
