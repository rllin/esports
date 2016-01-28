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
        avg_time.append(np.median(list(itertools.chain(*s.section_time_to_start))))
        exp.append(s.bio['exp'])

data = pd.DataFrame({'rank': rank, 'avg_times': avg_time, 'exp': exp})


for k, gp in data.groupby('exp'):
    sns.jointplot('rank', 'avg_times', gp, kind='reg')
    #sns.lmplot('rank', 'avg_times', gp)
    #sns.residplot('rank', 'avg_times', gp)
    sns.plt.savefig('retrieval exp: ' + str(k) + '.pdf')
#sns.plt.show()
#sns.jointplot('rank', 'avg_times', data, kind='reg', color='seagreen')
#sns.plt.savefig('retrieval.pdf')
#sns.plt.show()
