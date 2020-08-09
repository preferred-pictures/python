from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='preferred_pictures',
    packages=['preferred_pictures'],
    version='0.3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    description='A client for the PreferredPictures API that makes integration easy',
    author='Preferred.pictures',
    author_email='contact@preferred.pictures',
    url='https://github.com/preferred-pictures/python',
    download_url='https://github.com/preferred-pictures/python/archive/v_02.tar.gz',
    keywords=['preferred.pictures', 'optimization'],
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
