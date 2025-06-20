'''
Author: HDJ
StartDate: please fill in
LastEditTime: 2025-06-12 22:31:34
Description: 项目通用方法

				*		写字楼里写字间，写字间里程序员；
				*		程序人员写程序，又拿程序换酒钱。
				*		酒醒只在网上坐，酒醉还来网下眠；
				*		酒醉酒醒日复日，网上网下年复年。
				*		但愿老死电脑间，不愿鞠躬老板前；
				*		奔驰宝马贵者趣，公交自行程序员。
				*		别人笑我忒疯癫，我笑自己命太贱；
				*		不见满街漂亮妹，哪个归得程序员？    
Copyright (c) 2024-2025 by HDJ, All Rights Reserved. 
'''
import time
import random
from functools import wraps
from typing import Optional, Union, List, Dict
from urllib.parse import urlparse, parse_qs, unquote


from .logger import get_logger
LOG = get_logger()

def extract_url_parameter(
    url: str,
    param_name: str,
    *,
    default: Optional[str] = None,
    all_values: bool = False
) -> Union[str, List[str], None]:
    """
    从URL中提取并解码指定参数的值
    
    Args:
        url: 包含查询参数的URL字符串
        param_name: 要提取的参数名称
        default: 参数不存在时返回的默认值，默认为None
        all_values: 是否返回所有参数值（当参数出现多次时），默认为False
        
    Returns:
        如果all_values为False：返回单个参数值（字符串）或默认值
        如果all_values为True：返回所有参数值的列表或空列表
    """
    try:
        # 解析URL
        parsed_url = urlparse(url)
        # 解析查询字符串
        query_params = parse_qs(parsed_url.query)
        # 检查参数是否存在
        if param_name in query_params:
            # 获取参数值列表
            values = query_params[param_name]
            if all_values:
                # 返回所有解码后的值
                return [unquote(value) for value in values]
            else:
                # 只返回第一个值（通常情况）
                return unquote(values[0])
        # 参数不存在，返回默认值
        return default
    except Exception as e:
        # 发生异常时返回默认值
        return default

def sync_retry(max_retries=3, retry_delay=2, backoff_factor=2, exceptions=(Exception,)):
    """
    重试装饰器
    - max_retries: 最大重试次数
    - retry_delay: 初始延迟时间（秒）
    - backoff_factor: 退避系数（指数退避）
    - exceptions: 需要重试的异常类型元组
    """
    def decorator(func):    # 装饰器工厂函数，接收外部参数（如重试次数）
        @wraps(func)    # 保留原函数元信息（__name__、__doc__）
        def wrapper(*args, **kwargs): # 包装函数，实际执行时替换原函数
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retries += 1
                    if retries >= max_retries:
                        raise   # 保留完整的异常跟踪栈
                    
                    # 计算等待时间（指数退避 + 随机抖动）
                    wait_time = retry_delay * (backoff_factor ** (retries - 1))
                    jitter = random.uniform(0, wait_time * 0.5)  # 随机抖动
                    wait_time += jitter
                    
                    LOG.warning(f"Func {func.__name__} failed ({e})，{wait_time:.1f}秒后重试 ({retries}/{max_retries})......")
                    time.sleep(wait_time)
        return wrapper
    return decorator