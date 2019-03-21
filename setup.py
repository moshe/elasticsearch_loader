from setuptools import setup
import sys

extras = []
if sys.version_info.major == 2:
    extras.append('unicodecsv')

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except Exception:
    long_description = ''

setup(
    name='elasticsearch-loader',
    author='Moshe Zada',
    version='0.2.24',
    packages=['elasticsearch_loader'],
    keywords=['elastic', 'elasticsearch', 'csv', 'json', 'parquet', 'bulk', 'loader', 'redis'],
    url='https://github.com/Moshe/elasticsearch_loader',
    license='',
    long_description=long_description,
    description='A pythonic tool for batch loading data files (json, parquet, csv, tsv) into ElasticSearch',
    install_requires=['elasticsearch>=6', 'click==6.7', 'click-stream', 'click-conf', 'enum34'] + extras,
    extras_require={
        'parquet': ['parquet'],
        'redis': ['esl-redis'],
        'tests': ['pytest', 'mock'],
    },
    entry_points={
        'console_scripts': [
            'elasticsearch_loader = elasticsearch_loader:cli',
        ]
    }
)
