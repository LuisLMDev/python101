import csv

path_archivo = 'data/ejemplo.csv'
results = []

with open(path_archivo) as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print(results)

if __name__ == '__main__':
    print('Hola DictReader')
