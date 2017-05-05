from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except Exception:
    long_description = ''

setup(
    name='elasticsearch-loader',
    author='Moshe Zada',
    version='0.2.2',
    packages=['elasticsearch_loader'],
    keywords=['elastic', 'elasticsearch', 'csv', 'json', 'parquet', 'bulk', 'loader'],
    url='https://github.com/Moshe/elasticsearch_loader',
    license='',
    long_description=long_description,
    description='A pythonic tool for batch loading data files (json, parquet, csv, tsv) into ElasticSearch',
    install_requires=[
        'elasticsearch',
        'click',
        'click-stream==0.0.4',
        'futures'
    ],
    tests_require=[
        'pytest',
        'mock'
    ],
    extras_require={
        'parquet': ['parquet']
    },
    entry_points={
        'console_scripts': [
            'elasticsearch_loader = elasticsearch_loader:main',
        ]
    }
)
