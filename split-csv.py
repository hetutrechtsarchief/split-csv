#!/usr/bin/env python3

# this script splits a CSV file in multiple CSV files based on the value of a single field

import csv,sys,os
from sys import argv

delimiter=";"
encoding="utf-8"

if len(argv)!=4:
  sys.exit("Usage: "+os.path.basename(argv[0])+" {SPLIT_FIELD} {INPUT_CSV} {OUTPUT_FOLDER}")

split_field_name = argv[1]
input_filename = argv[2]
output_folder = argv[3] 
output_writers = {}

with open(input_filename, 'rt', encoding=encoding) as input_file:
  reader = csv.reader(input_file, delimiter=delimiter)
  header = next(reader)

  for r in csv.DictReader(input_file, fieldnames=header, delimiter=delimiter):

    split_field_value = dict(r)[split_field_name]

    if split_field_value not in output_writers:
      output_filepath = output_folder + "/" + os.path.basename(input_filename).replace(".csv",f"-{split_field_value}.csv")
      output_writers[split_field_value] = csv.DictWriter(open(output_filepath,"w"), fieldnames=header, delimiter=delimiter)
      output_writers[split_field_value].writeheader()

    output_writers[split_field_value].writerow(r)
