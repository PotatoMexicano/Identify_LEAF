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

            #cv2.imshow('hsv', hsv)
            lower = np.array([27, 0, 20])
            upper = np.array([70, 255, 255])

            mask = cv2.inRange(hsv, lower, upper)

            total_pix = mask.size
            number_of_white_pix = np.sum(mask==255)
            number_of_black_pix = np.sum(mask==0)

            #print(f"Total pixels: {number_of_white_pix + number_of_black_pix}")
            print(f"Brancos | Folhas: {number_of_white_pix}")
            print(f"Pretos | Não Folhas: {number_of_black_pix}")
            print("Porcentagem folhas: {:.0%}".format((number_of_white_pix/total_pix)))

            #cv2.imshow("Image", img)
            #cv2.imshow("Mask", mask)
            #cv2.waitKey(0)
            if (not(os.path.exists(os.path.join(caminho_imagem,'RESULT')))):
                os.makedirs(os.path.join(caminho_imagem, 'RESULT'))

            store = os.path.join(caminho_imagem, "RESULT",file)

            #cv2.imwrite(store, mask)

            img2 = cv2.merge((mask,mask,mask))

            vis = np.concatenate((img, img2), axis=1)
            cv2.imwrite(store, vis)