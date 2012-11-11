from setuptools import setup


setup(
    name='omitted',
    version='0.1.2',
    url='https://github.com/rconradharris/omitted',
    license='MIT',
    author='Rick Harris',
    author_email='rconradharris@gmail.com',
    description='A Do-Not-Care Value for Python',
    long_description=__doc__,
    py_modules=['omitted'],
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
