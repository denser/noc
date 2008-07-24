from noc.setup.models import Settings

def tt_url(self):
    if self.tt:
        return Settings.get("tt.url")%{"tt":self.tt}
    else:
        return None
        
def admin_tt_url(self):
    if self.tt:
        return "<A HREF='%s'>#%d</A>"%(Settings.get("tt.url")%{"tt":self.tt},self.tt)
    else:
        return ""
