class Memo:
    def update(self, state):
        for key in state:
            skey=str(key)
            if not skey.startswith("_"):
                setattr(self, key, state[key])
    
    @property
    def memo(self):
        ans = {}
        attrs = dir(self)
        for attr in self:
            print(attr)
            if hasattr(attr,'__self__') and not attr.startswith("_") and attr != "memo":
                value = getattr(self,attr)
                ans[attr]=value
        return ans

