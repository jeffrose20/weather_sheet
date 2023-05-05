import gsheet
import open_meteo

gs = gsheet.gsheet(workbook_name="acryl_data")

for i, tup in enumerate(gs.inputs):
    gs_row = i+2
    lat = tup[0]
    long = tup[1]

    om = open_meteo.OpenMeteo(lat, long)
    gs.add_output_values(row=gs_row, outputs=om.output)
