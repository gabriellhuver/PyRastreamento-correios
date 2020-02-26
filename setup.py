from distutils.core import setup
setup(
  name = 'PyRastreamentoCorreios',        
  packages = ['PyRastreamentoCorreios'],   
  version = '0.2',      
  license='MIT',        
  description = 'Biblioteca de rastreamento dos correios',   
  author = 'Gabriell Huver',                   
  author_email = 'gabriell.is.huver@gmail.com',    
  url = 'https://github.com/gabriellhuver/PyRastreamento-correios', 
  download_url = 'https://github.com/gabriellhuver/PyRastreamento-correios/archive/0.2.tar.gz', 
  keywords = ['CORREIOS', 'RASTREAMENTO', 'LINKCORREIOS'],   
  install_requires=[           
          'requests',
          'beautifulsoup4'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)