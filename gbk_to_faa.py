import subprocess
import argparse
import os
import shutil
from os import listdir
from os.path import isfile, join, isdir
import sys


from Bio import SeqIO



def main():

	parser = argparse.ArgumentParser(description="This program parses a .gbk file to a .faa file")
	parser.add_argument('-gbk', nargs='?', type=str, help=".gbk file", required=True)
	parser.add_argument('-o', nargs='?', type=str, help="results file name", required=True)


	args = parser.parse_args()

	gbk_to_faa(args.gbk, args.o)


def gbk_to_faa(gbk_filename, faa_filename):

	input_handle  = open(gbk_filename, "r")
	output_handle = open(faa_filename, "w")

	for seq_record in SeqIO.parse(input_handle, "genbank") :
	    print "Dealing with GenBank record %s" % seq_record.id
	    for seq_feature in seq_record.features :
	        if seq_feature.type=="CDS" :
	            assert len(seq_feature.qualifiers['translation'])==1
	            output_handle.write(">%s_from_%s\n%s\n" % (
	                   seq_feature.qualifiers['locus_tag'][0],
	                   seq_record.name,
	                   seq_feature.qualifiers['translation'][0]))

	output_handle.close()
	input_handle.close()
	print "Done"


if __name__ == "__main__":
	main()