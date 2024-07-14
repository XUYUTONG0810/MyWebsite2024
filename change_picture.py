from PIL import Image,ImageOps,ImageFilter,ImageDraw
import matplotlib.pyplot as plt

img = Image.open('挪威1.jpg')
width,height=img.size

# 图片变色
def change_colour(img, r_c, g_c, b_c):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][r_c]
            g = img_array[x,y][g_c]
            b = img_array[x,y][b_c]
            img_array[x,y] = (r, g, b)
    return img
    
# 灰度图
def gray(img):
    img_gray=img.convert('L')
    plt.rcParams['image.cmap']='gray'
    return img_gray

# 反色
def invert(img):
    img_invert=ImageOps.invert(img)
    return img_invert

# 高斯模糊
def gaussian(img):
    img_gaussian= img.filter(ImageFilter.GaussianBlur(5))
    return img_gaussian

# 全部透明
def alpha(img, a):
    img_alpha = img.convert('RGBA')
    img_alpha.putalpha(int(a))
    return img_alpha
