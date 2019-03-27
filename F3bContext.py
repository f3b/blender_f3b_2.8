from . import Logger as log

class F3bContext:
    def __init__(self,cfg,tofile,topath):
        self.cfg=cfg
        self.ids={}
        self.updateNeeded={}
        self.textures=[]    
        self.tofile=tofile
        self.topath=topath
    
    def idOf(self, v):
        vid=None
        if v in self.ids:
            vid=self.ids[v]
        else:
            vid=str(type(v).__name__)+"_"+str(hash(v))
        return vid  

    def setUpdateNeededFor(self, obj):
        vid = self.idOf(obj)
        self.updateNeeded[vid]=True
    
    def checkUpdateNeededAndClear(self,obj):
        vid=self.idOf(obj)
        res=True if not vid in self.updateNeeded else self.updateNeeded[vid]
        self.updateNeeded[vid]=False
        log.debug("%s update needed = %s" % (vid,res))
        return res