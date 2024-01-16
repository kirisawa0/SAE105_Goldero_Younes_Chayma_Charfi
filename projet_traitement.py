from collections import defaultdict
from math import*
from numpy import *
import datetime
import csv
t=array([int()]*1233)
j=list()


table=[]
with open('ADECal.csv',newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		table.append(row)
#suupprimer les colonnes 1 et 4
for i in range (len(table)):
	del table[i][0]
	del table[i][2]
n=len(table)

#mettre une seule salle pour chaque heur
test=False
salle=list()
while test ==False :
	for i in range(len(table)):
		x=0
		salle1=str(table[i][2])
		if "," in salle1 :
			while  salle1[x]!="," :
				x+=1
			salle.append(salle1[0:x])
		else :
			salle.append(table[i][2])
	test=True


#remplir un tableau t avec les horraires  dans le but de trier j
debut=""
fin=""
for i in range (0,n):
	t[i]=int(str(table[i][0][0:4])+str(table[i][0][5:7])+str(table[i][0][8:10])+str(table[i][0][11:13])+str(table[i][0][14:16]))
	debut=table[i][0]
	fin=table[i][1]
	j.append([debut[0:16],fin[0:16],salle[i]])
#trier le tableau
aux=0
ch=""
permut= True
while not (permut==False):
	permut=False
	for i in range(n-1):
		if t[i]>t[i+1]:
			aux=t[i]
			t[i]=t[i+1]
			t[i+1]=aux
			ch=j[i]
			j[i]=j[i+1]
			j[i+1]=ch
			permut=True
#supprimer les lignes qui n'ont pas des des salles
salles2=list()
for i in range(len(salle)):
	if salle[i] in salles2 :
		a=1
	else :
		salles2.append(salle[i])

for i in range(6):
	del(salles2[-1])
del(salles2[-3])
del(salles2[-3])


#effacer les salles qui ne sont pas dans la batiment r&t
liste_f=[]
for i in range(n):
	if j[i][2] in salles2 :
		liste_f.append(j[i])



#mettre les heurs ocupée par une salle
w=[]
deb=""
sec=""
for i in range (len(liste_f)):
	liste_f[i][0]=liste_f[i][0][ :14]+"00"
	fin=int(liste_f[i][1][14: ])
	heur_s=int(liste_f[i][1][11:13])
#	print(heur_s)
	if (heur_s+1 < 10) and (fin !=0) :
		liste_f[i][1]=liste_f[i][1][ :11]+"0"+str(heur_s +1)+":"+"00"
	elif fin != 00 :
		liste_f[i][1]=liste_f[i][1][ :11]+str(heur_s +1)+":"+"00"
	w.append(liste_f[i][2]+" le "+liste_f[i][0][ :11])
	deb=liste_f[i][0][11:16]
	sec=liste_f[i][1][11:16]
	w.append(deb+sec)

	
y=[]
for i in range (0,len(w),2):
	y.append([w[i], w[i+1]])
liste_f=y	

#print(liste_f)
#dict:cle:nom , valeur:date
d=defaultdict(list)
for k , v in liste_f :
	d[k].append(v)
sorted(d.items())
#print(d)
#liste avec tous les heur occupées par une salle
liste0fValues = d.values()
liste0fValues =list(liste0fValues)
#print(len(liste0fValues))
n=[]
h=[]
for i in range(len(liste0fValues)):
	h=liste0fValues[i]
	if len(h)>1:
		
		for j in range(len(h)):
			ch=""
			ch1=""
			ch += h[j][0:2]
			ch1 +=h[j][5:7]
		n.append([8,int(ch), int(ch1)])
	else:
		n.append([8,int(str(h[0][0:2])),int(str(h[0][5:7]))])
print(len(n))	
for i in range (len(n)):
	n[i].append(18)

#calculer les heurs libres par salle
m=[]
for i in range (len(n)):
	m=n[i]
	ch1=""
	for j in range(0,len(m),2):
		x=m[j+1]-m[j]
		if (x>0):
			ch1=ch1+"libre de " +str(m[j])+" jusqu'à "+str(m[j+1])+" "
	n[i]=ch1	
#print(n)	
#mettre les salles du dico dans une liste
keys = [key for key in d]
print(len(keys))
print(len(n))
#obtenir une liste final avec le nom de la salle et la date suivi de ses heures libres
finale=[]
for i in range(len(n)):
	finale.append([keys[i] , n[i]])
print(finale)



#ouvrir un fichier csv   
f=open('projet.csv', 'w')
writer=csv.writer(f)
for i in range (len(finale)):
	writer.writerow(finale[i])
f.close 