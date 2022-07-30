# Youtube Video Downloader - Python
 

Python is one of the most powerful programming languages out there due to its versatility and the prevalence of libraries to achieve all sorts of interesting things.
We can automate our day-to-dat tasks by using python. 

Why do we need online video downloaders if we can create our own video downloader by using 4 lines of code?

---

you need to Install `pytube` library from
```
pip install pytube
```
check out more about [pytube](https://pytube.io/en/latest/)

---
## How to download 

specify the video quality by `yt.streams.get_by_resolution()` 

```python
downloader = yt.streams.get_by_resolution('720p')
downloader = yt.streams.get_by_resolution('1080')
downloader = yt.streams.get_highest_resolution()
```
specify the directory  
```python
download("/home/amantha/Downloads/")
```
pass the video link as a parameter
```shell
python main.py <video/link>
```