from setuptools import setup

setup(
    name='clickhouse orm extended',
    version='2.1.4a0',
    author='Ivan Alexeev',
    author_email='ivan_alexeev@realytics.team',
    description='Extended version of infi.clickhouse-orm',
    url='https://github.com/Ninefiveblade/infi.clickhouse-orm-extended',
    packages=['infi'],
    python_requires='>=3.9',
    install_requires=[
        'iso8601 >= 0.1.12',
        'pytz',
        'requests',
        'setuptools'
    ],
)
