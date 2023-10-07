from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import numpy as np
from osgeo import gdal
from tqdm import tqdm
import sys


def apply_lda_to_image(image_file_path, n_components, labels):
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

    # 改變形狀以適用LDA
    reshaped_img = np.reshape(img_array, (bands, -1)).T

    # 執行LDA
    print("\nPerforming LDA...")
    sys.stdout.flush()
    lda = LDA(n_components=n_components)
    lda_result = lda.fit_transform(reshaped_img, labels.ravel())

    # 將LDA結果轉換回原始的圖像形狀
    lda_img = np.reshape(lda_result, (rows, cols, n_components))

    return lda_img

