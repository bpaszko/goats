from random import shuffle
import os


def move_files(files, dest_dir):
	for source_path in files:
		f_name = source_path.split('/')[-1]
		dest_path = os.path.join(dest_dir, f_name)
		os.rename(source_path, dest_path)


def split_data(source_dir, train_dir, test_dir, test_part=0.25):
	files = [os.path.join(source_dir, f_name) for f_name in os.listdir(source_dir) if f_name.endswith('.jpg')]
	shuffle(files)
	split_point = int(test_part*len(files))
	train_files, test_files = files[split_point:], files[:split_point]
	move_files(train_files, train_dir)
	move_files(test_files, test_dir)


if __name__ == '__main__':
	split_data('images', 'data/train_images', 'data/eval_images')