import re
import os
import subprocess

def get_absolute_path(relative_path):
    """
    根据相对路径获取绝对路径

    参数:
    relative_path (str): 相对路径

    返回:
    str: 绝对路径
    """
    return os.path.abspath(relative_path)

def get_protocol_and_domain(url):
    # 使用正则表达式匹配协议和域名
    match = re.search(r'^(https?://)?([^/:]+)', url)
    
    if match:
        protocol = match.group(1) or 'http://'  # 如果没有找到协议,默认为'http://'
        domain = match.group(2)
        return protocol.rstrip('//'), domain  # 移除协议末尾的'//'
    else:
        return None, None
    

def execute_shell_command(command):
    try:
        # 使用subprocess.run()函数执行shell命令
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        # 如果执行过程中发生异常,可以在这里处理
        pass