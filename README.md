# HTMLTableExtractor

This is a very simple script that relies on pandas, requests, and beautifulsoup (plus openpxyl for pandas to write Excel files) to extract tables of data from websites
and store them as Excel files. Very useful for larger data tables you would like to work with but do not want to take the time to copy over by hand or if copy/paste
is not an option for whatever reason. 

# Instructions:
1) Download requirements.txt to your Python environment (I used 3.10, an earlier version is probably fine).
2) Add requirements with pip install -r requirements.txt
3) Add url of the site with the table you would like to extract into the url variable at the top
4) Add desired Excel file name in the fname variable at the top
5) Run code and get your table!

# Considerations:
- You may have to change some of the keyword strings the function is searching for when grabbing row headers and the rows themselves, depending on the site setup
- I will consider generalizing this in the future!
