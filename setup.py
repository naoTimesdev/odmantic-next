import setuptools

__name__ = "odmantic"
__version__ = "0.3.6"


setuptools.setup(
    name=__name__,
    version=__version__,
    author="art0409",
    author_email="arthur.pastel@gmail.com",
    description="ODMantic, an AsyncIO MongoDB Object Document Mapper for Python using type hints",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/art049/odmantic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Object Brokering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "Framework :: AsyncIO",
        "Environment :: Web Environment",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
    ],
    python_requires=">=3.6,<4.0",
    install_requires=[
        "pydantic>=1.6.2,!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<1.9.0",
        "motor>=2.5.0,<2.6.0",
    ],
    extras_require={"extras": ["fastapi=0.61.1,<0.67.0"]},
    license="ISC",
)
