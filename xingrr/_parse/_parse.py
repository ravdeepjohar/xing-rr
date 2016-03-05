from xingrr.types import Impression
import csv
import sys

csv.field_size_limit(sys.maxsize)

def parse_impressions(filepath):

	with open(filepath) as csv_file:
		csvreader = csv.DictReader(csv_file, delimiter="\t")
		impressions = []
		for line in csvreader:
			try:
				yield Impression(line['user_id'], line['year'], line['week'], line['items'].split(","))
			except:
				pass

		

