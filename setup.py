from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'phlogo',        
  packages = ['phlogo'],
  include_package_data=True,
  version = '0.6',    
  license='MIT',     
  description = 'Pornhub Logo Generator', 
  author = 'Krypton Byte',                  
  author_email = 'galaxyvplus6434@gmail.com',     
  url = 'https://github.com/krypton-byte/drawHub',   
  download_url = 'https://github.com/krypton-byte/drawHub/archive/0.0.1.tar.gz',    
  keywords = ['pornhub', 'logo', 'generator'], 
  install_requires=[           
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
