from setuptools import find_packages, setup

setup(
    name='KyberKEM-py',
    packages=find_packages(include=['KyberKEM-py']),
    version='0.1.0',
    description='Python Implementation of KyberKEM, a Post Quantum Cryptography Algorithm',
    author='Subhajit Biswas & Rohan Kalra',
    install_requires=[
        'numpy',
        'sympy',
        'cryptography',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.3'],
    test_suite='tests',
)