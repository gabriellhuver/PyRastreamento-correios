from PyRastreamentoCorreios import rastrear


statusList = rastrear('CODIGO')
for status in statusList:
    print(status)