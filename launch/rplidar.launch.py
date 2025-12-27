from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                # ưu tiên by-id cho cố định thiết bị
                'serial_port': '/dev/serial/by-id//dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_00-port0',

                # THÊM DÒNG NÀY (quan trọng nhất)
                'serial_baudrate': 115200,

                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard',
            }]
        )
    ])