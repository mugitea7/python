from PIL import Image
import numpy as np

#元となる画像の読み込み
img = Image.open('qrcode_test.png')

#オリジナル画像の幅と高さを取得
width, height = img.size

#オリジナル画像と同じサイズのImageオブジェクトを作成する
img2 = img.resize((256,256))

img2.save('test.png')