
from Bio import SeqIO

def gbk_to_fasta(gbk_filename, fasta_filename):

	SeqIO.convert(gbk_filename, "genbank", fasta_filename, "fasta")

	return True


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
	return True


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
	return True



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

	return True