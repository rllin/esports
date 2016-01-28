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

avg_iki = []
rank = []
exp = []
name = []
for s in subjects:
    if not s.bio['rank'].isdigit():
        print s.bio['rank']
        continue
    else:
        rank.append(int(s.bio['rank']))
        avg_iki.append(np.mean(list(itertools.chain(*s.section_ikis))))
        print str(s.bio['email']) + ': ' + str(avg_iki[-1])
        exp.append(s.bio['exp'])
        name.append(s.bio['email'])

data = pd.DataFrame({'rank': rank, 'avg_ikis': avg_iki, 'exp': exp, 'name': name})

for k, gp in data.groupby('exp'):
    sns.jointplot('rank', 'avg_ikis', gp, kind='reg')
    #sns.lmplot('rank', 'avg_ikis', gp)
    #sns.residplot('rank', 'avg_ikis', gp)
    sns.plt.savefig('iki exp: ' + str(k) + '.pdf')
#sns.plt.show()

#sns.jointplot('rank', 'avg_ikis', data, kind='reg', color='seagreen')
#sns.plt.savefig('ikis.pdf')
#sns.plt.show()
