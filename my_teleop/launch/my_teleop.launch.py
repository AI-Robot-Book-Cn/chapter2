import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            prefix='xterm -e', package='my_teleop', executable='my_teleop_node', output='screen')
            ])

