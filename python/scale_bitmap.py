import wx

# https://stackoverflow.com/questions/2504143/how-to-resize-and-draw-an-image-using-wxpython
def scale_bitmap(bitmap, width, height):
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.Bitmap(image)
    return result
