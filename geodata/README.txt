Using the Google Places API with a Database and
Visualizing Data on Google Map

En este proyecto, usamos Google geocoding API para limpiar
algunas ubicaciones geográficas ingresadas por el usuario de
nombres de universidades y luego colocamos los datos en un 
GoogleMap.

---------------------------------------------------------
Notes: 
1)Windows has difficulty in displaying UTF-8 characters
in the console so for each command-window you open, you may need
to type the following command before, running this code:

D:\phytonSpace\freeCodeCamp\python\myLessons>chcp 65001
Página de códigos activa: 65001

2)explain chcp:
http://stackoverflow.com/questions/388490/unicode-characters-in-windows-command-line-how

3)You should install the SQLite browser to view and modify
the databases from: http://sqlitebrowser.org/
-----------------------------------------------------------

The first problem to solve is that the Google geocoding
API is rate limited to a fixed number of requests per day.
So if you have a lot of data you might need to stop and
restart the lookup process several times. So them we break
the problem into two phases.

In the first phase 'geoload.py' we take our input data from file 
'where.data' and read it one line at a time, and retrieve the geocoded
 response from google and then store it in a database (geodata.sqlite).

------------------------------------------------------------------
note:
Before we use the 'geocoding API', we first simply check to see 
if we are already have the data for that particular line of input.
this something the previus step to be sure all are running okey and
before we jump to real world.

You can re-start the process at any time by removing the file
geodata.sqlite
-------------------------------------------------------------------
Run the 'geoload.py' program; This program will read the input
lines from 'where.data' and for each line going to check if it is already
in the database and if we can't retrieve the data for the location, them
call the 'geocoding API' to retrieve the data from google in JSON format
and store it in the database.

from December 2016 today, the Google Geocoding APIs was changed dramatically.
They moved some functionality that we use from the 'Geocoding API'
into the 'Places API'.  Also all the Google Geo-related APIs require an
API key. To complete this assignment without a Google account,
without an API key, or from a country that blocks
access to Google, you can use a subset of that data which is
available at:

http://py4e-data.dr-chuck.net/json

To use this, simply leave the api_key set to False in 
geoload.py.

This URL only has a subset of the data but it has no rate limit so
it is good for testing.

If you want to try this with the API key, follow the
instructions at:

https://developers.google.com/maps/documentation/geocoding/intro

and put the API key in the code.

Here is a sample run after there is already some data in the
database:

Mac: python3 geoload.py
Win: geoload.py

Found in database  Northeastern University

Found in database  University of Hong Kong, Illinois Institute of Technology, Bradley University

Found in database  Technion

Found in database  Viswakarma Institute, Pune, India

Found in database  UMD

Found in database  Tufts University

Resolving Monash University
Retrieving http://py4e-data.dr-chuck.net/json?key=42&address=Monash+University
Retrieved 2063 characters {    "results" : [
{u'status': u'OK', u'results': ... }

Resolving Kokshetau Institute of Economics and Management
Retrieving http://py4e-data.dr-chuck.net/json?key=42&address=Kokshetau+Institute+of+Economics+and+Management
Retrieved 1749 characters {    "results" : [
{u'status': u'OK', u'results': ... }

The first five locations are already in the database and so they
are skipped.  The program scans to the point where it finds un-retrieved
locations and starts retrieving them.

The geoload.py can be stopped at any time, and there is a counter
that you can use to limit the number of calls to the geocoding
API for each run.

Once you have some data loaded into geodata.sqlite, you can
visualize the data using the (geodump.py) program.  This
program reads the database and writes tile file (where.js)
with the location, latitude, and longitude in the form of
executable JavaScript code.

A run of the geodump.py program is as follows:

Mac: python3 geodump.py
Win: geodump.py

Northeastern University, 360 Huntington Avenue, Boston, MA 02115, USA 42.3396998 -71.08975
Bradley University, 1501 West Bradley Avenue, Peoria, IL 61625, USA 40.6963857 -89.6160811
...
Technion, Viazman 87, Kesalsaba, 32000, Israel 32.7775 35.0216667
Monash University Clayton Campus, Wellington Road, Clayton VIC 3800, Australia -37.9152113 145.134682
Kokshetau, Kazakhstan 53.2833333 69.3833333
...
12 records written to where.js
Open where.html to view the data in a browser

The file (where.html) consists of HTML and JavaScript to visualize
a Google Map.  It reads the most recent data in where.js to get
the data to be visualized.  Here is the format of the where.js file:

myData = [
[42.3396998,-71.08975, 'Northeastern University, 360 Huntington Avenue, Boston, MA 02115, USA'],
[40.6963857,-89.6160811, 'Bradley University, 1501 West Bradley Avenue, Peoria, IL 61625, USA'],
[32.7775,35.0216667, 'Technion, Viazman 87, Kesalsaba, 32000, Israel'],
   ...
];

This is a JavaScript list of lists.  The syntax for JavaScript
list constants is very similar to Python so the syntax should
be familiar to you.

Simply open where.html in a browser to see the locations.  You
can hover over each map pin to find the location that the
geocoding API returned for the user-entered input.  If you
cannot see any data when you open the where.html file, you might
want to check the JavaScript or developer console for your browser.

