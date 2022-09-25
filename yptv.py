#!/usr/bin/env python
def get_high_res(url):
 from pytube import YouTube
 yt = YouTube(url)

 return yt.streams.get_highest_resolution().url


url = 'https://www.youtube.com/watch?v=yWtWt-e_p24'

m3u = get_high_res(url)
print(m3u)
