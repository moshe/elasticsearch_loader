from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except Exception:
    long_description = ''

setup(
    name='elasticsearch-loader',
    author='Moshe Zada',
    version='0.1.0',
    py_modules=['elasticsearch_loader'],
    keywords=['elastic', 'elasticsearch', 'csv', 'json', 'parquet', 'bulk', 'loader'],
    url='https://github.com/Moshe/elasticsearch_loader',
    license='',
    long_description=long_description,
    description='A pythonic tool for batch loading data files (json, parquet, csv, tsv) into ElasticSearch',
    install_requires=[
        'elasticsearch',
        'click',
        'click-stream',
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
