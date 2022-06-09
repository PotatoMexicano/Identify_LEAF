# Identify_LEAF
Identificação de elementos verdes em fotos, usado para detectar folhas/mato em fotos
![EPF_20220316135458_af1db44382964e22bc121a1fc84fa38c](https://user-images.githubusercontent.com/34165801/171314607-f4803803-e98c-416c-ba99-46b4ccad7430.jpg)

# Código

```python
import cv2
import numpy as np
import os 

caminho_imagem = input("Caminho Imagens: ")
for root, _, files in os.walk(caminho_imagem):
    for file in files:
        if file.endswith(".jpg"):
            imagem = os.path.join(root, file)
            img = cv2.imread(imagem)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            lower = np.array([27, 0, 20])
            upper = np.array([70, 255, 255])

            mask = cv2.inRange(hsv, lower, upper)

            total_pix = mask.size
            number_of_white_pix = np.sum(mask==255)
            number_of_black_pix = np.sum(mask==0)

            print(f"Brancos | Folhas: {number_of_white_pix}")
            print(f"Pretos | Não Folhas: {number_of_black_pix}")
            print("Porcentagem folhas: {:.0%}".format((number_of_white_pix/total_pix)))

            if (not(os.path.exists(os.path.join(caminho_imagem,'RESULT')))):
                os.makedirs(os.path.join(caminho_imagem, 'RESULT'))

            store = os.path.join(caminho_imagem, "RESULT",file)

            img2 = cv2.merge((mask,mask,mask))

            vis = np.concatenate((img, img2), axis=1)
            cv2.imwrite(store, vis)
```
