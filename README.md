# waifu_im.py
Web-API for [waifu.im](https://waifu.im) website for getting anime pictures

## Example
```python3
import waifu_im
waifu_client = waifu_im.WaifuClient(token="")
image = waifu_client.get_random_image()
print(f"-- Image url::: {image['images'][0]['url']}")
```
