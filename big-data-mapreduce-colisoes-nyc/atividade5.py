import csv
from mrjob.job import MRJob


class MediaCiclistasBoroughAno(MRJob):
    """Média de ciclistas feridos por acidente, por bairro (borough) e ano."""

    def mapper(self, _, line):
        try:
            fields = next(csv.reader([line]))
            if len(fields) < 15 or fields[0] == "CRASH DATE":
                return
            borough = fields[2].strip().upper() or "UNKNOWN"
            parts = fields[0].strip().split("/")
            if len(parts) != 3:
                return
            yield [borough, parts[2]], [int(fields[14].strip() or 0), 1]
        except (ValueError, StopIteration):
            pass

    def reducer(self, key, values):
        total, count = 0, 0
        for feridos, n in values:
            total += feridos
            count += n
        yield "%s\\%s" % (key[0], key[1]), round(total / count, 2) if count else 0


if __name__ == "__main__":
    MediaCiclistasBoroughAno.run()
