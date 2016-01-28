import json
import collections
import numpy
import matplotlib.pyplot as plt
from itertools import islice

class Event:
    def __init__(self, data, timestamp):
        self.timestamp = int(timestamp)
        self.event_type = data['state']
        if self.event_type == 'key down':
            self.target = data['data']['target queue']
            #self.current = data['data']['current queue']
            self.success = data['data']['success state']
            self.key = data['data']['key event']


class Invoker:
    def __init__(self, filename):
        self.od = collections.OrderedDict(sorted(json.load(open(filename)).items()))
        self.bio = self.od.items()[0][1]['data']
        self.sections = [e['data']['task mode'] for e in [v for k, v in self.od.iteritems() if v['state'] == 'initialize']]
        self.section_start_times = [int([k for k, v in self.od.iteritems() if v['state'] == 'initialize' and v['data']['task mode'] == section][0]) for section in self.sections]
        self.section_start_times.append(int(max(self.od.keys())))
        self.section_start_end_times = zip(self.section_start_times[:-1], self.section_start_times[1:])
        self.section_times = dict(zip(self.sections, [collections.OrderedDict(sorted({str(e): self.od[str(e)] for e in range(*pair) if str(e) in self.od}.items())) for pair in self.section_start_end_times]))

        self.section_data = dict(zip(self.sections, [[Event(self.od[d], d) for d in self.section_times[s]] for s in self.sections]))

        self.section_times_to_combo = [self.time_to_combo(section) for section in self.sections]
        self.section_time_to_start = [self.time_to_start_press(section) for section in self.sections]
        _, self.section_ikis, self.section_time_to_correct = zip(*[self.IKI(section) for section in self.sections])
        self.error_time = []
         
    def time_to_combo(self, section):
        ''' Time in milliseconds to successful combo '''
        times = []
        for event in self.section_data[section]:
            if event.event_type == 'initialize':
                last_time = event.timestamp
            if (event.event_type == 'key down' and event.success == 'matched'):
                times.append(event.timestamp - last_time)
                last_time = event.timestamp
        return times


    def time_to_start_press(self, section):
        ''' Time in milliseconds to first key press '''
        times = []
        flag = 'found'
        for event in self.section_data[section]:
            if flag == 'found' and (event.event_type == 'initialize' or (event.event_type == 'key down' and event.success == 'matched')):
                last_time = event.timestamp
                flag = 'unfound'
                continue
            if (event.event_type == 'key down' and flag == 'unfound'):
                times.append(event.timestamp - last_time)
                flag = 'found'
        return times 


    def IKI(self, section):
        ''' IKIs and time to correct combo start '''
        times = []
        ikis = []
        times_since = []
        current = [0,] * 6
        iki = [0,] * 6
        time_since = [0,] * 6
        last = self.section_data[section][0].timestamp
        combo_start = last
        for ind, event in enumerate(self.section_data[section][1:]):
            if event.event_type == 'key down':
                if event.key in [49, 81, 87, 69, 82, 68]:
                    current.pop(0)
                    current.append(event.key)
                    iki.pop(0)
                    iki.append(event.timestamp - last)
                    time_since.pop(0)
                    time_since.append(event.timestamp - combo_start)
                    #print 'iki(' + str(ind) + '): ' + str(iki) + ', ' + str(last)
                    last = event.timestamp
                    if event.target.upper() == ''.join([chr(e) for e in current]):
                        ikis.append(iki[1:])
                        times.append(iki[0])
                        times_since.append(time_since[0])
                        combo_start = last
                        time_since = [0,] * 6
                        current = [0,] * 6
                        iki = [0,] * 6
                        #print 'ikis: '
                        #print ikis
        return times, ikis, times_since
