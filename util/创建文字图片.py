from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 创建图像尺寸和背景
width, height = 1920, 1080
img = Image.new('RGB', (width, height), color='black')
draw = ImageDraw.Draw(img)

# 尝试使用中文字体（请确保您系统有以下字体或修改为已有中文字体）
try:
    # 尝试几种常见中文字体
    font = ImageFont.truetype("SimHei.ttf", 80)  # 黑体
except:
    try:
        font = ImageFont.truetype("msyh.ttf", 80)  # 微软雅黑
    except:
        try:
            font = ImageFont.truetype("simsun.ttc", 80)  # 宋体
        except:
            # 如果都找不到，使用默认字体（可能不支持中文）
            font = ImageFont.load_default()

# 文字内容
text = "不支持的格式,或预览超时.\n请下载至本地打开"

# 获取文字尺寸
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# 计算文字位置（居中）
x = (width - text_width) / 2
y = (height - text_height) / 2

# 添加文字阴影效果（轻微模糊）
shadow_color = (50, 50, 50)  # 深灰色阴影
for i in range(5):  # 绘制多次创建模糊效果
    offset_x = x + random.randint(-3, 3)
    offset_y = y + random.randint(-3, 3)
    draw.text((offset_x, offset_y), text, font=font, fill=shadow_color)

# 绘制主文字
draw.text((x, y), text, font=font, fill='white')

# 添加装饰性分隔线
line_y = y + text_height + 30
draw.line([(x, line_y), (x + text_width, line_y)], fill='gray', width=2)

# 保存图片
img.save('d://error_message.jpg', 'JPEG')
print("图片已生成并保存为 error_message.jpg")
