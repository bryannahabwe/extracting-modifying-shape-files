import glob
import shapefile
import xlsxwriter

villages = []
shp_files = glob.glob("./shapefiles/apac_villages.shp")
w = shapefile.Writer("./apac/apac_villages.shp", encoding="utf8")
# Loop through ONLY the shp files and copy their shapes
# to a writer object. We avoid opening the dbf files
# to prevent any field-parsing errors.
for f in shp_files:
    r = shapefile.Reader(f)
    w.fields = r.fields[1:]  # skip first deletion field
    for shaperec in r.iterShapeRecords():
        print("APAC Records: %s" % shaperec.record['V'])
        villages.append(shaperec.record['V'])
print(villages)
workbook = xlsxwriter.Workbook('apac_villages.xlsx')
worksheet = workbook.add_worksheet()

array = [villages]

row = 0

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()
