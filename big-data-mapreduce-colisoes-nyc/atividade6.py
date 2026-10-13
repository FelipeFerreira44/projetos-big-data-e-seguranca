from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class AcidentesBoroughAnoMes(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_count, combiner=self.combiner_count, reducer=self.reducer_count),
            MRStep(mapper=self.mapper_max, reducer=self.reducer_max)
        ]

    def mapper_count(self, _, line):
        try:
            fields = next(csv.reader([line]))
            if len(fields) < 3 or fields[0] == 'CRASH DATE': return
            borough = fields[2].strip().upper() or 'UNKNOWN'
            date_str = fields[0].strip()
            parts = date_str.split('/')
            if len(parts) != 3: return
            yield [borough, parts[2], parts[0].zfill(2)], 1
        except: pass

    def combiner_count(self, key, values):
        yield key, sum(values)

    def reducer_count(self, key, values):
        yield key, sum(values)

    def mapper_max(self, key, value):
        yield key[0], (key[1], key[2], value)

    def reducer_max(self, key, values):
        max_y, max_m, max_c = max(values, key=lambda x: x[2])
        yield key, f"{key}\{max_y}\{max_m}\{max_c}"

if __name__ == '__main__':
    AcidentesBoroughAnoMes.run()
