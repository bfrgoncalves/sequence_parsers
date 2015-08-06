import subprocess
import argparse
import os
import shutil
from os import listdir
from os.path import isfile, join, isdir
import sys

from Bio import SeqIO

def main():

	parser = argparse.ArgumentParser(description="This program parses a .gbk file to a .fna file")
	parser.add_argument('-gbk', nargs='?', type=str, help=".gbk file", required=True)
	parser.add_argument('-o', nargs='?', type=str, help="results file name", required=True)


	args = parser.parse_args()

	gbk_to_gff(args.gbk, args.o)


def gbk_to_gff(gbk_filename, fna_filename):


	def checkStrand(strand_gbk):
		
		if strand_gbk == 1:
			return '+'
		elif strand_gbk == -1:
			return '-'
		else:
			return '.'
	

	input_handle  = open(gbk_filename, "r")
	output_handle = open(fna_filename, "w")

	for gb_record in SeqIO.parse(input_handle, "genbank") :
		print "Name %s, %i features" % (gb_record.name, len(gb_record.features))

		output_handle.write('##gff\n##dataFROM_gbk_to_gff.py_@bfrgoncalves\n')
		for features in gb_record.features:
			if features.type != 'misc_feature':
				output_handle.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (
						gb_record.name,
						'RefSeq',
						features.type,
						features.location.start,
						features.location.end,
						'.',
						checkStrand(features.location.strand),
						'.'))

				toWrite = ''

				for qualifiers in features.qualifiers:
					if qualifiers == 'translation':
						continue
					else:
						toWrite += qualifiers + '=' + features.qualifiers[qualifiers][0] + ';'

				output_handle.write(toWrite + '\n')

	print 'Done'



if __name__ == "__main__":
	main()