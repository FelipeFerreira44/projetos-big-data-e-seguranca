from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class MediaFeridos2022Borough(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_filter, reducer=self.reducer_sum),
            MRStep(mapper=self.mapper_avg, reducer=self.reducer_final)
        ]

    def mapper_filter(self, _, line):
        try:
            fields = next(csv.reader([line]))
            if len(fields) < 11 or fields[0] == 'CRASH DATE': return
            date_str = fields[0].strip()
            parts = date_str.split('/')
            if len(parts) != 3 or parts[2] != '2022': return
            injured = int(fields[10].strip() or 0)
            if injured <= 0: return
            borough = fields[2].strip().upper() or 'UNKNOWN'
            yield borough, [injured, 1]
        except: pass

    def reducer_sum(self, key, values):
        s, c = 0, 0
        for v in values: s += v[0]; c += v[1]
        yield key, [s, c]

    def mapper_avg(self, key, value):
        yield 'GLOBAL', (key, value)

    def reducer_final(self, key, values):
        medias = {}
        for b, val in values:
            s, c = val
            medias[b] = round(s / c, 2) if c > 0 else 0



        for b in sorted(medias):
           yield (b, '%.2f' % medias[b])

        if medias:
            max_b = max(medias, key=medias.get)
            min_b = min(medias, key=medias.get)
            yield ('MAIOR_MEDIA', '%.2f (%s)' % (medias[max_b], max_b))
            yield ('MENOR_MEDIA', '%.2f (%s)' % (medias[min_b], min_b))


       

if __name__ == '__main__':
    MediaFeridos2022Borough.run()
