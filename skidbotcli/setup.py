from setuptools import setup

package_name = 'skidbotcli'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='steven.lavalle@gmail.com',
    description='Skidbot client',
    license='Apache 2.0 License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             'service = skidbotcli.service_member_function:main',
             'client = skidbotcli.client_member_function:main',
        ],
    },
)
