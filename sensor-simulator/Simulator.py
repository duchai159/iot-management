import random

def simulate_temperature_sensor(min_temp=0.0, max_temp=55.0):
    """
    Giả lập dữ liệu trả về của cảm biến nhiệt độ.
    
    Args:
        min_temp (float): Nhiệt độ tối thiểu (mặc định là 0.0°C).
        max_temp (float): Nhiệt độ tối đa (mặc định là 55.0°C).
    
    Returns:
        float: Giá trị nhiệt độ ngẫu nhiên trong khoảng từ min_temp đến max_temp.
    """
    return round(random.uniform(min_temp, max_temp), 2)

def simulate_humidity_sensor(min_humidity=20.0, max_humidity=80.0):
    """
    Giả lập dữ liệu trả về của cảm biến độ ẩm.
    
    Args:
        min_humidity (float): Giá trị độ ẩm tối thiểu (mặc định là 20.0%).
        max_humidity (float): Giá trị độ ẩm tối đa (mặc định là 80.0%).
    
    Returns:
        float: Giá trị độ ẩm ngẫu nhiên trong khoảng từ min_humidity đến max_humidity.
    """
    return round(random.uniform(min_humidity, max_humidity), 2)

def simulate_smoke_sensor(min_voltage=0.0, max_voltage=5.0):
    """
    Giả lập dữ liệu trả về của cảm biến khói analog.
    
    Args:
        min_voltage (float): Điện áp tối thiểu của cảm biến (mặc định là 0.0V).
        max_voltage (float): Điện áp tối đa của cảm biến (mặc định là 5.0V).
    
    Returns:
        float: Giá trị điện áp ngẫu nhiên trong khoảng từ min_voltage đến max_voltage.
    """
    return round(random.uniform(min_voltage, max_voltage), 2)

def simulate_gas_sensor(min_gas=0, max_gas=120):
    """
    Giả lập dữ liệu trả về của cảm biến khí.
    Args:
        min_gas (int): Nồng độ khí gas tối thiểu của cảm biến (mặc định là 0ppm).
        max_gas (int): Nồng độ khí gas tối đa của cảm biến (mặc định là 1000ppm).
    
    Returns:
        int: Giá trị nồng độ khí (ppm) giả lập.
    """
    # Giả lập giá trị nồng độ khí trong khoảng từ 0 đến 120 ppm
    gas_concentration = random.randint(min_gas, max_gas)
    return gas_concentration

def simulate_light_sensor(min_voltage=0.0, max_voltage=3.3):
    """
    Giả lập dữ liệu trả về của cảm biến ánh sáng.
    
    Args:
        min_voltage (float): Điện áp tối thiểu của cảm biến (mặc định là 0.0V).
        max_voltage (float): Điện áp tối đa của cảm biến (mặc định là 3.3V).
    
    Returns:
        float: Giá trị điện áp ngẫu nhiên trong khoảng từ min_voltage đến max_voltage.
    """
    return round(random.uniform(min_voltage, max_voltage), 2)
