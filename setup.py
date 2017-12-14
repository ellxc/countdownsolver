from setuptools import setup, find_packages





setup(
    name='countdownsolver',

    version='1.0.0',

    description='a fast and efficient countdown numbers game solver written in python',

    url='https://github.com/ellxc/countdown',

    author='Elliot Carr',
    author_email='ec486@kent.ac.uk',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',


    ],

    # What does your project relate to?
    keywords='maths solver countdown numbers game',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
)