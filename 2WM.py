import qrcode
import base64

# 自定义HTML内容
html_content = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>产品详情页</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .product-image { width: 100%; }
        .price { color: red; font-size: 24px; }
        .buy-button { background-color: orange; color: white; padding: 10px 20px; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>产品详情页</h1>
        < img src="https://vip.helloimg.com/i/2024/07/14/66934ac06a19a.png" alt="产品图片" class="product-image">
        <p>这是一个示例产品页面，包含产品的详细信息。</p >
        <p class="price">价格：¥8380</p >
        <button class="buy-button">立即购买</button>
    </div>
</body>
</html>
'''

# 将HTML内容转换为Base64编码
encoded_html = base64.b64encode(html_content.encode()).decode()

# 创建数据URI
data_uri = f"data:text/html;base64,{encoded_html}"

# 创建QRCode对象
qr = qrcode.QRCode(
    version=None,  # 自动选择合适的版本
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 纠错等级
    box_size=10,  # 每个“盒子”的像素数
    border=4,  # 边框厚度
)

# 添加数据URI
qr.add_data(data_uri)
qr.make(fit=True)

# 生成二维码图像
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图像
img.save("qrcode_custom.png")

# 打开二维码图像
img.show()

