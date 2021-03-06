from ..core import Menu

class PrivMethodEdit(Menu):
    def __init__(self, scr, path):
        self.leaf = True
        self.skip = False
        Menu.__init__(self, scr, path, "Choose Methods")
        self.read = self.mkopt('r', "Read Permissions", ['+', self.updateparent])
        self.create = self.mkopt('w', "Create Permissions", ['+', self.updateparent])
        self.delete = self.mkopt('d', "Delete Permissions", ['+', self.updateparent])
        self.annotate = self.mkopt('n', "Annotate Permissions", ['+', self.updateparent])
        self.manage = self.mkopt('m', "Manage Permissions", ['+', self.updateparent])
        self.opts = [
            self.read,
            self.create,
            self.delete,
            self.annotate,
            self.manage,
            None,
            self.mkopt('h', "Help", '?'),
            self.mkopt('q', "Back", None, hdoc=False)]

    def show(self):
        if self.skip: self.skip = False
        else: Menu.show(self)

    def updateparent(self, _=None):
        methodstr = ''
        if self.read['val']: methodstr += 'r'
        if self.create['val']: methodstr += 'w'
        if self.delete['val']: methodstr += 'd'
        if self.annotate['val']: methodstr += 'n'
        if self.manage['val']: methodstr += 'm'
        if len(methodstr) == 0:
            msg = "At least one permission method must be selected."
            self.scr.msg = ('err', msg)
            return False
        self.option['val'] = methodstr

    def initialize(self):
        val = self.option['val']
        self.read['val'] = val != None and 'r' in val
        self.create['val'] = val != None and 'w' in val
        self.delete['val'] = val != None and 'd' in val
        self.annotate['val'] = val != None and 'n' in val
        self.manage['val'] = val != None and 'm' in val
