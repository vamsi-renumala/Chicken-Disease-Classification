import setuptools

with open('README.md', 'r', encoding='utf-8' ) as f:
    long_description = f.read()


__version__ = '0.0.0'
AUTHOR_NAME = 'Vamsi'
SRC_REPO = 'CnnClassifier'
AUTHOR_EMAIL = 'vamsirenumala000@gmail.com'
REPO_NAME = 'Chicken-Disease-Classification'

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    description = 'A small python package for CNN App',
    Long_description = long_description,
    Long_description_content = 'text/markdown',
    url = f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    project_urls = {
        "Bug Tracker": f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues'
    },
    package_dir = {'': 'src'},
    pakages = setuptools.find_packages(where='src')
)
