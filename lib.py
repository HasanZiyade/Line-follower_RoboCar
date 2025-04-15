def direction(error):
    if -40 < error < 40:
        dutya = 100
        dutyb = 100
    elif 200 > error > 40:
        dutya = 50
        dutyb = 80
    elif -200 < error < -40:
        dutya = 80
        dutyb = 50
    elif -320 < error < -200:
        dutya = 70
        dutyb = 0
    elif error == -320:
        dutya = 0
        dutyb = 0
    elif error > 200:
        dutya = 0
        dutyb = 70
    else:
        dutya = 0
        dutyb = 0
    return dutya, dutyb

def camera(image):
    centerx_blk = 0
    roi = image[0:130, 0:639]
    Blackline = cv2.inRange(roi, (0, 0, 0), (90, 90, 90))
    kernel = np.ones((10,10), np.uint8)
    Blackline = cv2.morphologyEx(Blackline, cv2.MORPH_OPEN, kernel)
    Blackline = cv2.erode(Blackline, kernel, iterations=6)
    Blackline = cv2.dilate(Blackline, kernel, iterations=9)
    contours_blk, hierarchy_blk = cv2.findContours(Blackline.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	
    if len(contours_blk) > 0 :
       x_blk, y_blk , w_blk, h_blk = cv2.boundingRect(contours_blk[0])
       centerx_blk = int(x_blk + (w_blk/2))	   	   
       cv2.line(image, (centerx_blk, 200), (centerx_blk, 250),(255,0,0),3)
    setpoint = 320
    error = centerx_blk - setpoint
    centertext = "Error = " + str(error)
    cv2.putText(image, centertext, (200,340), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0),3)	
    cv2.imshow("orginal with line", image)
    cv2.imshow("blck", Blackline)
    return error