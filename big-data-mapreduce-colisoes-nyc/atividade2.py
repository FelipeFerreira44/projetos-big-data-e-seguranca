import csv
from mrjob.job import MRJob


class CiclistasFeridosBronx(MRJob):
    """Ciclistas feridos no Bronx, por ano."""

    def mapper(self, _, line):
        try:
            # csv.reader respeita as aspas: o campo LOCATION contém vírgula
            fields = next(csv.reader([line]))
            if len(fields) < 15 or fields[0] == "CRASH DATE":
                return
            if fields[2].strip().upper() != "BRONX":
                return
            parts = fields[0].strip().split("/")
            if len(parts) != 3:
                return
            yield parts[2], int(fields[14].strip() or 0)
        except (ValueError, StopIteration):
            pass

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    CiclistasFeridosBronx.run()
