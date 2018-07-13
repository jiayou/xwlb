
HTML=$1
TEXT=${HTML/pages/text}

cat $HTML |  grep \<p\> | grep -v mrxwlb |  sed -e 's/<[^>]*>//g' > $TEXT 
