from setuptools import setup
setup(
    name = 'blockdrm',
    version = '0.1.0',
    packages = ['blockdrm'],
    entry_points = {
        'console_scripts': [
            'blockdrm = blockdrm.__main__:main'
        ]
    })