from gsheet import gsheet
from open_meteo import OpenMeteo

# open google sheet
gs = gsheet(workbook_name="acryl_data")

# loop through input values (lat and long)
for i, tup in enumerate(gs.inputs):
    gs_row = i+2
    lat = tup[0]
    long = tup[1]

    # pull values from weather API
    om = OpenMeteo(lat, long)
    gs.add_output_values(row=gs_row, outputs=om.output)
