# Help-With-CDFs
This is to help my pal open and view data from a CDF

We import a cdf file using the SpacePy import. Calling the data through strings given
by a simple print statement. That essentially maps out what is in your file.

If you end up needing to map any data,
it is rather difficult at times in python. Many mapping imports are originally written 
in C++. If you need to use mapping functions within python, you can access pre-compiled
.whl files for them from here: https://www.lfd.uci.edu/~gohlke/pythonlibs/

Some modules you may need are GDAL, Fiona, Rasterio, Shapely, or GeoPandas. The dependancies
between the modules can be confusing. So let me know if you decide to make the maps 
in python. Otherwise, you may be able to extract the rest of that data into a single
.csv file and import it to ArcMap. Just keep an eye our for a coordinate reference
system.

# NOTE: There is a copy of the .cdf file in case the other gets corrupted!


