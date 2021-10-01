import glob
import shapefile

shp_files = glob.glob("./shape_files/*.shp")
w = shapefile.Writer("./new_shape_files/east_africa.shp", encoding="utf8")
# Loop through ONLY the shp files and copy their shapes
# to a writer object. We avoid opening the dbf files
# to prevent any field-parsing errors.
for f in shp_files:
    r = shapefile.Reader(f)
    print("Fields : %s" % r.fields)
    w.fields = r.fields[1:]  # skip first deletion field
    for shaperec in r.iterShapeRecords():
        w.record(*shaperec.record)
        w.shape(shaperec.shape)
w.close()
