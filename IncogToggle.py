def toggle_incognito(self):
    if self.incognito_mode:
        self.incognito_mode = False
        self.setWindowTitle("KratorWeb - Normal Mode")
    else:
        self.incognito_mode = True
        self.setWindowTitle("KratorWeb - Incognito Mode")
    
    # Toggle between normal mode and incognito mode settings
    self.setup_private_mode(self.incognito_mode)

def setup_private_mode(self, incognito):
    if incognito:
        self.webview.page().profile().clearHttpCache()
        self.webview.page().profile().clearHttpCookies()
        self.webview.setUrl(QUrl("about:blank"))
    else:
        self.webview.setUrl(QUrl(self.home_url))
