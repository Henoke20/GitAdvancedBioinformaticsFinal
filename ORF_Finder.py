#!/usr/local/bin/python3
import cgi, json
import os
import mysql.connector
def main():
    # connect to database and create cursor object
    conn = mysql.connector.connect(user='hshifer1', password=PASSWORDHERE, host='localhost', database='hshifer1')
    curs = conn.cursor()

    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')
    
    organism = ["Athaliana", "btaurus", "dmel", "ecoli", "human"]
    IDs = 100000
    for org in organism:
        command = 'read_fasta -i ./files/sequences/{0}.txt | find_orfs -O results.txt'.format(org)
        os.system(command)
        # parse results file
        file = open("results.txt")

        #os.system("python3 dog.py")

        #file = open("./files/results.txt")
        results = {'orf_matches': list()}
        for x in file:
            if x.startswith("REC_TYPE"):
                temp=[]
                for num in range(0,6):
                    temp.append(x.strip())
                    x = next(file)
                results['orf_matches'].append({'sequence_name': temp[1][13:],
                                           'sequence': temp[2][5:],
                                           'sequence_length': temp[3][9:],
                                           'beg_coord': temp[4][7:],
                                           'end_coord': temp[5][7:]})
            ##query
                qry = '''INSERT INTO ORFS (entry_ID, Sequence_name, sequence, sequence_length, beg_coord, end_coord)
            VALUES (%s,%s,%s,%s,%s,%s);'''

            # execute search query
                curs.execute(qry, (IDs, temp[1][13:] ,temp[2][5:], temp[3][9:],
                                + int(temp[4][7:]), int(temp[5][7:]),))
                IDs+=1
    curs.close()
    conn.close()
    print(json.dumps(results))
if __name__ == '__main__':
    main()
