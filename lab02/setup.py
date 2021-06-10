from distutils.core import setup

setup(
    name="jpty",
    version="2.0",
    description="Module for (de)serializing Json/Pickle/Toml/Yaml data",
    author="Ivan Ilyushchanka",
    author_email="ginvaelwf@mail.ru",
    packages=["json_parser", "pickle_parser", "toml_parser", "yaml_parser",
              "Utilities", "JptySerializer"],
    install_requires=["dill", "pytomlpp", "pyyaml"],
    scripts=["jptyapp.py"]
)
