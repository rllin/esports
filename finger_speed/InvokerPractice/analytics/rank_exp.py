import Invoker as inv
import glob
import matplotlib.pyplot as plt
import numpy as np
import itertools
import pandas as pd
import seaborn as sns

path = '../data/pilot/'

subjects = []
for fname in glob.glob(path + '*.json'):
    try:
        subjects.append(inv.Invoker(fname))
        print 'read' + fname
    except Exception as e:
        print 'skipping' + fname
        print e
        continue

avg_time = []
rank = []
exp = []
for s in subjects:
    if not s.bio['rank'].isdigit():
        print s.bio['rank']
        continue
    else:
        rank.append(int(s.bio['rank']))
        exp.append(s.bio['exp'])

data = pd.DataFrame({'rank': rank, 'exp': exp})

    #sns.plt.savefig('retrieval exp: ' + str(k) + '.pdf')
#sns.plt.show()
#sns.jointplot('rank', 'avg_times', data, kind='reg', color='seagreen')
#sns.plt.savefig('retrieval.pdf')
#sns.plt.show()
