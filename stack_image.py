import sys

sys.path.append('D:\\Programs\\GDAL\\bin\\gdal\\python')
from osgeo import gdal
gdal.UseExceptions()


def stack_image(tiff_files, output_filename):
    # 讀取第一個檔案以獲取基本信息
    first_ds = gdal.Open(tiff_files[0], gdal.GA_ReadOnly)
    rows, cols = first_ds.RasterYSize, first_ds.RasterXSize
    geo_transform = first_ds.GetGeoTransform()
    proj = first_ds.GetProjectionRef()
    first_ds = None  # 關閉數據集

    # 創建新的多波段TIFF檔案
    driver = gdal.GetDriverByName('GTiff')
    out_ds = driver.Create(output_filename, cols, rows, len(tiff_files), gdal.GDT_Float32)
    out_ds.SetGeoTransform(geo_transform)
    out_ds.SetProjection(proj)

    # 叠加每個波段
    for i, tiff_file in enumerate(tiff_files):
        in_ds = gdal.Open(tiff_file, gdal.GA_ReadOnly)
        in_band = in_ds.GetRasterBand(1)

        out_band = out_ds.GetRasterBand(i + 1)
        out_band.WriteArray(in_band.ReadAsArray())

        in_ds = None  # 關閉數據集

        completion_percentage = ((i + 1) / len(tiff_files)) * 100
        print("\rImage stacking completed: {:.2f}%".format(completion_percentage), end="", flush=True)

    # 保存並關閉多波段TIFF檔案
    print("\nImage stacking completed")
    out_ds.FlushCache()
    out_ds = None

