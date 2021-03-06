from setuptools import setup

setup(
    name='cms7',
    version='0.1a20',
    description='Simple static site generator',
    author='Ed Kellett',
    author_email='e@kellett.im',
    url='https://github.com/freenode/cms7',
    packages=['cms7', 'cms7.modules'],
    install_requires=[
        'colorlog',
        'clize',
        'feedgenerator',
        'html5lib',
        'jinja2',
        'markdown',
        'requests',
        'pathlib2',
        'python-dateutil',
        'pyyaml',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'cms7 = cms7.cli:main'
        ]
    }
)
