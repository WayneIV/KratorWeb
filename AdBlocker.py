def setup_adblocker(self):
    self.webview.page().profile().setRequestInterceptor(self.request_interceptor)

def request_interceptor(self, request):
    url = request.url()
    # Block requests from known ad servers (simple example)
    ad_domains = ["doubleclick.net", "adservices.google.com"]
    if any(domain in url for domain in ad_domains):
        request.abort()  # Block the request

