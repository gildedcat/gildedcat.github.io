import qrcode

# GitHub Pages URL
url = 'https://gildedcat.github.io/produc_html.html'  # 替换为你的GitHub Pages URL

# 创建QRCode对象
qr = qrcode.QRCode(
    version=1,  # 控制二维码的大小，1是最小的21x21矩阵
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 纠错等级
    box_size=10,  # 每个“盒子”的像素数
    border=4,  # 边框厚度
)

# 添加数据
qr.add_data(url)
qr.make(fit=True)

# 生成二维码图像
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图像
img.save("qrcode.png")

# 打开二维码图像
img.show()


