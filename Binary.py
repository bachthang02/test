import cv2 
from PIL import Image # Thư viện xử lí ảnh PILLOW hỗ trợ nhiều định dạng ảnh hơn so với cv2
import numpy as np

# Khai báo đường dẫn file hình
filehinh = r'lena_color.png'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

# Đọc ảnh màu dùng thư viện PILLOW. Ảnh PILLOW này dung để thực hiện các tác vụ xử lý và tính toán thay vì dung OpencV
imgPIL = Image.open(filehinh)

# Tạo 1 ảnh có cùng kích thước và mode với ảnh imgPIL. Ảnh này dungf để chứa kết quả chuyển đổi ảnh màu RGB sang Binary
binary = Image.new(imgPIL.mode, imgPIL.size)

# Lấy kích thước của ảnh từ imgPIL
width = binary.size[0]
height = binary.size[1]

# Thiết lập 1 giá trị ngưỡng để tính điểm ảnh nhị phân, đặt tên biến ngưỡng giá tri 130
Nguong = 90

# Mỗi ảnh là 1 ma trận 2 chiều nên sẽ dung 2 vòng for để quét, đọc tất cả các điểm ảnh (pixel) có trong ảnh.
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại vị trí (x, y)
        R, G, B = imgPIL.getpixel((x, y)) # RGB là 1 vector 3 giá trị trả về từ hàm getpixel tại vị trí xy tại các ảnh khi đọc từ thư viện PIlloW

        # Công thức chuyển đổi điểm ảnh màu RGB thành điểm ảnh mức xám Grayscale dung phương pháp Luminance
        gray = np.uint8(0.2126*R + 0.7152*G + 0.0722*B) # ép kiểu trả về kiểu 8 bit từ 0-255

        # xét giá trị điểm ảnh nhị phân
        if (gray < Nguong):

        # Gán giá trị mức xám vừa tính cho ảnh
            binary.putpixel((x, y), (0, 0, 0))
        else:
            binary.putpixel((x, y), (255, 255, 255))

# Chuyển ảnh từ PIL sang OpenCV để hiển thị bằng OpenCV
nhiphan = np.array(binary)

# Hiẻn thị ảnh dungf thư viện OpenCV
cv2.imshow('Anh mau RGB goc co gai Lena', img)
cv2.imshow('Anh nhi phan (Binary)', nhiphan)

# Bấm phím bất kì để đong của sổ hiển thị ảnh
cv2.waitKey(0)

# Giả phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị ảnh
cv2.destroyAllWindows()