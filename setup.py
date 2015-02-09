try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'pysec',
    'version': '0.1.211',
    'author': 'Martin Thoma',
    'author_email': 'info@martin-thoma.de',
    'maintainer': 'Martin Thoma',
    'maintainer_email': 'info@martin-thoma.de',
    'packages': ['pysec'],
    'scripts': ['bin/pysec'],
    'package_data': {'pysec': ['templates/*', 'misc/*']},
    'platforms': ['Linux', 'MacOS X', 'Windows'],
    'url': 'https://github.com/MartinThoma/pysec',
    'license': 'MIT',
    'description': 'Tool to get stolen notebook back.',
    'long_description': "A tookit to get your notebook back if it was stolen",
    'install_requires': [
        "NetworkManager",
        "SimpleCV",
        "six"
    ],
    'keywords': ['pysec', 'security', 'notebook'],
    'download_url': 'https://github.com/MartinThoma/pysec',
    'classifiers': ['Development Status :: 3 - Alpha',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Natural Language :: English',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.3',
                    'Programming Language :: Python :: 3.4',
                    'Topic :: Software Development',
                    'Topic :: Utilities'],
    'zip_safe': False,
    'test_suite': 'nose.collector'
}

setup(**config)
