from setuptools import setup


if __name__ == "__main__":
    setup(
        name="ipython_autoimport",
        version="0.0",
        description="Autoimport missing modules in IPython",
        author="Antony Lee",
        license="BSD",
        classifiers=["Development Status :: 4 - Beta",
                     "Framework :: IPython",
                     "License :: OSI Approved :: BSD License",
                     "Programming Language :: Python :: 3.5"],
        py_modules=["ipython_autoimport"],
    )
