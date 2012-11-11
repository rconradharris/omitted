from setuptools import setup


setup(
    name='notset',
    version='0.1.1',
    url='https://github.com/rconradharris/notset',
    license='MIT',
    author='Rick Harris',
    author_email='rconradharris@gmail.com',
    description='A Do-Not-Care Value for Python',
    long_description=__doc__,
    py_modules=['notset'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[''],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
