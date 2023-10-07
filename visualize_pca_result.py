from matplotlib import pyplot as plt
from matplotlib.transforms import Bbox


def visualize_pca_result(pca_result):
    n_components = pca_result.shape[2]
    n_components_to_show = min(10, n_components)  # 最多顯示10個主成分

    fig, axes = plt.subplots(1, n_components_to_show, figsize=(n_components*2, 5))
    fig.suptitle('PCA Result by 111c51502')

    for i in range(n_components_to_show):
        ax = axes[i] if n_components_to_show > 1 else axes
        ax.imshow(pca_result[:, :, i], cmap='gray')
        ax.set_title(f'PC {i + 1}')

        if i == 0:  # 只在PC1上顯示X和Y軸的最大和最小刻度
            ax.set_xticks([0, pca_result.shape[1] - 1])
            ax.set_yticks([0, pca_result.shape[0] - 1])
        else:
            ax.axis('off')  # 對其它主成分隱藏軸

    plt.savefig('All_Principal_Components_test.pdf', dpi=2000)  # 保存圖像
    plt.show()





