"""  вантовый симул€тор"""
import math
import random
import numpy as np


class Qubit:
	def q(self,Pol1,Pol2,a,b):

		sost=np.array([0,1];
		a=np.random.random.choice(sost,1,relace=true,p=[0.5])
		b=np.random.random.choice(sost,1,relace=true,p=[0.5])
		f=np.array([90,135];
		g=np.array([0,45];

		if a==1:
			Pol1=np.random.random.choice(f,1,relace=true,p=[0.5])

		else:
		Pol1=np.random.random.choice(g,1,relace=true,p=[0.5])

		if b==1:
			Pol2=np.random.random.choice(f,1,relace=true,p=[0.5])

		else:
			Pol2=np.random.random.choice(g,1,relace=true,p=[0.5])

		self.q=Pol1*a+Pol2*b
		
		print(Pol1+"*|"+a+">"+Pol2+"*|"+b+">")
		return q
