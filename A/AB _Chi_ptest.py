import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#data
n_A ,con_A = 1000,52
n_B,conv_B  =1000,68
rate_A = con_A/n_A
rate_B = conv_B/n_B

print(f'version A conversion rate : {rate_A*100:.1f}%')
print(f'Version B conversion rate : {rate_B*100:.1f}%')
print(f'Improvement : {(rate_B-rate_A)/rate_A*100:.1f}%')

#chi value test for stasticl significance
table = [[con_A,n_A-con_A],[conv_B,n_B-conv_B]]
chi2,p_value,dof,expected = stats.chi2_contingency(table)

print(f'chi-square :{chi2:.4f}')
print(f'p-value : {p_value:.4f}')
print('Result:','significant - B is better !' if p_value<0.05 else 'Not significant-could be random')