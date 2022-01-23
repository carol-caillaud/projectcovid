import numpy as np
import matplotlib.pyplot as plt
faixa_etaria = ('18-25','26-35','36-45','46-55','55+')
renda = [1805.45,2458,12,3752.15,4120.89,3486.22]
plt.bar (faixa_etaria, renda)
#plt.ylim(ymin=0)
#plt.xlim(xmin=0.0)
plt.pyplot.ylim(0, 50000)
#legenda de cada barra no eixo x
plt.xticks (faixa_etaria)
plt.ylabel ('Renda média')
plt.xlabel ('Faixa etária (anos)')
plt.title('Renda média x Faixa etária no Brasil')
plt.show()
