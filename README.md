# Traditional_Chinese_Scene-OCR

## 硬體環境
- Windows 10
- CPU : Intel(R) Core(TM) i7-10700 CPU / 2.90 GHz / 8 核心
- GPU: NVIDIA GeForce RTX 3090
- 記憶體（RAM）：32 GB

## Requirements

* Python = 3.7
* cuda = 11.3
* cudnn = 8.2.1
* tf2.5（tf-nightly）或 tf1.15.4
* pytorch = 1.8
* keras = 2.3
* tqdm
* opencv-python
* matplotlib
* easyocr

## 安裝步驟
### 創建環境

```
conda create --name <name> python=3.7
conda activate <name>
```

**如果要刪除環境請使用 ```conda env remove -n <name>```**

### 安裝套件

```
pip3 install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
```

```
conda install cudatoolkit=11.3
conda install cudnn=8.2
```

```
conda install tensorflow-gpu=2.5
conda install -c conda-forge keras=2.3
pip install tqdm
pip install opencv-python
pip install matplotlib
pip install easyocr
```

## Generate label data

使用 json2txt.py 將 JSON 檔的資訊轉換為 txt 格式。

此程式碼中的 `json_root` 為欲讀取的 JSON 檔路徑，`txt_root` 為轉換過後的 txt 存放的路徑。
另外，`obj_names = 'data/train/obj.names'` 為 `.names` 檔存放的路徑，請先下載 [obj.names](https://drive.google.com/file/d/1itnRYL0KrQL0Dsnpx_-cVezLL1np0fRN/view?usp=sharing)

## Training

請先至 [Download](https://drive.google.com/drive/folders/1aSlwNK183ecMWAFz_MfW71xBe4ljnrtM?usp=sharing) 下載所需 weights、cfg、yaml、data 等檔案

```
python train.py --device 0 --batch-size 8 --data data/chinese_ocr.yaml --cfg cfg/chinese_ocr.cfg --weights weights/ocr.pt --name ocr
```

若遇到以下錯誤碼：
```
RuntimeError: CUDA out of memory. Tried to allocate 452.00 MiB (GPU 0; 24.00 GiB total capacity; 20.32 GiB already allocated; 1.24 GiB free; 20.53 GiB reserved in total by PyTorch)
```

此為 GPU 記憶體不足，請將 batch-size 調小即可。

## Detect
```
python detect.py --weights weights/ocr.pt --cfg cfg/chinese_ocr.cfg --name data/obj.names
```
