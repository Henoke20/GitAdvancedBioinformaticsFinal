#!/usr/local/bin/python3

'''
Henoke Shiferaw

CGI file used to retrieve ORF and Blast_Seq info from the stored database

'''
import cgi, json
import os
import mysql.connector
def main():
    # connect to database and create cursor object
    conn = mysql.connector.connect(user='hshifer1', password='finley920m,.', host='localhost', database='hshifer1')
    curs = conn.cursor()
    
    print("Content-Type: application/json\n\n")
    # get data from form
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')
    
    results = {'orf_matches': list(), 'blast_seqs': list()}
            ##query
    qry = '''Select * FROM ORFS WHERE Sequence_name LIKE %s'''
    #for (Sequence_name,sequence,sequence_length,beg_coord,end_coord) in curs.fetchall():
            # execute search query
    curs.execute(qry,('%' + str(term)+'%',) )

    for (entry_ID, Sequence_name,sequence,sequence_length,beg_coord,end_coord) in curs.fetchall():
        results['orf_matches'].append({'sequence_name': Sequence_name,
                                           'sequence': sequence,
                                           'sequence_length': sequence_length,
                                           'beg_coord': beg_coord,
                                           'end_coord': end_coord,
                                           'entry_ID': entry_ID})

    # execute search query on blast sequence
    qry = '''Select * FROM BLAST_SEQS WHERE query_ID LIKE %s'''
    
    curs.execute(qry,('%' + str(term)+ '%',))
    
    for(entry_ID, strand, subject_ID, subject_beginning, subject_end, query_ID, query_Beginning, query_END, Identity, e_value) in curs.fetchall(): 
        results['blast_seqs'].append({
                'strand': strand,
                'subject_ID': subject_ID,
                'subject_beginning': subject_beginning,
                'subject_end': subject_end,
                'query_ID': query_ID,
                'query_Beginning':query_Beginning,
                'query_END': query_END,
                'Identity': str(Identity),
                'e_value': str(e_value),
                'entry_ID': entry_ID})
       
    curs.close()
    conn.close()
    print(json.dumps(results))
if __name__ == '__main__':
    main()
