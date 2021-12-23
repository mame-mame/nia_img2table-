import os
import pandas as pd
import numpy as np
import cv2




import cells_detection
import ocr_image.__Init__
import ocr_to_csv
import easyocr

global reader


def convert(reader,input):




    img = cv2.imread(input)
    img_cp = img.copy()
    img_cp2 = img.copy()


    result = reader.readtext(img, paragraph=False)

    for i in result:
            cv2.rectangle(img, (int(i[0][0][0]), int(i[0][0][1])), (int(i[0][2][0]), int(i[0][2][1]) - 4),(255, 255, 255), -1)




    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 400, 450, apertureSize=5)




    minLineLength = 10
    maxLineGap = 35
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 70, minLineLength, maxLineGap)
    # for line in lines:
    #     for x1, y1, x2, y2 in line:
    #             print(line)
    #             cv2.line(img_cp2, (x1, y1), (x2, y2), (0, 0, 0), 2)
    #             cv2.imshow("test", img_cp2)
    #             cv2.waitKey(0)

    # #test 지점
    # img2 = np.zeros((900, 900, 3), np.uint8)
    # for line in lines:
    #     for x1, y1, x2, y2 in line:
    #         cv2.line(img2, (x1, y1), (x2, y2), (255, 255, 255), 2)
    #         cv2.imshow("test", img2)
    #         cv2.waitKey(0)



    min = np.min(lines, axis=0)
    max = np.max(lines, axis=0)
    x1_min = min[0][0]
    y1_min = min[0][1]
    x2_max = max[0][2]
    y1_max = max[0][1]

    cv2.line(img_cp, (x1_min, y1_min), (x1_min, y1_max), (0, 0, 0), 4)
    cv2.line(img_cp, (x2_max, y1_min), (x2_max, y1_max), (0, 0, 0), 4)
    cv2.line(img_cp, (x1_min, y1_min), (x2_max, y1_min), (0, 0, 0), 4)
    cv2.line(img_cp, (x1_min, y1_max), (x2_max, y1_max), (0, 0, 0), 4)


    garo = []
    sero = []

    line = np.squeeze(lines, axis=1)
    for x1, y1, x2, y2 in line:
        if x1 == x2: #세로
            sero.append([x1,y1,x2,y2])
        if y1 == y2: #가로
            # for j, i in enumerate(result) :
                # if int(i[0][0][1]) != y1 or int(i[0][2][1])-4 != y1:
                #     cv2.line(img_cp, (x1_min, y1), (x2_max, y2), (0, 0, 0), 2)
            garo.append([x1,y1,x2,y2])

            # print(garo)
            # print('----------garo----------')


    # for a, b in enumerate(garo):
    #     del garo[a][3]
    #     del garo[a][2]
    #     del garo[a][1]
    #     del garo[a][0]
    # garo = list(filter(None,garo))
    # print(garo)




    for i in result:
        for a, b in enumerate(garo):
            if((int(i[0][0][1])+1 >= b[1]) and (int(i[0][0][1])-1 <= b[1])) or ((int(i[0][2][1])-4 <= b[1]) and (int(i[0][2][1]) > b[1])):
                del garo[a][3]
                del garo[a][2]
                del garo[a][1]
                del garo[a][0]
        garo = list(filter(None, garo))


    for x1, y1, x2, y2 in sero:
        cv2.line(img_cp, (x2, y1_min), (x1, y1_max), (0, 0, 0), 2)

    for i, b in enumerate(garo):
        cv2.line(img_cp, (x1_min, b[1]), (x2_max, b[3]), (0, 0, 0), 2)








    # cv2.imshow("test", img_cp)
    # cv2.waitKey(0)





    # for line in lines:
    #     for x1, y1, x2, y2 in line:
    #         if x1 == x2:
    #             cv2.line(img_cp,(x2,y1_min),(x1,y1_max),(0,0,0),2)
    #         if y1 == y2:
    #             cv2.line(img_cp,(x1_min,y1),(x2_max,y2),(0,0,0),2)





    # cv2.imshow('test',img_cp)
    # cv2.waitKey(0)






    #
    # np.random.seed(42)
    # COLORS = np.random.randint(0, 255, size=(255, 3), dtype="uint8")
    #
    # for i in result:
    #     x = i[0][0][0]
    #     y = i[0][0][1]
    #     w = i[0][1][0] - i[0][0][0]
    #     h = i[0][2][1] - i[0][1][1]
    #
    #     color_idx = random.randint(0, 255)
    #     color = [int(c) for c in COLORS[color_idx]]
    #
    #     # cv2.putText(img, str(i[1]), (int((x + x + w) / 2), y - 2), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    #     img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    #

    #
    #
    #
    # image_tables = tables_detection.__Init__.extract_table(img_file,reader)
    # #print("Extracted the following tables from the image:")
    # #print(image_tables,"\n")
    html_string = []
    text_string = []

    image_cell,cells_num = cells_detection.extract_cell(img_cp)
    # for c in image_cell :
    #     cv2.imshow("test", c)
    #     cv2.waitKey(0)


    ######ocr_image 사용

    ocr = [
        ocr_image.__Init__.ocr_images(cell, reader)
        for cell in image_cell
            ]

    """
    ocr = []
    for cell in image_cell:
                reader.readtext(cell, paragraph=True, detail = 0)
                if
    """


    tt, hl = ocr_to_csv.text_files_to_csv(ocr, cells_num)
    text_string.append(tt)
    html_string.append(hl)

    tx = ','.join(text_string)
    hs = ','.join(html_string)





    """
    for i in image_cell:
        print("i==",i)
        ocr=[]cells = ocr_image.ocr_images(i,reader)
        html_string_return = ocr_to_csv.text_files_to_csv(cells)
    """

    """
    for image, tables in image_tables:
        #print(f"Processing tables for {image}.")

        for table in tables:
            #print(f"Processing table {table}.")
            cells = cells_detection.extract_cell(table)

            ocr = [
                ocr_image.ocr_images(cell, reader)
                for cell in cells
            ]
            #print("Extracted {} cells from {}".format(len(ocr), table))
            #print("Cells:")
            for c, o in zip(cells[:3], ocr[:3]):
                with open(o) as ocr_file:
                    # Tesseract puts line feeds at end of text.
                    # Stript it out.
                    text = ocr_file.read().strip()
                    #print("{}: {}".format(c, text))
            # If we have more than 3 cells (likely), print an ellipses
            # to show that we are truncating output for the demo.

            if len(cells) > 3:
                print("...",'\n')

            #csv_value, html_string_return = ocr_to_csv.text_files_to_csv(ocr,table)
            #print('\n',"Here is the entire CSV output:",'',csv_value,sep='\n')
            html_string_return = ocr_to_csv.text_files_to_csv(ocr, table)
    """

    # return tx, hs
    return hs

def evaluation(reader,test_dataset_dir, output_dir):
    if os.path.isdir(output_dir) == False:
        os.mkdir(output_dir)
    gt_txt_dir = os.path.join(test_dataset_dir, r'gt.txt')
    test_img_dir = os.path.join(test_dataset_dir, r'class')
    test_img_name = os.path.join(test_dataset_dir, r'name.txt')
    file_name = []
    gt_list = []
    n_correct = 0
    length_of_data = 0
    df = pd.DataFrame()
    TF=''

    try:
        with open(zip(gt_txt_dir, test_img_name), 'r') as f, e :
            gt_f = f.readlines()
            img_f = e.readlines()
            for  gt, name in zip(gt_f, img_f):
                gt_list.append(gt.split('\n')[0])
                file_name.append(name.split('t')[0])
        for i, image in enumerate(sorted(os.listdir(test_img_dir),key=len)):
            IMAGE_PATH = os.path.join(test_img_dir,image)
            html = convert(reader, os.path.join(test_img_dir, names))

            if html == gt_list[i]:
                n_correct += 1
                TF = 'True'
            else:
                TF = 'False'
            length_of_data += 1

            data = [{'파일명': file_name[i], '정답값': gt_list[i], '인식결과': html,
                     '일치여부': TF}]
            df = df.append(data, ignore_index = True)
            print(data)

    finally:
        df.to_csv(output_dir+'/testResult.csv',encoding='utf-8-sig')
        accuracy = n_correct / float(length_of_data)*100

        if os.path.isfile(output_dir+'/testResult.csv') == True:
            print('검증 데이터 갯수: ', length_of_data)
            print('일치도: ',accuracy)

            with open(output_dir + '/testResult.csv', 'a', newline='\n') as csvfile:
                wr = csv.writer(csvfile)
                wr.writerow(['검증 데이터 갯수', length_of_data])
                wr.writerow(['일치도', accuracy])


# def evaluation(reader,test_dataset_dir, output_dir):
#     if os.path.isdir(output_dir) == False:
#         os.mkdir(output_dir)
#     gt_txt_dir = os.path.join(test_dataset_dir, r'gt.txt')
#     test_img_dir = os.path.join(test_dataset_dir, r'class')
#     test_img_name = os.path.join(test_dataset_dir, r'name.txt')
#     file_name = []
#     gt_list = []
#     prediction = []
#     n_correct = 0
#     length_of_data = 0
#     df = pd.DataFrame()
#     gt_f = open(gt_txt_dir,'r')
#     img_f = open(test_img_name, 'r')
#     gt_data = gt_f.readlines()
#     img_data = img_f.readlines()
#     TF=''
#
#     for gt, name in zip(gt_data, img_data):
#         tgt, enter1 = gt.split('\n')
#         names, enter2 = name.split('\n')
#         print(names)
#         gt_list.append(tgt)
#         file_name.append(names)
#         html = convert(reader,os.path.join(test_img_dir,names))
#         prediction.append(html)
#     for i in range(len(gt_list)):
#         if prediction[i] == gt_list[i]:
#             n_correct += 1
#             TF ='True'
#         else :
#             TF = 'False'
#
#         length_of_data += 1
#         data = [{'파일명': file_name[i], '정답값': gt_list[i], '인식결과': prediction[i],
#                 '일치여부': TF}]
#         df = df.append(data, ignore_index=True)
#         print(data)
#
#     df.to_csv(os.path.join(output_dir,'testResult.csv'),encoding='utf-8-sig')
#     accuracy = n_correct / float(length_of_data) * 100
#     print(accuracy)
