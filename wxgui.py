import wx


class DropTarget(wx.FileDropTarget):
    def __init__(self, parent):
        super().__init()
        self.textctl = parent

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((200, 200))

        self.panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetToolTip(u'Drop Here')

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, '')
        self.frame.Centre()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()