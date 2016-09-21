from setuptools import setup


setup(
    name='elasticsearch_loader',
    version='0.1',
    py_modules=['elasticsearch_loader'],
    url='',
    license='',
    description='',
    install_requires=[
        'elasticsearch',
        'click',
        'futures'
    ],
    tests_require=[
        'pytest'
    ],
    extras_require={
        'parquet': ['parquet']
    },
    entry_points={
        'console_scripts': [
            'elasticsearch_loader = elasticsearch_loader:cli',
        ]
    }
)
