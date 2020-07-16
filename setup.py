from distutils.core import setup
setup(
    name='preferred_pictures',
    packages=['preferred_pictures'],
    version='0.1',
    license='MIT',
    description='A client for the Preferred.pictures API that makes integration easy',
    author='Preferred.pictures',
    author_email='contact@preferred.pictures',
    url='https://github.com/preferred-pictures/python',
    # I explain this later on
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['preferred.pictures', 'optimization'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
