# Add a SeqMatch Database

Click on this [link](https://onedrive.live.com/download?cid=CF4E6E0B1440602C&resid=CF4E6E0B1440602C%21114579&authkey=AN43HO59zBZP9mA) to download the archive file SeqMatch_DBs.zip. Place the file in the folder you mapped to the contianer (see creating-the-container) and decompress it. This generates the directory SeqMatch_DBs with the following files:  

```{text}
| SeqMatch_DBs  
├── release11_4_types.trainee  
├── release11_4_type_descriptions.txt  
├── release11_4_bac_islote_descriptions.txt  
├── isolate_trainee_files  
  ├──── release11_4_bac_isolates_1.trainee  
  ├──── release11_4_bac_isolates_2.trainee  
  ├──── release11_4_bac_isolates_3.trainee
  ├──── release11_4_bac_isolates_4.trainee  
  ├──── release11_4_bac_isolates_5.trainee  
  ├──── release11_4_bac_isolates_6.trainee  
  ├──── release11_4_bac_isolates_7.trainee  
  ├──── release11_4_bac_isolates_8.trainee  
        
```
As you can see, their are two databases; one for type strains and another for bacterial isolates.  

# Using SeqMatch

Entering the following command from within the container ...  

```{text}
java -jar /usr/local/RDPTools/SequenceMatch.jar seqmatch
```

Gives a help message for the seqmatch program:  

```{text}


usage: seqmatch <refseqs | trainee_file_or_dir> <query_file>
                trainee_file_or_dir is a single trainee file or a
                directory containing multiple trainee files
 -d,--desc <arg>      A tab-delimited description file containing seqID
                      and description
 -k,--knn <arg>       Find k nearest neighbors [default = 20]
 -o,--outFile <arg>   Write output to a file
 -s,--sab <arg>       Minimum sab score [default = .5]

```


To classify sequences in a fasta file with the type strains database, use a command of the form (edit paths as necessary):  

```{text}
java -jar /usr/local/RDPTools/SequenceMatch.jar seqmatch \
~/SeqMatch_DBs/release11_4_types.trainee \
query.fasta \
--desc ~/SeqMatch_DBs/release11_4_type_descriptions.txt \
--knn 20 \
--sab 0.5 \
--outFile query_classified.tsv
```

To classify sequences in a fasta file with the isolates database, use a command of the form (edit paths as necessary):  

```{text}
java -jar /usr/local/RDPTools/SequenceMatch.jar seqmatch \
~/SeqMatch_DBs/isolate_trainee_files \
query.fasta \
--desc ~/SeqMatch_DBs/release11_4_bac_isolate_descriptions.txt \
--knn 20 \
--sab 0.5 \
--outFile query_classified.tsv
```

