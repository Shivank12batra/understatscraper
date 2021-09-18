from setuptools import setup, find_packages

setup(
  name = 'understatscraper',
  packages = find_packages(),
  version = '0.0.2',
  license='MIT License',
  description = 'A Python package to scrape shots data from understat.com for either a single game or a whole season.',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  author = 'Shivank Batra',
  author_email = 'Shivank56batra@gmail.com',
  url = 'https://github.com/Shivank12batra/understatscraper',
  install_requires=[
          'numpy',
          'pandas',
          'requests',
          'bs4',
          'lxml'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
  ],
)
