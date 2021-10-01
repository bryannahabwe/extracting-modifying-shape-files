import glob
import shapefile

shp_files = glob.glob("./shapefile/*.shp")
w = shapefile.Writer("./gulu/gulu_parishes.shp", encoding="utf8")
# Loop through ONLY the shp files and copy their shapes
# to a writer object. We avoid opening the dbf files
# to prevent any field-parsing errors.
for f in shp_files:
    r = shapefile.Reader(f)
    w.fields = r.fields[1:]  # skip first deletion field
    for shaperec in r.iterShapeRecords():
        if 'Gulu' in shaperec.record:
            print("Gulu Records: %s" % shaperec.record)
            w.record(*shaperec.record)
            w.shape(shaperec.shape)
w.close()
