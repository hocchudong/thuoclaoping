from setuptools import setup

setup(
    name='thuoclaoping',
    version='2.0.0',
    description='Monitor Ping and HTTP',
    url='https://github.com/locvx1234/ThuoclaoPing',  # Optional
    author='LocVU, MinhKMA',  # Optional
    extras_require={
        'dev': [
            'tox',
        ],
    },
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tox ping thuoclao setuptools development',  # Optional
    packages=['thuoclao'],
)
