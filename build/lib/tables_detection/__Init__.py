import os
import cv2
import numpy as np


def table_polygon(image,reader):
    result = reader.readtext(image)

    x1 = x2 = y1 = y2 = 0;
    for r1 in result:
        for r2 in r1[0]:
            if (x1 == 0):
                x1 = r2[0]
            elif (x1 > r2[0]):
                x1 = r2[0]
            if (x2 == 0):
                x2 = r2[0]
            elif (x2 < r2[0]):
                x2 = r2[0]
            if (y1 == 0):
                y1 = r2[1]
            elif (y1 > r2[1]):
                y1 = r2[1]
            if (y2 == 0):
                y2 = r2[1]
            elif (y2 < r2[1]):
                y2 = r2[1]

    points = np.array([[x1, y1], [x1, y2], [x2, y2], [x2, y1]])
    print('points==',points)
    imagecopy = cv2.polylines(image, [points], True, (0, 0, 0),3)

    """
    cv2.imshow('blurred', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

    return imagecopy




def find_table(image):
    BLUR_KERNEL_SIZE = (17, 17)
    STD_DEV_X_DIRECTION = 0
    STD_DEV_Y_DIRECTION = 0
    blurred = cv2.GaussianBlur(image, BLUR_KERNEL_SIZE, STD_DEV_X_DIRECTION, STD_DEV_Y_DIRECTION)
    cv2.imshow('blurred', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    #블러처리
    MAX_COLOR_VAL = 255
    BLOCK_SIZE = 15
    SUBTRACT_FROM_MEAN = -2

    img_bin = cv2.adaptiveThreshold(
        ~blurred,
        MAX_COLOR_VAL,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        BLOCK_SIZE,
        SUBTRACT_FROM_MEAN,
    )
    vertical = horizontal = img_bin.copy()
    SCALE = 5
    image_width, image_height = horizontal.shape
    print(int(image_width/SCALE))
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (int(image_width / SCALE), 1))
    horizontally_opened = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, horizontal_kernel)
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(image_height / SCALE)))
    vertically_opened = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, vertical_kernel)


    horizontally_dilated = cv2.dilate(horizontally_opened, cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1)))
    vertically_dilated = cv2.dilate(vertically_opened, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 60)))


    mask = horizontally_dilated + vertically_dilated
    contours, heirarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE,
    )

    MIN_TABLE_AREA = 1e5
    contours = [c for c in contours if cv2.contourArea(c) > MIN_TABLE_AREA]
    perimeter_lengths = [cv2.arcLength(c, True) for c in contours]
    epsilons = [0.1 * p for p in perimeter_lengths]
    approx_polys = [cv2.approxPolyDP(c, e, True) for c, e in zip(contours, epsilons)]
    bounding_rects = [cv2.boundingRect(a) for a in approx_polys]



    # The link where a lot of this code was borrowed from recommends an
    # additional step to check the number of "joints" inside this bounding rectangle.
    # A table should have a lot of intersections. We might have a rectangular image
    # here though which would only have 4 intersections, 1 at each corner.
    # Leaving that step as a future TODO if it is ever necessary.
    images = [image[y:y + h, x:x + w] for x, y, w, h in bounding_rects]

    return images


def extract_table(file,reader):

    #directory, filename = os.path.split(file)
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    tables= find_table(image)





    if(tables==[]):
        print("진입")
        tables = find_table(table_polygon(image,reader))
    tables.reverse()






    """
    files = []
    filename_sans_extension = os.path.splitext(filename)[0]
    if tables:
        os.makedirs(os.path.join(directory, filename_sans_extension), exist_ok=True)

    for i, table in enumerate(tables):

        table_filename = "table-{:03d}.png".format(i)
        table_filepath = os.path.join(
            directory, filename_sans_extension, table_filename
        )
        files.append(table_filepath)
        cv2.imwrite(table_filepath, table)

    if tables:
        results.append((file, files))

    # Results is [[<input image>, [<images of detected tables>]]]
    """

    return tables