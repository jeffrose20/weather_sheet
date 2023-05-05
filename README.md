# weather_sheet
 Pull weather data from an API and insert into a google sheet

## Specifications
- Read the requested latitudes and longitudes (from columns A and B).
- Fetch the latest weather information for each latitude/longitude.
- Write that information back into the sheet (into columns C, D, and E). Note that column E should just contain the timestamp of when the data was fetched from the weather API.
- This was written / tested in Python 3.7

## Resources
- Weather API docs: https://open-meteo.com/.
- Google Sheets API docs: https://developers.google.com/sheets/api/guides/concepts.
- Authentication for Google Sheets: https://docs.gspread.org/en/latest/oauth2.html

## Using the tool
- The driver script is `app.py`.  You need to set up your google sheet according the authentication link above and provide the sheet name.  
- Internal wrapper functions have been added to simplify API calls for OpenMeteo and Google Sheets.
- Run the tool like this: `python3 app.py`
- Example of output during testing:
![alt text](https://github.com/jeffrose20/weather_sheet/blob/main/output.jpg?raw=true)

