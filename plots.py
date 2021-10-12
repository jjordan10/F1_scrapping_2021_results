import numpy as np
import matplotlib.pylab as plt
from numpy.core.function_base import linspace
from scipy.interpolate import interp1d
import mpld3

filterr=46

racer=13
a=[]
for i in range (racer):
    a.append(np.load('carrera'+str(i+1)+'.npy',allow_pickle=True))
a=np.array(a)
p_lewis=[]
p_verstappen=[]

#pilots names
pilots_names=[]
amount_races=0
for carrera in a:
    amount_races+=1
    for piloto in carrera:
        if piloto[3]=='Robert  Kubica  KUB':
            piloto[3]='Kimi  Räikkönen  RAI'
        if piloto[3] != 'Driver' :
            if not piloto[3] in pilots_names:
                pilots_names.append(piloto[3])

#pilots points
pilots_points=np.empty(len(pilots_names), dtype=object)
for carrera in a:
    for piloto in carrera:
        if piloto[3] != 'Driver' :
            index= pilots_names.index(piloto[3])
            pilots_points[index]=np.append(pilots_points[index],[float(piloto[-2])])
            
x=np.arange(0,racer+1,1)+1

actual=[]

plt.figure(figsize=(7,10)) 
for i in range (len(pilots_names)):
    cum_sum=np.cumsum(pilots_points[i][1:])
    pilots_points[i]=cum_sum
    #pilots_names[i]=pilots_names[i]+' Points='+str(cum_sum[-1])
    actual.append(cum_sum[-1])
    #interpolation
    y_new= interp1d(x, cum_sum, kind='cubic')
    x_new=np.linspace(1,len(cum_sum),45)
    if cum_sum[-1]>=filterr:
        if i<10:
            plt.plot(x_new,y_new(x_new))
        if i>=10:
            plt.plot(x_new,y_new(x_new),'--')
        #cum_sum=np.cumsum(pilots_points[i][1:])
        plt.scatter(x,cum_sum)
labels = ['Bahrain', 'Italy', 'Portugal', 'Spain','Monaco','Azerbaijan','France','Austria','Austria 2','Great Britain Sprint','Great Britain','Hungary','Belgium','Netherlands','Italy Sprint','Italy']

res = dict(zip(pilots_names, actual))
res = sorted(res.items(), key=lambda x: x[1],reverse=True)


plt.xticks(np.arange(0,len(cum_sum)+2,1),labels=labels,rotation=75)
plt.yticks(np.arange(0,250,25))
#plt.legend(res,bbox_to_anchor=(1, 0.9))
plt.grid()
plt.title('2021 RACE RESULTS')
plt.xlabel('RACE')
plt.ylabel('POINTS')
for i in range (len(pilots_names)-10):
    if np.abs(res[i-1][1]-res[i][1])<10:
        plt.annotate(res[i], (x[-1],res[i][1]),xytext=[x[-1],res[i][1]-3])
    else:
        plt.annotate(res[i], (x[-1],res[i][1]))

plt.savefig('2021_race_result.jpg',dpi=700,bbox_inches='tight')
mpld3.show()