import sys
sys.path.append('D:\\Programs\\GDAL\\bin\\gdal\\python')
from osgeo import gdal, osr
gdal.UseExceptions()


def save_pca_result_to_geotiff(pca_result, output_filename, geo_transform, projection):
    height, width, num_bands = pca_result.shape
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(output_filename, width, height, num_bands, gdal.GDT_Float32)
    dataset.SetGeoTransform(geo_transform)
    dataset.SetProjection(projection)

    for i in range(num_bands):
        band = dataset.GetRasterBand(i + 1)
        band.WriteArray(pca_result[:, :, i])

    dataset.FlushCache()
    dataset = None

