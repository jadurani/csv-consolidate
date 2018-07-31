#!/usr/bin/env python2

import csv
import os
import re
import sys

WORK_DIR = sys.argv[1] if len(sys.argv) > 1 else '.'
OUT_DIR = sys.argv[2] if len(sys.argv) > 1 else 'output/output.csv'

if os.path.dirname == '':
  OUTDIR = 'output/' + OUT_DIR
  print "Placing output in", OUT_DIR

if not os.path.exists(os.path.dirname(OUT_DIR)):
  os.makedirs(os.path.dirname(OUT_DIR))


""" Get all filenames recursively """
all_csv_files = []
for (dirpath, dirnames, filenames) in os.walk(WORK_DIR):
  for filename in filenames:
    if (
      filename.endswith('.csv') and
      os.path.join(dirpath, filename) != OUT_DIR
    ):
      all_csv_files.append(os.path.join(dirpath, filename))


""" Reprint all rows of all files into a single csv file--reformatted"""
count = 0
outputfilename = OUT_DIR
with open(outputfilename, 'w') as outputfile:
  fieldnames = [
    'full_name',
    'address',
    'zip',
    'country',
    'contact_number',
    'email'
  ]
  writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
  writer.writeheader()

  for filename in all_csv_files:
    with open(filename, 'rb') as csvfile:
      reader = csv.DictReader(csvfile)
      names = reader.fieldnames

      for row in reader:
        if row['Buyer Fullname'] == '':
          continue

        joined_address_strings = ' '.join([
          row['Buyer Address 1'],
          row['Buyer Address 2'],
          row['Buyer City'],
          row['Buyer State'],
        ])


        writer.writerow({
          'full_name': row['Buyer Fullname'],
          'address': re.sub(' +', ' ', joined_address_strings),
          'zip': row['Buyer Zip'],
          'country': row['Buyer Country'],
          'contact_number': row['Buyer Phone Number'],
          'email': row['Buyer Email'],
        })
        count += 1

print count, 'rows printed into', outputfilename
