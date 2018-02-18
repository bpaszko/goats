from urllib.request import urlretrieve
import os
from random import shuffle


def get_urls(path):
	with open(path, 'r') as f:
		lines = f.readlines()
	urls = [l.strip() for l in lines if l.strip()]
	shuffle(urls)
	return urls


def download_images(urls, save_dir, amount=270, offset=0):
	failed, current = 0, 1
	for url in urls:
		save_path = os.path.join(save_dir, str(current + offset) + '.jpg')
		try:
			urlretrieve(url, save_path)
		except Exception as e:
			print(e)
			failed += 1
			continue

		if current >= amount:
			break
		
		current += 1
	print('Failed: %d' % failed)


if __name__ == '__main__':
	images_urls = get_urls('/home/bartek/Workspace/promity/links.txt')
	download_images(images_urls, '/home/bartek/Workspace/promity/images', offset=280)