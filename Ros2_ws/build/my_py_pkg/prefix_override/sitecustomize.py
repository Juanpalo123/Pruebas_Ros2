import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/juanito_7/Pruebas_Ros2/Ros2_ws/install/my_py_pkg'
