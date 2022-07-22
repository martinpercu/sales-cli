from setuptools import setup


setup(
    name='sta',
    version='0.1',
    py_modules=['sta'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sta=sta:cli
    ''',
)