from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except Exception:
    long_description = ''

setup(
    name='esl-redis',
    author='Moshe Zada',
    version='0.3.0',
    py_modules=['esl_redis'],
    keywords=['elastic', 'elasticsearch', 'esl', 'redis', 'bulk', 'loader'],
    url='https://github.com/moshe/elasticsearch_loader',
    license='',
    long_description=long_description,
    description='elasticsearch_loader plugin for redis',
    install_requires=[
        'elasticsearch-loader',
        'redis'
    ],
    tests_require=[
        'pytest'
    ],
    entry_points='''
        [esl.plugins]
        register=esl_redis:register
    '''
)
