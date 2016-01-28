import Invoker as inv
import glob
import matplotlib.pyplot as plt
import numpy as np
import itertools
import pandas as pd
import seaborn as sns
''' This looks at time difference of time to start of successful combo and time to first key.  This then captures
any mistakes that are only motor mistakes '''

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

time_lost = []
rank = []
exp = []
for s in subjects:
    if not s.bio['rank'].isdigit():
        print s.bio['rank']
        continue
    else:
        rank.append(int(s.bio['rank']))
        lost = np.array([a - b for a, b in zip(itertools.chain(*s.section_time_to_correct), itertools.chain(*s.section_time_to_start))])
        # do we want to capture time lost due to screwing up repeatedly or screwing up once that is the choice between including zeros and nonzeros
        #time_lost.append(np.mean(lost[np.nonzero(lost)]))
        time_lost.append(np.mean(lost))
        exp.append(s.bio['exp'])

data = pd.DataFrame({'rank': rank, 'time_lost': time_lost, 'exp': exp})

for k, gp in data.groupby('exp'):
    sns.jointplot('rank', 'time_lost', gp, kind='reg')
    #sns.lmplot('rank', 'time_lost', gp)
    #sns.residplot('rank', 'time_lost', gp)
    sns.plt.savefig('time lost exp: ' + str(k) + '.pdf')
#sns.plt.show()
#sns.jointplot('rank', 'time_lost', data, kind='reg', color='seagreen')
#sns.plt.savefig('retrieval.pdf')
#sns.plt.show()
