from django.contrib import sitemaps
from django.urls import reverse

class StaticViewsSitemap(sitemaps.Sitemap):
    protocol = 'https'
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ['index2']
    
    def location(self, item):
        return reverse(item)