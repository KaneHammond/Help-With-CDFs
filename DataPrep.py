import Modules
from Modules import *

#####################################################
# This will open our cdf file for data manipulation #
# and observation. We can access all segments of    #
# data and play with it.                            #
#####################################################


# Lets open our CDF file
cdf = pycdf.CDF('isccp_c2.cdf')

# Printing this will return: 
# CLD_AMT: CDF_REAL4 [90, 144, 72]
# CLD_PATH: CDF_REAL4 [90, 144, 72]
# EPOCH: CDF_EPOCH [90]
# FQ_HCLD: CDF_REAL4 [90, 144, 72]
# FQ_LCLD: CDF_REAL4 [90, 144, 72]
# FQ_MCLD: CDF_REAL4 [90, 144, 72]
# LATITUDE: CDF_REAL4 [72] NRV
# LONGITUD: CDF_REAL4 [144] NRV
# OPT_DPTH: CDF_REAL4 [90, 144, 72]
# PRS_CLDT: CDF_REAL4 [90, 144, 72]
# RFL_SFC: CDF_REAL4 [90, 144, 72]
# SFC_CODE: CDF_REAL4 [90, 144, 72]
# SNOW_ICE: CDF_REAL4 [90, 144, 72]
# TMP_CLDT: CDF_REAL4 [90, 144, 72]
# TMP_SSFC: CDF_REAL4 [90, 144, 72]

# Calling these items individually we see that they are in fact
# of datatype <type 'str'>. Our file size for this example is 
# greater than 43mb. So this clearly is not all our data! We can 
# use these strings to call the data within the .cdf file. 
# Below we do this to obtain our array data.

# Lets define these arrays for reference!

CLD_AMT = cdf['CLD_AMT'][::]
CLD_PATH = cdf['CLD_PATH'][::]
EPOCH = cdf['EPOCH'][::]
FQ_HCLD = cdf['FQ_HCLD'][::]
FQ_LCLD = cdf['FQ_LCLD'][::]
FQ_MCLD = cdf['FQ_MCLD'][::]
LATITUDE =cdf['LATITUDE'][::]
# Spelling error in file so we use it 
LONGITUD = cdf['LONGITUD'][::]
OPT_DPTH = cdf['OPT_DPTH'][::]
PRS_CLDT = cdf['PRS_CLDT'][::]
RFL_SFC = cdf['RFL_SFC'][::]
SFC_CODE = cdf['SFC_CODE'][::]
SNOW_ICE = cdf['SNOW_ICE'][::]
TMP_CLDT = cdf['TMP_CLDT'][::]
TMP_SSFC = cdf['TMP_SSFC'][::]

# What we did here was take an element within the file, such as TMP_SSFC, and
# called it from the file. The [::] indicator means the entire dataset. This
# can be modified to show segments of the data, such as [0:155]. This will show 
# the first 156 records, as 0 is an index value in the set. [5::] Would return 
# all the data excluding the first 5 records. Now that we have these in arrays,
# we can modify some data.

####################################################################################
# Lets see what we have...

# CHECK EPOCH * CHECK EPOCH * CHECK EPOCH * CHECK EPOCH

# print EPOCH
# print len(EPOCH)
# print type(EPOCH)
# sys.exit()
# Returns: <type 'numpy.ndarray'>

# The EPOCH sataset is a range of dates, checking the lenght of the item,
# we find 90 records exist. With datatype <type 'numpy.ndarray'>

# CHECK CLD_AMT * CHECK CLD_AMT * CHECK CLD_AMT * CHECK CLD_AMT

# print CLD_AMT
# print len(CLD_AMT)

# Here we find we have a collection of data for cloud records, the records
# seem to be lists of numbers. Checking the lenght of the data we find we
# also have 90 records. So one for each date element.

# I will now assume all other datasets are the same lenght
####################################################################################

# Filter through our date data! Since we have matching records for the datasets,
# they will share the same index. We can filter the dates by index placement and
# pull the other data sets accordingly for analysis.

# Identifying the dates!
# I will be pulling this data into a list, from which we can identify the placement 
# of each data with it's index. The associated index for a particular date,
# will be directly related to another item in a separate array by index. Meaning,
# Data xxx index value is 2, if we pull the second record from CLD_AMT, it will be
# the data for that associated date.

Dates = []
# For simplicity, I will add an index variable directly in the list for you to see.
i = 0
for aDate in EPOCH:
	# Make an insertable item. Don't have to do it this way, but I think it will be
	# easier for you understand.

	# Here we define the item. Where I is it's index, and aDate is the associated date!
	InsertableItem = [i, aDate]

	# Lets append this to our Dates list item.
	Dates.append(InsertableItem)

	# Count our iteration for i, we want it to increase by 1 each time.
	i=i+1

# Looking at the firs 2 records we see our data is in the form of sublists.
# Each element in Dates is a separate list item. Printing 0:2 will print records
# 0 and 1, it will stop at 2 and you will not see it.

# print Dates[0:2]

# If we print Dates[0] we notice it pulls the first record. The 0 in the brackets
# is its index value within the list, as you can see the i item we inserted earlier
# is equal to this. Like I said earlier, its added in so you can see the index next to 
# your data, if handling large amounts of data, you may want to avoid this to save
# memory.

# print Dates[0]


# Here we will bring in some complication. We need to filter through our 
# date items now.

# Define our dates!
# Here for a single date
Year = '1985'
Month = '1'

# Here for a date range
# Start
YearS = '1985'
MonthS = '1'
# End
YearE = '1985'
MonthE = '6'

# Define single date, all the data we have appears to start on the first of each 
# month, so we insert a 1. the 0s are most time variables which are set to zero.
# We will convert our dates from the same format as the dataset ( :
# I am assuming the final zeros we see in the datasets are hours and minutes,
# so I include those in our date conversion below.
# See https://www.journaldev.com/23365/python-string-to-datetime-strptime for more info

# Single date
SingleDate = Year+', '+Month+', '+'1'+', '+'0'', '+'0'
# Python 2.7 is silly so this is how we call datetime strip (datetime.datetime.striptime())
SingleDate = datetime.datetime.strptime(SingleDate, '%Y, %m, %d, %H, %M')

# Range of Dates
StartDate = YearS+', '+MonthS+', '+'1'+', '+'0'', '+'0'
StartDate = datetime.datetime.strptime(StartDate, '%Y, %m, %d, %H, %M')
EndDate = YearE+', '+MonthE+', '+'1'+', '+'0'', '+'0'
EndDate = datetime.datetime.strptime(EndDate, '%Y, %m, %d, %H, %M')

# Convert this to a datetime item. This could be done several ways! For your purpose,
# it might be easier for you to be able to manipulate the year and month separately.
# So thats why I did it that way.

# Define our desired index, this will be the index value we use to pull data from
# our other datasets that relate to our sepecific date.
DesiredIndex = 0

for Date in Dates:
	Index = Date[0]
	Date = Date[1]
	# Printing this information we find our index,
	# our date, and data type for date. We are given
	# <type 'datetime.datetime'> for our date. So we need
	# to ensure our filtering method uses syntax for this specific format.
	# print Index
	# print Date
	# print type(Date)
	# sys.exit()

	# Here we filter our date data to extract it's location in the list.
	# remember, we added the index values in for visualization! So Date[0]
	# is the location of our index variable.
	if Date == SingleDate:
		print Date
		print Index
		# Lets take this index value as an integer for filtering later.
		DesiredIndex = int(Index)


# Lets select a date associated dataset from an item within our cdf! Oh Joy!

# We use our index value from dates to pull a record from TMP_SSFC at the same
# index. This will give us a dataset specific to the date we chose as a single 
# date.
TMP_SSFC_FSD = TMP_SSFC[DesiredIndex]
# Show the data for that year and month.
# print TMP_SSFC_FSD
# print type(TMP_SSFC_FSD)
# Data type returns: <type 'numpy.ndarray'> This can be converted to list if needed
# if its graphed with coordinates from a separate file, you will need the row and column
# information from the array. This would be crossed refernced with the coordinate data.

# Other parts of the dataset can be pulled in similarly. I started a section
# for filtering by a date range but I didn't finish it as I'm not certain if it's
# what you need.