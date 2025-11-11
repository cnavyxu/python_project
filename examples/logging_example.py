"""
日志模块使用示例
"""

from src.logging import get_logger, setup_logging, LogConfig, configure_module_logger


def basic_usage():
    """基本使用示例"""
    print("=== 基本使用 ===")
    logger = get_logger()

    logger.debug("这是调试信息")
    logger.info("这是普通信息")
    logger.warning("这是警告信息")
    logger.error("这是错误信息")
    logger.critical("这是严重错误信息")


def custom_config():
    """自定义配置示例"""
    print("\n=== 自定义配置 ===")

    config = LogConfig(
        name="custom_logger",
        level="DEBUG",
        format="[%(levelname)s] %(asctime)s | %(name)s | %(message)s",
        date_format="%H:%M:%S",
        log_dir="logs",
        log_file="custom.log",
        console_output=True,
        file_output=True,
        rotation_type="size",
        max_bytes=5 * 1024 * 1024,  # 5MB
        backup_count=3,
    )

    logger = setup_logging(config)
    logger.info("这是使用自定义配置的日志")


def module_logger():
    """模块专用 Logger 示例"""
    print("\n=== 模块专用 Logger ===")

    logger = configure_module_logger(
        module_name="my_algorithm", level="INFO", console_output=True, file_output=True
    )

    logger.info("算法开始执行")
    logger.debug("这是调试信息（不会显示，因为级别是 INFO）")
    logger.info("算法执行完成")


def exception_logging():
    """异常日志示例"""
    print("\n=== 异常日志 ===")

    logger = get_logger("exception_demo")

    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.error("发生除零错误", exc_info=True)

    try:
        data = [1, 2, 3]
        value = data[10]
    except IndexError as e:
        logger.exception("索引错误")  # exception() 自动包含堆栈信息


def structured_logging():
    """结构化日志示例"""
    print("\n=== 结构化日志 ===")

    logger = get_logger("structured")

    user_id = 12345
    action = "login"
    ip_address = "192.168.1.100"

    logger.info(
        f"用户操作 | user_id={user_id} | action={action} | ip={ip_address} | status=success"
    )


def algorithm_example():
    """算法中使用日志的示例"""
    print("\n=== 算法中使用日志 ===")

    logger = get_logger("sorting")

    def quick_sort(arr, depth=0):
        indent = "  " * depth
        logger.debug(f"{indent}quick_sort 调用，数组长度: {len(arr)}")

        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        logger.debug(
            f"{indent}分区: left={len(left)}, middle={len(middle)}, right={len(right)}"
        )

        return quick_sort(left, depth + 1) + middle + quick_sort(right, depth + 1)

    logger.info("开始排序")
    data = [3, 6, 8, 10, 1, 2, 1]
    logger.info(f"输入数据: {data}")

    result = quick_sort(data)

    logger.info(f"排序结果: {result}")
    logger.info("排序完成")


def performance_logging():
    """性能日志示例"""
    print("\n=== 性能日志 ===")

    import time

    logger = get_logger("performance")

    def timed_operation(name, duration):
        logger.info(f"开始操作: {name}")
        start_time = time.time()

        time.sleep(duration)

        elapsed = time.time() - start_time
        logger.info(f"操作完成: {name} | 耗时: {elapsed:.4f}秒")

    timed_operation("数据加载", 0.1)
    timed_operation("模型训练", 0.2)
    timed_operation("结果保存", 0.05)


if __name__ == "__main__":
    print("日志模块使用示例\n")

    basic_usage()
    custom_config()
    module_logger()
    exception_logging()
    structured_logging()
    algorithm_example()
    performance_logging()

    print("\n日志文件已保存到 logs/ 目录")
