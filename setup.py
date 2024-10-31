import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0" 

REPO_NAME = "End-to-end-WasteDetection-Using-YoloV8"
AUTHOR_USER_NAME = 'Lavishgangwani'
AUTHOR_EMAIL = 'lavishgangwani22@gmail.com'
SRC_REPO = 'wasteDetection'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for computer Vision task",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages= setuptools.find_packages(),
)