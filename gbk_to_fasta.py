import subprocess
import argparse
import os
import shutil
from os import listdir
from os.path import isfile, join, isdir
import sys

from Bio import SeqIO


def main():

	parser = argparse.ArgumentParser(description="This program parses a .gbk file to a .fasta file")
	parser.add_argument('-gbk', nargs='?', type=str, help=".gbk file", required=True)
	parser.add_argument('-o', nargs='?', type=str, help="results file name", required=True)


	args = parser.parse_args()

	SeqIO.convert(args.gbk, "genbank", args.o, "fasta")


if __name__ == "__main__":
	main()