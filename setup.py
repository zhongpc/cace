from setuptools import setup, find_packages

setup(
    name='CACE',
    version='0.1.0',
    author='Bingqing Cheng',
    author_email='tonicbq@gmail.com',
    description='Cartesian Atomic Cluster Expansion Machine Learning Potential',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'ase',
        'torch',
        'matscipy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

