#!/bin/bash

# Website can be changed here
website='https://www.cigaraficionado.com/ratings/search?brand=&countries[0]=+Cuba&q=&taste_date=&page'

if [ ! -d reviews ]; then
	mkdir reviews
fi

# find the review URLs from the first 10 pages
for i in {1..20}
do
	if [ $i = 1 ]; then
		echo "Curling $website"
		curl -s $website >> output.txt
	else
		echo "Curling $website$i"
		curl -s "$website=$i" >> output.txt
	fi
	#cat output.txt | html2text >> output_cleaned.txt
	grep -oP '(?<=href="/ratings/).*?(?=">View Tasting Note)' output.txt >> cigars.txt
	rm output*.txt
	
	#cat cigars.txt
done

echo ""

# loop through the review URLs and put the curl contents in a file (after cleaning)
while read line;
do
	temp_website="https://www.cigaraficionado.com/ratings/$line"
	echo "Curling $temp_website"
	curl -s $temp_website >> tmp.txt
	fn_tmp1=$(grep "@id" tmp.txt | grep ratings)
	fn_tmp2=$(echo $fn_tmp1 | sed 's|.*\/\(.*\)|\1|')
	file_name=$(echo ${fn_tmp2:0:-2})
	echo "Creating $file_name in reviews dir."
	cat tmp.txt >> reviews/$file_name
	rm tmp.txt
	sed -n 's_/[^*]*__p' cigars.txt >> cigars.txt
done < cigars.txt

# remove all lines before this pattern
#sed -n '/[the pattern itself]/,$p'
# remove all lines after this pattern
#sed -n '/[the pattern itself]/q;p'

# Clean up
#rm cigars.txt
