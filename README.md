### PyRastreamento-correios
Biblioteca de rastreamento de objetos em python utilizando webscrap

### Requerimento

[Python 3.7](https://www.python.org/downloads/release/python-370/)

### Instalação
```shell
pip install PyRastreamentoCorreios
```

### Utilização
```python
from PyRastreamentoCorreios import rastrear

statusList = rastrear('CODIGO')
for status in statusList:
    print(status)
```
### Autor
* Gabriell Huver
