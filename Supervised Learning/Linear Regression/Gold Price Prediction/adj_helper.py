import numpy as np
import pandas as pd

def adjR2 (xtest,ytest,r2):
	n = len(ytest)
	k = xtest.shape[-1]
	adj_r2 = 1 - ((1 - r2)*(n - 1)) / (n - k -1)
	print('The adjusted R2 is:', adj_r2)
	