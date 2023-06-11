import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()    
    
__version__ ="0.0.0"

REPO_NAME = "Text_summarization-Project"
AUTHOR_USERNAME = "SaviourSCS"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "shubhamchamdrasaurabh1@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USERNAME,
    author_email = AUTHOR_EMAIL,
    description = "Text Summarizer",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/SaviourSCS/Text_summarization-Project",
    packages = setuptools.find_packages(where="src")
)