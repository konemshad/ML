#TODO Not completed yet. 
import numpy as np
from math import log,e
from ml.activation.util import softmax,sigmoid
class LOSS:
	def __init__(self,feat=None,weights=None,hyp=None):
		self.feat=feat
		self.w=weights
		self.hyp=hyp

	@staticmethod
	def sigmoidal(self,X):
		return sigmoid(normal(self,X))

	@staticmethod
	def soft_max(self,X):
		return softmax(self.normal(self,X))

	@staticmethod
	def mean_squared_loss(self,features,targets,hyp="Regression"):
		self.f=features
		self.hyp=HYP[hyp]
		self.target=targets
		self.no_train=len(self.feat)
		su=0
		for i in range(self.no_train):
			res=(self.hyp(self.feat[i])-self.target[i])**2
			su+=res
		return np.mean(su)

	@staticmethod
	def cross_entropy(self,targets,features,hyp="binary_class"):
		self.feat=features
		self.target=targets
		self.hyp=HYP[hyp]
		self.no_train=len(self.feat)
		s=0
		for _ in range(self.no_train):
			s+=self.target[_]*log(self.hyp(self.feat[_]))+(1-self.target[_])*log(1-self.hypo(self.feat[_]))
		r=(1/self.no_train)*s
		return r

	@staticmethod
	def categorical_cross_entropy(self,feat,target,hyp="multiclass"):
		self.target=target
		self.k=self.target.shape[1]
		self.feat=feat
		self.no_train=len(self.feat)
		self.hyp=HYP[hyp]
		r = np.dot(self.target,np.log(self.hyp(self.feat)))
		return r

	@staticmethod
	def normal(self,obj,X):
		return np.matmul(obj.weights,X)

HYP={"Regression":LOSS.normal,"binary_class":LOSS.sigmoidal,"multiclass":LOSS.soft_max}
			
			
			
			
			
		
		
		
		
		
		
	
	
