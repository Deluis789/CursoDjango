from mundoPC.Computadora import Computadora
from mundoPC.Monitor import Monitor
from mundoPC.Orden import Orden
from mundoPC.Raton import Raton
from mundoPC.Teclado import Teclado

monitor1 = Monitor('Samsung', '45px')
teclado1 = Teclado('USB', 'Dragons')
raton1 = Raton('USB', 'Fex')
compu1 = Computadora('Hp', monitor1, teclado1, raton1)


monitor2 = Monitor('Samsung', '45px')
teclado2 = Teclado('USB', 'Dragons')
raton2 = Raton('USB', 'Fex')
compu2 = Computadora('Hp', monitor1, teclado1, raton1)


computadoras1 = [compu1, compu2]
orden1 = Orden(computadoras1)
print(orden1)

monitor3 = Monitor('Samsung', '45px')
teclado3 = Teclado('USB', 'Dragons')
raton3 = Raton('USB', 'Fex')
compu3 = Computadora('Hp', monitor1, teclado1, raton1)


monitor4 = Monitor('Samsung', '45px')
teclado4 = Teclado('USB', 'Dragons')
raton4 = Raton('USB', 'Fex')
compu4 = Computadora('Hp', monitor1, teclado1, raton1)


computadoras2 = [compu3, compu4]
orden2 = Orden(computadoras2)
print(orden2)
