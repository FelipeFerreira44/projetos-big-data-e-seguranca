from mrjob.job import MRJob

class AcidentesPorAno(MRJob):
    def mapper(self, _, value):
        fields = value.split(",")
        if len(fields) < 1 or fields[0] == 'CRASH DATE':
            return
        try:
            date_str = fields[0].strip()
            if date_str:
                parts = date_str.split('/')
                if len(parts) == 3:
                    year = parts[2]
                    yield year, 1
        except ValueError:
            pass

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    AcidentesPorAno.run()
