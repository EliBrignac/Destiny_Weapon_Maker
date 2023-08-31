    



while True:
    print('\n')
    image_urls = input("Enter URL thing: ")

    img_urls = image_urls.split("(")[1]
    print(img_urls)
    img_urls = img_urls[:-1]

    img_tags = []
    img_tags.append(f'<img src="{img_urls}" alt="Image" width=100% height =100%>')
    html_code = '\n'.join(img_tags)

    print('\n')

    print(html_code)
