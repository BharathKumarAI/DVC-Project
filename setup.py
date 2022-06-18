import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "DVC-Project"
USER_NAME = "BharathKumarAI"

setuptools.setup(
    name=f"dvc-project-{USER_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email="bharath.aiexp@gmail.com",
    description="Testing the dvc components in a project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    # install_requires=[] # your dependent packages here
)
