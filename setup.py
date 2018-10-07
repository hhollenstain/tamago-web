"""``tamago`` lives on
https://github.com/hhollenstain/tamago-web
"""
from setuptools import setup, find_packages
import tamago_web

INSTALL_REQUIREMENTS = [
    'coloredlogs',
    'flask',
    'waitress',
]

TEST_REQUIREMENTS = {
    'test':[
        'pytest',
        'pylint',
        'sure',
        ]
    }

setup(
    name='Tamago Web',
    version=tamago_web.VERSION,
    description='Tamago web for Tamago Discord Bot',
    url='https://github.com/hhollenstain/tamago-web',
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIREMENTS,
    extras_require=TEST_REQUIREMENTS,
    entry_points={
        'console_scripts':  [
            'tamago_web = tamago_web.tamago_web:main',
        ],
    },
    )
