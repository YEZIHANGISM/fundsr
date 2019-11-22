import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fundsr',
    version="1.0.0",
    author='yezihangism',
    author_email='yezihangism@gmail.com',
    py_modules=['fundsr.fundsr', 'fundsr.holiday'],
    url='https://github.com/YEZIHANGISM/fundsr',
    long_description = long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
)