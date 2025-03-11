from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtlesim_square'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/launch', ['launch/demo_launch.py']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='juanito_7',
    maintainer_email='juanito_7@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "draw_square_service  = turtlesim_square.turtle_service_node:main",
            "draw_square_action = turtlesim_square.draw_square_action:main",
            "turtle_square_with_params = turtlesim_square.turtle_square_with_params:main",  


        ],
    },
    
)
