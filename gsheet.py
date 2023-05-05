import gspread


class gsheet:
    def __init__(self, workbook_name: str, sheet_name: str = "Sheet1"):
        """
            Input: workbook_name, sheet_name

            opens up a google sheet and loads lat / long values
        """
        # open / load sheet using gspread
        self.workbook_name = workbook_name
        self.sheet_name = sheet_name

        self.gc = gspread.service_account()
        self.wb = self.gc.open(self.workbook_name)
        self.ws = self.wb.worksheet(self.sheet_name)

        # grab the relevant lat and long values
        self.inputs = self.get_lat_long_values()


    def get_lat_long_values(self) -> list:
        """
            Get values in the first two columns and remove headers
            Return as a list of tuples [(lat, long)]
        """
        lats = self.ws.col_values(1)[1:]
        longs = self.ws.col_values(2)[1:]
        return list(zip(lats, longs))

    def add_output_values(self, row: str, outputs: tuple):
        for i, val in enumerate(outputs):
            col = i+3
            self.ws.update_cell(row, col, val)
        pass

if __name__ == "__main__":
    gs = gsheet(workbook_name="acryl_data")
