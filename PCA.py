from sklearn.decomposition import PCA
from tqdm import tqdm
import joblib
import numpy as np
import sys
sys.path.append('D:\\Programs\\GDAL\\bin\\gdal\\python')
from osgeo import gdal
gdal.UseExceptions()


def apply_pca_to_image(image_file_path, n_components, temp_storage_path='temp_pca_data.joblib'):
    # 打開GeoTIFF檔案
    ds = gdal.Open(image_file_path)
    if ds is None:
        print("Could not open image file.")
        return

    bands = ds.RasterCount
    rows = ds.RasterYSize
    cols = ds.RasterXSize
    print(f"bands:{bands}, rows:{rows}, cols:{cols}")

    # 將所有波段數據存儲到一個NumPy數組中
    img_array = np.zeros((bands, rows, cols), dtype=np.float32)

    for i in tqdm(range(1, bands + 1), desc='Reading bands', file=sys.stdout):
        band = ds.GetRasterBand(i)
        img_array[i - 1, :, :] = band.ReadAsArray()
        sys.stdout.flush()

    # 保存原始數據以減少記憶體使用
    # joblib.dump(img_array, temp_storage_path)

    # 從硬碟加載數據
    # img_array = joblib.load(temp_storage_path)

    # 改變形狀以適用PCA
    reshaped_img = np.reshape(img_array, (bands, -1)).T

    # 中心化數據：減去每一列的平均值
    reshaped_img -= np.mean(reshaped_img, axis=0)

    # 執行PCA
    print("\nPerforming PCA...")
    sys.stdout.flush()
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(reshaped_img)

    # 保存PCA結果以減少記憶體使用
    # joblib.dump(pca_result, 'pca_result.joblib')

    # 從硬碟加載PCA結果
    # pca_result = joblib.load('pca_result.joblib')
    # pca_img = np.reshape(pca_result, (rows, cols, n_components))

    # 變異比例
    explained_variance_ratios_percent = [f"{x * 100:.4f}%" for x in pca.explained_variance_ratio_]
    total_explained_variance_percent = f"{sum(pca.explained_variance_ratio_) * 100:.4f}%"

    print("Explained Variance Ratios:", explained_variance_ratios_percent)
    print("Total Explained Variance:", total_explained_variance_percent)

    # 將PCA結果轉換回原始的圖像形狀
    pca_img = np.reshape(pca_result, (rows, cols, n_components))

    return pca_img

