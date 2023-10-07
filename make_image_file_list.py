import os
from datetime import datetime


def make_image_file_list(dataset_path):
    # 獲取所有 .TIF 檔案
    tif_files = [f for f in os.listdir(dataset_path) if f.endswith('.TIF')]

    # 獲取系統的年月日時分來命名.txt檔
    current_time = datetime.now().strftime("%Y%m%d%H%M")
    txt_filename = f"{current_time}.txt"

    # 寫入 .txt 檔
    with open(txt_filename, 'w') as txt_file:
        for tif_file in tif_files:
            txt_file.write(f"{dataset_path}\\{tif_file}\n")
    print(f"List of {len(tif_files)} .TIF files has been saved to : {txt_filename}")

    return txt_filename

