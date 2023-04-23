import setuptools
with open("README.md",r) as rd:
    long_description = rd.read()
setuptools.setup(name = "outageapp", version = "0.1", \
      description ="This is a Python program that interacts with an API to manage outages" ,\
      long_description = long_description,author = "sarath", \
      author_email="sarathchandra.digavalli@gmail.com",\
        install_requirements= ["requests==2.28.2","PyYAML==6.0","configparser==5.1","pytest==7.3.1"],\
      packages = setuptools.find_packages(), python_requires = "==3.11.3")

