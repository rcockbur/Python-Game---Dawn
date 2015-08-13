class Obserber(object):
    def __init__(self):
        self.viewList = list()
        
    def addView(self, view):
        self.viewList.append(view)
        
    def notifyViews(self):
        for view in self.viewList:
            view.notifyUpdate()
        