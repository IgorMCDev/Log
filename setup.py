from setuptools import find_packages, setup
setup(
    name='loglib',
    packages=find_packages(include=['loggerlib']),
    version='0.1.0',
    description='Customized log library',
    author='IgorMcDev',
    license='',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)