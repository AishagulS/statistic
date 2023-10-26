import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# считываем датасет с помощью pandas

data1 = pd.read_csv('https://stepik.org/media/attachments/lesson/8083/genetherapy.csv')



# создаем отфильтрованный датасет, в котором есть только строки с Therapy == A

therA = data1[data1['Therapy']=='A']


# создаем QQ-plot с помощью statsmodels, в качестве аргумента 'expr' из отсортированного датасета

sm.qqplot(therA['expr'], line='s')


# добавляем название графика

plt.title('Treatment A', fontsize=25)


# выводим на экран 

plt.show()