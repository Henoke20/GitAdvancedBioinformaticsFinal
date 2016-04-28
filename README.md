# GitAdvancedBioinformaticsFinal
********The following is documentation Final Project done in my Advanced Practical Computer Concepts in Bioinformatics course.
The project reinforces what we learned in the course including more intermediate Python scripting, Unix commandline, HTML, CSS,
JavaScript and Jquery. I have posted the python scripts on this github and will add the HTML, CSS, and JavaScript files later on.***

Henoke Shiferaw

Open Reading Frame finder and Blast_seq analysis tool

———————————
DIRECTORIES
———————————

Source code for along with files located in:
/var/www/html/hshifer1/final/

Tarbell located at:
/var/www/html/hshifer1/biopiece_verification_tool_final.tar.gz
(also sent)

The various programs used in the implementation of the tools depends heavily on file placement therefore it is recommended to download the demo as a whole.


Database files stored in:
/var/www/html/hshifer1/final/files/dbs
Can be downloaded at:
/var/www/html/hshifer1/final/files/blast_db_storage.tar.gz

———————
TOOLS
——————-
The tools used can be accessed at:
https://code.google.com/p/biopieces/

—————————————————
IMPLEMENTATION
—————————————————
Tools were ran on the unix server through python scripts: ORF_Finder.py, blast_search.py. Which ran the biopieces tools and stored them in tables on a MySQL Server. The site thus accesses prerun data from the MYSQL Server and displays it.

————————————————————-
HARDWARE REQUIREMENTS
—————————————————————
Recommended you have 1gb of hard drive space to download folder


——————————————————
USAGE INSTRUCTIONS
—————————————————-

1. Site is accessed at http://bfx.eng.jhu.edu/hshifer1/final/biopiecever.html

2. Choose from 1 of 5 Species to view pre_run datasets from.
Arabidopsis thaliana  
Bos taurus (Cattle)
Drosophila Melanogaster (Fruit Fly)
Escherichia coli 
Homo Sapiens (Human)

3. Choose between View ORFS or VIEW Sample Blast_Seqs.
* View ORFs will display all the open reading frames found from the sample genome data. On the right side you are also given the options to view the sequence of the found open reading frame.


* Clicking View Sample Blast_Seqs will display the top 5 hits for a selected open reading frame. The open reading frame chosen for blast seq can be seen by viewing the Entry_ID and looking for it in in the View ORFs data.


———————————
SAMPLE DATA
——————————-

Sequence data used to generate prerun ORF data found from:

Arabidopsis thaliana Sequence Chromosome 1 sequence
http://www.ncbi.nlm.nih.gov/nuccore/332189094


Drosophila melanogaster chromosome 3L 
http://www.ncbi.nlm.nih.gov/nuccore/AE014296.5?report=fasta&log$=seqview


Btaurus ref_Seq
ftp://ftp.ncbi.nih.gov/refseq/B_taurus/mRNA_Prot/cow.1.rna.fna.gz


Escherichia coli Complete Genome
http://www.ncbi.nlm.nih.gov/nuccore/NC_000913

Human DNA sequence from clone RP11-34P13 on chromosome 1, complete sequence
http://www.ncbi.nlm.nih.gov/nucleotide/24210292?report=genbank&log$=nuclalign&blast_rank=1&RID=XHEYX46V01R

Databases used in blast_seq were downloaded from::
ftp://ftp.ncbi.nih.gov/refseq/
