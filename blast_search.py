#!/usr/local/bin/python3
'''
Author: Henoke Shiferaw

This script runs the blast tool that is part of the biopieces toolset. FASTA datasets sampled 
from 5 organisms were used in running the blast_seq tool. Results are then written to MySQL Database.
'''

import cgi, json
import os
import mysql.connector
def main():
    # connect to database and create cursor object
    conn = mysql.connector.connect(user='hshifer1', password=passwordWasHere, host='localhost', database='hshifer1')
    curs = conn.cursor()

    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')
    
    organism = ["Athaliana", "btaurus", "dmel", "ecoli", "human"]
    ids = [100005, 100084, 100412, 100473, 100772]
    idindex=0
    
    #Run blast_seq on all 5 fastafiles and store results in res.txt
    for org in organism:
        command = 'read_fasta -i {0}sec.txt | blast_seq -d ./files/dbs/{0}.fna -O res.txt'.format(org)
        os.system(command)
        
        # parse results file
        file = open("res.txt")
        
        
        results = {'orf_matches': list()}
        entries = 0
        while entries < 5:
            x = file.readline().strip()
            if x.startswith("STRAND"):
                temp=[]
                for num in range(0,14):
                    temp.append(x.strip())
                    #print(x.strip())
                    x=file.readline() 
                strand=temp[0][8:] # Full DNA Sequence
                q_ID=temp[1][6:] #Query ID
                s_ID=temp[3][6:] # Subject ID
                identity=temp[5][7:] # Identity percentage
                e_val=temp[6][7:] # E value
                s_beg=temp[7][7:] # Beginning location of Subject strand
                q_beg=temp[8][7:] #Beginning location of query strand
                q_end=temp[11][7:] #End location of query strand
                s_end=temp[13][7:] # End location of subject strand
                ##query
                qry = '''INSERT INTO BLAST_SEQS (entry_ID,strand, subject_ID, subject_beginning, subject_end, query_ID, query_Beginning, query_END, Identity, e_value) VALUES (%s,%s,%s,%s,%s,
                       %s,%s,%s,%s,%s);'''

                # execute search query
                curs.execute(qry, (ids[idindex], strand ,s_ID, s_beg,s_end,q_ID,q_beg,q_end,identity, e_val,))
                entries+=1
        idindex+=1
    curs.close()
    conn.close()
    print(json.dumps(results))
if __name__ == '__main__':
    main()
