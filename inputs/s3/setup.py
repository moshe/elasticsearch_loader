from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except Exception:
    long_description = ''

setup(
    name='esl-s3',
    author='Moshe Zada',
    version='0.3.0',
    py_modules=['esl_s3'],
    keywords=['elastic', 'elasticsearch', 'esl', 's3', 'bulk', 'loader', 'boto', 'aws', 'cloud'],
    url='https://github.com/moshe/elasticsearch_loader',
    license='',
    long_description=long_description,
    description='elasticsearch_loader plugin for AWS s3',
    install_requires=[
        'elasticsearch-loader',
        'boto3'
    ],
    tests_require=[
        'pytest'
    ],
    entry_points='''
        [esl.plugins]
        register=esl_s3:register
    '''
)
