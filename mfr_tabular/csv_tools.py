from utilities import column_population, row_population
import csv


def data_from_csv(fp):
    """Read and convert a csv file to JSON format using the csv library
    :param fp: File pointer object
    :return: tuple of columns and rows
    """

    dialect = csv.Sniffer().sniff((fp).read(1024))
    fp.seek(0)
    # TODO(asmacdo) Nice way of displaying if there is no header
    # has_header = csv.Sniffer().has_header(infile.read())
    # infile.seek(0)
    reader = csv.reader(fp, dialect)
    data = [row for row in reader]

    columns = column_population(data[0])
    rows = row_population(data[1:], data[0])

    return columns, rows