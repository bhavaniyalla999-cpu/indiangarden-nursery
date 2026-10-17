import os

def insert_after(content, target, insertion):
    idx = content.find(target)
    if idx != -1:
        end_idx = idx + len(target)
        return content[:end_idx] + "\n" + insertion + content[end_idx:]
    return content

def replace_between(content, start_target, end_target, replacement):
    start_idx = content.find(start_target)
    end_idx = content.find(end_target)
    if start_idx != -1 and end_idx != -1:
        return content[:start_idx] + replacement + content[end_idx:]
    return content


# 1. Update index.html
index_file = r'c:\Users\Admin\Desktop\Sri Bhaskar\index.html'
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

index_insertion1 = """    <link rel="canonical" href="https://sribhaskarnursery.vercel.app/">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="author" content="The Indian Garden Nursery">
    <meta name="geo.region" content="IN-AP">
    <meta name="geo.placename" content="Kadiyam, Rajahmundry">
    <meta name="geo.position" content="16.924843;81.859666">
    <meta name="ICBM" content="16.924843, 81.859666">"""

index_content = insert_after(index_content, '<meta name="keywords" content="The Indian Garden Nursery, Indian Garden Nursery, outdoor plants, landscaping services, Kadiyam nursery, avenue trees, flowering plants, palm trees, nursery Andhra Pradesh">', index_insertion1)

og_replacement = """    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_IN">
    <meta property="og:site_name" content="The Indian Garden Nursery">
    <meta property="og:title" content="The Indian Garden Nursery | Premium Outdoor Plants & Trees in Kadiyam">
    <meta property="og:description" content="India's trusted wholesale plant nursery in Kadiyam, Andhra Pradesh. 500+ varieties of outdoor plants, avenue trees, indoor plants & landscaping services. 20+ years experience.">
    <meta property="og:image" content="https://sribhaskarnursery.vercel.app/nursery-signboard.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="The Indian Garden Nursery - Premium Plant Nursery in Kadiyam">
    <meta property="og:url" content="https://sribhaskarnursery.vercel.app/">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="The Indian Garden Nursery | Premium Outdoor Plants & Trees">
    <meta name="twitter:description" content="India's trusted wholesale plant nursery. 500+ varieties, 20+ years experience. Kadiyam, AP.">
    <meta name="twitter:image" content="https://sribhaskarnursery.vercel.app/nursery-signboard.jpg">
    <meta name="twitter:image:alt" content="The Indian Garden Nursery Kadiyam">
"""
index_content = replace_between(index_content, '<!-- Open Graph -->', '    <!-- Google Search Console Verification -->', og_replacement)

manifest_insertion = """    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#2e7d32">
    <meta name="apple-mobile-web-app-title" content="The Indian Garden Nursery">"""
index_content = insert_after(index_content, '<link rel="icon" type="image/jpg" href="logo.jpg">', manifest_insertion)

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_content)


# 2. Update category pages
categories = {
    'outdoor.html': {
        'title': 'Outdoor Plants Wholesale — The Indian Garden Nursery, Kadiyam',
        'desc': 'Premium outdoor plants for villas, resorts, and estates. Palms, flowering plants, and ornamental trees at wholesale prices.',
        'img': 'nursery-real-12.jpg'
    },
    'indoor.html': {
        'title': 'Indoor Plants Wholesale Supplier — The Indian Garden Nursery',
        'desc': 'Premium indoor plants for your home and office. Healthy, low-maintenance indoor greenery at wholesale prices.',
        'img': 'indoor-palm.jpg'
    },
    'avenue.html': {
        'title': 'Avenue Trees Wholesale Supplier — Kadiyam AP',
        'desc': 'Premium avenue trees and large-scale plantation stock. Healthy, fast-growing trees for roadsides, parks, and estates.',
        'img': 'avenue-trees.png'
    },
    'ornamental.html': {
        'title': 'Ornamental & Flowering Plants Wholesale — The Indian Garden Nursery',
        'desc': 'Premium ornamental plants for architectural landscaping and luxury gardens. High-quality topiary and decorative plants.',
        'img': 'round-topiary.jpg'
    },
    'fruit.html': {
        'title': 'Fruit Plants Wholesale — Mango, Star Fruit | The Indian Garden Nursery',
        'desc': 'High-yielding fruit plants and saplings. Mango, Guava, Lemon, and exotic fruit varieties for your orchard.',
        'img': 'banana-mango.jpg'
    }
}

for cat_file, data in categories.items():
    path = os.path.join(r'c:\Users\Admin\Desktop\Sri Bhaskar', cat_file)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find meta description end
        desc_start = content.find('<meta name="description"')
        if desc_start != -1:
            desc_end = content.find('>', desc_start)
            if desc_end != -1:
                insertion = f"""
    <link rel="canonical" href="https://sribhaskarnursery.vercel.app/{cat_file}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_IN">
    <meta property="og:site_name" content="The Indian Garden Nursery">
    <meta property="og:title" content="{data['title']}">
    <meta property="og:description" content="{data['desc']}">
    <meta property="og:image" content="https://sribhaskarnursery.vercel.app/{data['img']}">
    <meta property="og:url" content="https://sribhaskarnursery.vercel.app/{cat_file}">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{data['title']}">
    <meta name="twitter:description" content="{data['desc']}">
    <meta name="twitter:image" content="https://sribhaskarnursery.vercel.app/{data['img']}">"""
                content = content[:desc_end+1] + insertion + content[desc_end+1:]
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)

# 3. Update Utility Pages
utils = {
    'cart.html': {
        'title': '<title>My Cart — The Indian Garden Nursery</title>',
        'insert': """
    <meta name="description" content="Review your selected plants before checkout. The Indian Garden Nursery cart.">
    <meta name="robots" content="noindex, nofollow">
    <link rel="canonical" href="https://sribhaskarnursery.vercel.app/cart.html">
    <link rel="icon" type="image/jpg" href="logo.jpg">"""
    },
    'checkout.html': {
        'title': '<title>Checkout — The Indian Garden Nursery</title>',
        'insert': """
    <meta name="description" content="Secure checkout for your plant order. The Indian Garden Nursery.">
    <meta name="robots" content="noindex, nofollow">
    <link rel="canonical" href="https://sribhaskarnursery.vercel.app/checkout.html">
    <link rel="icon" type="image/jpg" href="logo.jpg">"""
    },
    'privacy.html': {
        'title': '<title>Privacy Policy | The Indian Garden Nursery</title>',
        'insert': """
    <meta name="description" content="Privacy Policy for The Indian Garden Nursery. Learn how we collect and use your information.">
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="https://sribhaskarnursery.vercel.app/privacy.html">
    <link rel="icon" type="image/jpg" href="logo.jpg">"""
    }
}

for util_file, data in utils.items():
    path = os.path.join(r'c:\Users\Admin\Desktop\Sri Bhaskar', util_file)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = insert_after(content, data['title'], data['insert'])
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)


# 4. Sitemap
sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://sribhaskarnursery.vercel.app/</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <image:image>
      <image:loc>https://sribhaskarnursery.vercel.app/nursery-signboard.jpg</image:loc>
      <image:title>The Indian Garden Nursery Kadiyam</image:title>
      <image:caption>The Indian Garden Nursery - Premium Plant Nursery in Kadiyam, Andhra Pradesh</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://sribhaskarnursery.vercel.app/logo.jpg</image:loc>
      <image:title>The Indian Garden Nursery Logo</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://sribhaskarnursery.vercel.app/outdoor.html</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <image:image>
      <image:loc>https://sribhaskarnursery.vercel.app/avenue-trees.png</image:loc>
      <image:title>Premium Avenue Trees</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://sribhaskarnursery.vercel.app/indoor.html</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <image:image>
      <image:loc>https://sribhaskarnursery.vercel.app/indoor-palm.jpg</image:loc>
      <image:title>Indoor Plants Collection</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://sribhaskarnursery.vercel.app/avenue.html</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <image:image>
      <image:loc>https://sribhaskarnursery.vercel.app/avenue-trees.png</image:loc>
      <image:title>Avenue Trees Collection</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://sribhaskarnursery.vercel.app/ornamental.html</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <image:image>
      <image:loc>https://sribhaskarnursery.vercel.app/round-topiary.jpg</image:loc>
      <image:title>Ornamental Plants Collection</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://sribhaskarnursery.vercel.app/fruit.html</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <image:image>
      <image:loc>https://sribhaskarnursery.vercel.app/banana-mango.jpg</image:loc>
      <image:title>Fruit Plants Collection</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://sribhaskarnursery.vercel.app/cart.html</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.4</priority>
  </url>
  <url>
    <loc>https://sribhaskarnursery.vercel.app/checkout.html</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://sribhaskarnursery.vercel.app/privacy.html</loc>
    <lastmod>2026-06-02</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.2</priority>
  </url>
</urlset>"""

with open(r'c:\Users\Admin\Desktop\Sri Bhaskar\sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)


# 5. Robots
robots = """User-agent: *
Allow: /
Disallow: /cart.html
Disallow: /checkout.html
Disallow: /orders.html
Disallow: /delivery-report.html

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

Sitemap: https://sribhaskarnursery.vercel.app/sitemap.xml"""

with open(r'c:\Users\Admin\Desktop\Sri Bhaskar\robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots)

print("Updates applied successfully.")
