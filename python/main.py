# https://www.tutorialspoint.com/wxpython/wxpython_drawing_api.htm

import wx
from scale_bitmap import scale_bitmap
 
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (1050,680))  
      self.InitUI() 
         
   def InitUI(self): 
      self.Bind(wx.EVT_PAINT, self.OnPaint) 
      self.Centre() 
      self.Show(True)
		
   def OnPaint(self, e): 
      dc = wx.PaintDC(self) 
      brush = wx.Brush("white")  
      dc.SetBackground(brush)  
      dc.Clear() 

      fieldBitmap = scale_bitmap(wx.Bitmap("common/football.jpg"), 1050, 680)
      dc.DrawBitmap(fieldBitmap, 0, 0, True) 
       
      englandBitmap = scale_bitmap(wx.Bitmap("common/england.jpg"), 25, 40)
      dc.DrawBitmap(englandBitmap, 105, 320, True) # Goal
      dc.DrawBitmap(englandBitmap, 190, 260, True) # Fullbacks
      dc.DrawBitmap(englandBitmap, 190, 380, True)
      dc.DrawBitmap(englandBitmap, 210,  95, True) # Centerbacks 
      dc.DrawBitmap(englandBitmap, 210, 545, True)
      dc.DrawBitmap(englandBitmap, 238, 320, True) # Midfielders
      dc.DrawBitmap(englandBitmap, 325, 235, True)
      dc.DrawBitmap(englandBitmap, 325, 415, True) 
      dc.DrawBitmap(englandBitmap, 390,  95, True)
      dc.DrawBitmap(englandBitmap, 390, 545, True)
      dc.DrawBitmap(englandBitmap, 480, 320, True) # Striker


ex = wx.App() 
Mywin(None, 'Codeball') 
ex.MainLoop()
