Sequence Analysis Pipeline (Miniprotein Display Library) 


Note: Even if it isn’t indicated, some of these steps might require using the ‘sed’ command to remove unwanted characters. Check output files in terminal with the ‘head’ command.

    1. Use PEAR application to get .fastq files from MiSeq data
    2. i_trim_translate_mp.py
        a. input: .fastq files
        b. removes adapters and translates DNA to protein, writing it to .csv files
        c. write the name of the file in the “readfile” line, will append “_tt_.csv” to the file
        d.  The script needs to be changed if the length of the adapter sequences are different. Translated sequences are written to the output file.
    3. ii_sort_translations_MDL.py
        a. input: “_tt_.csv” files
        b. Write name of file in “filename” line, outputs csv files
        c. Isolates protein sequences based on N- and C- termini
        d. Currently the script is set to print a .csv file of just sequences with N and C termini. You can uncomment the bottom section to print proteins with and without N and C sequences.
    4. Trim sorts
        a. Used sed in bash/command line
        
for F in *.csv; do
    sed 's/","GGGSASH//' $F > $F.out;
done
for F in *.out; do
    sed 's/LEGGGSEQK"//' $F > $F.done;
done
for F in *.done; do
    sed 's/"//' $F > $F.fine;
done

gets rid of adapters and preps protein for analysis


	5. Then you are ready for enrichment calculation and analysis in .ipynb. 
	   (In the manuscript, the files from "rd2_seqfiles_NC_trimmed_output" were used at this step)
