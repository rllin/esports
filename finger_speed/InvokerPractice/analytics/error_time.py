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

error_time = []
rank = []
exp = []
for s in subjects:
    if not s.bio['rank'].isdigit():
        print s.bio['rank']
        continue
    else:
        rank.append(int(s.bio['rank']))
        error_time.append(np.mean([i - j for i, j in zip(itertools.chain(*s.section_time_to_correct), itertools.chain(*s.section_time_to_start))]))
        exp.append(s.bio['exp'])

data = pd.DataFrame({'rank': rank, 'error_times': error_time, 'exp': exp})


for k, gp in data.groupby('exp'):
    sns.jointplot('rank', 'error_times', gp, kind='reg')
    #sns.lmplot('rank', 'error_times', gp)
    #sns.residplot('rank', 'error_times', gp)
    sns.plt.savefig('error exp: ' + str(k) + '.pdf')
#sns.plt.show()
#sns.jointplot('rank', 'error_times', data, kind='reg', color='seagreen')
#sns.plt.savefig('retrieval.pdf')
#sns.plt.show()
