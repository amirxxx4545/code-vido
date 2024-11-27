import cv2 # وارد کردن کتابخانه OpenCV

image_x="./images/alpha.jpg" # تعیین مسیر فایل تصویر
image=cv2.imread(image_x) # خواندن تصویر از مسیر مشخص شده
cv2.imshow("image",image) # نمایش تصویر در یک پنجره
cv2.waitKey(0) # منتظر ماندن برای ورودی کلید

cv2.destroyAllWindows() # بستن تمام پنجره‌ها
