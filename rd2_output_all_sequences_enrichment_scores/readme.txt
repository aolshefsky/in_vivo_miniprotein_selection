README

These csvs have the log10 enrichments of miniprotein sequences in mouse organs.

They are intended to be imported into a Jupyter notebook using pandas:
	df = pd.read_csv('path to file')

====Samples====
- Organs from mice
- 3 mouse groups:
	- hel stands for healthy mouse
	- tum stands for tumor-bearing mouse
	- hhr stands for mouse 10 (healthy mouse, 1hr circulation)

- Each organ is a 2-letter abbreviation
	- he - heart
	- ki - kidneys
	- li - liver
	- lu - lungs
	- sp - spleen
	- tu - tumor
	- TA - tibialis anterior
	- ga - gastrocnemius
	- so - soleus
	- di - diaphragm
	- bp - PBMCs from healthy mice
	- bh - blood from healthy-mice
	- bt - blood from tumor-bearing mice


- The order of the columns is: 
sequence,
hel_br,tum_br,hhr_br,
hel_he,tum_he,hhr_he,
hel_ki,tum_ki,hhr_ki,
hel_li,tum_li,hhr_li,
hel_lu,tum_lu,
hel_sp,tum_sp,hhr_sp,
tum_tu,
hel_ta,tum_ta,hhr_ta,
hel_ga,tum_ga,hhr_ga,
hel_so,tum_so,hhr_so,
hel_di,tum_di,hhr_di,
hel_bl, (blood from healthy mice)
tum_bl, (blood from tumor mice)
hel_pb (PBMCs from healthy mice)

====Files====
- log_enrich_all_seq_all_organs.csv has all the titles, self-explanatory. Probably the one to use.

- 20230118_log_enrich_all_seq_all_organs_from_dict.csv and 20230118_log_enrich_all_seq_all_organs_from_dict_2.csv similar data as log_enrich... without the headers. I was experimenting with formatting.
