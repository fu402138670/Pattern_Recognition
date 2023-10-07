# pr_hw#02C_111c51502
# CY Chingyao Fu,
# AI-EMBA Program, NTUT
# 2023/10/07

from make_image_file_list import make_image_file_list
from get_images_list import get_images_list
from stack_image import stack_image
from PCA import apply_pca_to_image
from visualize_pca_result import visualize_pca_result
from save_pca_result_to_geotiff import save_pca_result_to_geotiff

import os
os.environ['PROJ_LIB'] = 'D:\\Programs\\GDAL\\bin\\proj9\\share'
from osgeo import gdal
gdal.UseExceptions()

# 指定原始衛星圖像目錄路徑
dataset_path = "D:\\CY\\Documents\\Python\\NTUT\\Pattern_Recognition\\Dataset\\EO1H1170422008059110PW_1T"
# dataset_path = "D:\\CY\\Documents\\Python\\NTUT\\Pattern_Recognition\\Dataset\\test"

# 建立圖像清單.txt檔
image_list_file_name = make_image_file_list(dataset_path)
print(f"The image list file name : {image_list_file_name}")

# 讀取圖像清單
image_list = get_images_list(image_list_file_name)
print(f"The image list length: {len(image_list)}")

# 叠加影像，結果輸出.TIF
stacked_filename = "stacked_hyperion_images.tif"
# stacked_filename = "stacked_test.tif"
stack_image(image_list, stacked_filename)

# PCA主成分分析
n_components = 10
analysis_result = apply_pca_to_image(stacked_filename, n_components)
# analysis_result = apply_pca_to_image(stacked_filename, n_components)

# LDA線性判別分析
# analysis_result = apply_lda_to_image(stacked_filename, n_components, labels)

# FLD Fisher's綫性判別分析
# analysis_result = apply_fld_to_image(stacked_filename, n_components, labels)

# PCA結果視覺化
if analysis_result is not None:
    visualize_pca_result(analysis_result)

    dataset = gdal.Open(stacked_filename)
    geo_transform = dataset.GetGeoTransform()
    projection = dataset.GetProjection()

    # 保存為GeoTIFF
    tif_file_name = "output_pca_result.tif"
    save_pca_result_to_geotiff(analysis_result, tif_file_name, geo_transform, projection)
