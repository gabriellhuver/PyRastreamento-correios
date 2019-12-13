from distutils.core import setup
setup(
  name = 'PyRastreamento-correios',        
  packages = ['PyRastreamento-correios'],   
  version = '0.1',      
  license='MIT',        
  description = 'Biblioteca de rastreamento dos correios',   
  author = 'Gabriell Huver',                   
  author_email = 'gabriell.is.huver@gmail.com',    
  url = 'https://github.com/gabriellhuver/PyRastreamento-correios', 
  download_url = 'https://github.com/gabriellhuver/PyRastreamento-correios/archive/first.tar.gz', 
  keywords = ['CORREIOS', 'RASTREAMENTO', 'LINKCORREIOS'],   
  install_requires=[           
          'requests',
          'beautifulsoup4',
          'time'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)