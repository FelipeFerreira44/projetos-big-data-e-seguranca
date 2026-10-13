import csv
from mrjob.job import MRJob


class MediaFeridosAno(MRJob):
    """Média de pessoas feridas por acidente, por ano."""

    def mapper(self, _, line):
        try:
            fields = next(csv.reader([line]))
            if len(fields) < 11 or fields[0] == "CRASH DATE":
                return
            parts = fields[0].strip().split("/")
            if len(parts) != 3:
                return
            yield parts[2], [int(fields[10].strip() or 0), 1]
        except (ValueError, StopIteration):
            pass

    def reducer(self, key, values):
        total, count = 0, 0
        for feridos, n in values:
            total += feridos
            count += n
        yield key, round(total / count, 2) if count else 0


if __name__ == "__main__":
    MediaFeridosAno.run()
