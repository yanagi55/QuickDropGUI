import wx
import wx.lib.newevent
drop_event, EVT_DROP_EVENT = wx.lib.newevent.NewEvent()

class DropTarget(wx.FileDropTarget):
    def __init__(self, parent):
        wx.FileDropTarget.__init__(self)
        self.obj = parent
        # self.file = False

    def OnDropFiles(self, x, y, filenames):
        evt = drop_event(data=filenames)
        wx.PostEvent(self.obj.frame, evt)
        return True
        # if os.path.isdir(filenames[0]):
        #     self.file = False
        # else:
        #     self.file = True
        # return True
        # test.append(filenames)


class GUI:
    def __init__(self):
        self.frame = wx.Frame(None, -1, 'list')
        self.frame.SetTitle(u'Drop Here')
        self.frame.Centre()
        panel = wx.Panel(self.frame, wx.ID_ANY, size=(200,200))
        panel.SetToolTip(u'Drop Here')

        self.frame.drop = DropTarget(self)
        self.frame.SetDropTarget(self.frame.drop)
        self.frame.Bind(EVT_DROP_EVENT, self.OnDropped)

        self.frame.Show()
    
    def OnDropped(self, event):
        # self.frame.datas.append(event.data)
        self.frame.data = event.data
        self.frame.Close(True)



def get_filelist() -> list[str]:
    app = wx.App()
    gui = GUI()
    app.SetTopWindow(gui.frame)
    app.MainLoop()
    return gui.frame.data


if __name__ == '__main__':
    test = get_filelist()
    print(test)