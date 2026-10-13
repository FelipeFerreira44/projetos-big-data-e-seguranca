from mrjob.job import MRJob

class AcidentesBoroughAno(MRJob):
    def mapper(self, _, value):
        fields = value.split(",")
        if len(fields) < 3 or fields[0] == 'CRASH DATE':
            return
        try:
            borough = fields[2].strip().upper()
            if not borough:
                borough = 'UNKNOWN'
            date_str = fields[0].strip()
            parts = date_str.split('/')
            if len(parts) != 3:
                return
            year = parts[2]
            yield [borough, year], 1
        except ValueError:
            pass

    def reducer(self, key, values):
        yield '%s\%s' % (key[0], key[1]), sum(values)

if __name__ == '__main__':
    AcidentesBoroughAno.run()
