
import argparse
import csv
from logging import FileHandler
import pathlib
from contact_book import *
"""
Write a CLI that interacts with a csv file, that allows you to save contact information in the CSV file. 

-Allow user to look up a contact by email, first/last name or phone number.
-Allow user to update an entry in the file
-Allow user to display all email addresses, first names, last names etc.

examples: 

Show al the emails in the csv file:

IN: python3 contact-book.py --infile contacts.csv --all-emails 
OUT:

user1@gmail.com
user2@yahoo.com
...

IN: python3 contact-book.py --infile contacts.csv --user user1@gmail.com --first-name Dom  --update NAME


NOTE: separate the CLI from the logic 


"""

def contact_book_cli():

	parser = argparse.ArgumentParser(description="Tool for managing CSV file of Contact Data")
	# parser.add_argument('-in','--infile', action='store', type=argparse.FileType('r'))
	parser.add_argument('infile', type=pathlib.Path, help="Input file name/path is required")
	parser.add_argument('--search', action='store', nargs='+', help="When an ID number is given, will ignore the rest of the arguments")
	parser.add_argument('--update', action='store', nargs='+', help='Requires ID number and will not run without one')
	parser.add_argument('--browse', action='store', type=int, nargs='+', help="Single number returns df.head(num), two digits returns df.loc[num_1:num_2, :]")
	args = parser.parse_args()

	if args.infile:
		data_file = FileHandler(args.infile)
		if args.search:
			if len(args.search) > 1:
				'''Check to see args.search has, at least, one Column - Key Word pair'''
				data_file.user_search(args.search)
			else:
				raise Exception("Need Column - Key Word Pair to Seach. No Column - Key Word Pair Found")
		elif args.update:
			if len(args.update) > 1:
				data_file.update(args.update)
			else:
				raise Exception("Need Column - New Information Pair to Update, No Column - New Information Pair Found")
		elif args.browse:
			if len(args.browse) < 2:
				'''When one number digit is passed'''
				print(data_file.csv_to_df().head(args.browse[0]))
			else:
				'''When two numbers are pasased'''
				print(data_file.csv_to_df().loc[args.browse[0]:args.browse[1], :])

if __name__ == "__main__":
	contact_book_cli()
