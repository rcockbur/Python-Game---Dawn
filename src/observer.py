class Observer(object):
    def __init__(self):
        self.viewList = list()
        
    def addView(self, gameView):
        self.viewList.append(gameView)
        
    def notifyViews(self):
        for gameView in self.viewList:
            gameView.notifyUpdate()
        