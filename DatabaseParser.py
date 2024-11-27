import csv
import os

class DatabaseParser:

    def parseData(self, path):
        data = []
        labels = []
        try:
            with open(path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)

                fields = next(csvreader)

                for row in csvreader:
                    data.append(row[5])
                    labels.append(row[0])

            return data, labels

        except FileNotFoundError:
            print('Error: File not found')


if __name__ == '__main__':
    parser = DatabaseParser()
    data, label = parser.parseData(os.curdir+'/data/dataset.csv')
    print(data[:5])