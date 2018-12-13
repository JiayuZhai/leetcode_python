# Read from the file words.txt and output the word frequency list to stdout.
awk '{ i = 1; while ( i <= NF ) { name[$i]++;i++}} END {for(i in name){print i " " name[i]}}' words.txt | sort -r -n -t " " -k 2
