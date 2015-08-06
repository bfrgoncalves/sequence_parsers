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

	gbk_to_fna(args.gbk, args.o)


def gbk_to_fna(gbk_filename, fna_filename):
	

	input_handle  = open(gbk_filename, "r")
	output_handle = open(fna_filename, "w")

	for seq_record in SeqIO.parse(input_handle, "genbank") :
	    print "Dealing with GenBank record %s" % seq_record.id
	    output_handle.write(">%s %s\n%s\n" % (
	           seq_record.id,
	           seq_record.description,
	           seq_record.seq))

	output_handle.close()
	input_handle.close()
	print 'Done'

if __name__ == "__main__":
	main()