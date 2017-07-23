# Notes - file created by "CA5_process_changes_JFraser.py" was CA5_changes_JF.csv
# However, this had 3 records which went onto two lines and a few other inaccuracies
# This program worked well on that file without revision. However, I converted to excel,
# did some revising/cleaning etc. and re-converted back to .csv: CA5_changes_JF2.csv

output_file1 = 'CA5_changes_JF2.csv'
my_file1 = open(output_file1,'r')

# read first line separately, which is just headings:
s1 = my_file1.readline()
print s1

# want to count number of operations carried out on different days ("what days of the week are busiest")
# so need list of days and also a list containing "counts" for each day
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
days_count = [0,0,0,0,0]

# next, want to achieve something similar for authors (operators?)
# so, declare authors and count_authors - need to insert initial elements to enable "while" statement below to start....
authors = ["name1"]
count_authors = [0]

large_count = int(raw_input("Information on transactions larger than a certain figure will be calculated and analysed - enter number for this (1-500,say): "))
#cross_count will be used to count how many transactions >large_count (or whatever number) are attributed to each author
cross_count = [0]

j=0
k = 1
# I know there are 422 records in total from looking at file - could have calculated this by counting in CA5_process_changes_JFraser.py, but seemed unnecessary??
while k<423:
	s1 = my_file1.readline()
	details = s1.split(',')
	# the 5th element of each row/line, details[4], is the day:
	day = details[4]
	# next, details[5] will be the length of "lines", a measure related to the number of transactions i each operation
	lines = float(details[5])
	# next, search for day in list of days
	day_number = days.index(day)
	days_count[day_number] = days_count[day_number]+1
	#next function below is to record where lines (# of transactions) exceed a given number; will run the program with this set to different values
	counter = lambda x: 1 if (x>large_count) else 0
	j = j + counter(lines)
	k=k+1
	author_number = len(authors)
	# next comes the process of filling up the lists containing author and number of operations carried out by each author
	new = 0
	m = 0
	while m < author_number:
		if details[1] == authors[m]:
			count_authors[m] = count_authors[m]+1
			cross_count[m] = cross_count[m]+counter(lines)
			new = 1
			m = author_number
		else:
			m = m+1
	# if new remains 0, this means we have found a new author name which must be added to the list(s)
	if new == 0:
		authors.append(details[1])
		count_authors.append(1)
		cross_count.append(counter(lines))

# need to remove first elements of authors and count_authors, which were originally inserted as dummies to allow above while statements to begin
authors.remove("name1")
count_authors.remove(0)
#for cross_count, there may be more than one 0, but below will remove the first 0, which is what I want!
cross_count.remove(0)

#print len(s1)
print days, " - number of operations in each of these days: ", days_count
print "Number greater than ", large_count, " is: ", j
print "List of authors/operators: ", authors
print "Number of operations carried out by each author/operator", count_authors
print "Number greater than ", large_count, " split by author: ", cross_count

d1 = len(authors)
print "Number of authors: ", d1
check_count_authors = reduce(lambda x,y:x+y, count_authors)
print "Check total count of authors (this is actually a test that individual figures add to correct total): ", check_count_authors

my_file1.close()