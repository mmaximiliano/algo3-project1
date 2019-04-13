import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
sns.set()

#grafico complejidad de exp
df = pd.read_csv("times_fuerzaBruta_n30.csv")

# Nano -> Milli
df['time']  /= 1000000.0
df['teorica'] = 0.000007*df['n'] * 2**(df['n'])

df.plot('n', ['time', 'teorica'])

ax1 = sns.lmplot(x='time', y='teorica', data=df);
plt.xlabel("T(n)");
plt.ylabel("cota(n)");

plt.show()
