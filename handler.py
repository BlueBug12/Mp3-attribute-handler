# -*- coding: utf-8 -*-
from langconv import Converter
import os
from mutagen.id3 import ID3
import mutagen

path="location/of/files"
for item in os.listdir(path):
	print(item)
	song = ID3(path+'/'+item)
	name=Converter('zh-hant').convert(item)
	
	"""
	key:
		'TIT2':title
		'TALB':album
		'TPE1':artist
	"""

	title = Converter('zh-hant').convert(song['TIT2'][0])
	album = Converter('zh-hant').convert(song['TALB'][0])
	artist = Converter('zh-hant').convert(song['TPE1'][0])

	song.add(mutagen.id3.TIT2(encoding=1, text=title))
	song.add(mutagen.id3.TALB(encoding=1, text=album))
	song.add(mutagen.id3.TPE1(encoding=1, text=artist))
	song.save()
	
	os.rename(path+'/'+item,path+'/'+name)