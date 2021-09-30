from PIL import Image
import random

def construct(width, frequency, speed_start=2):
	Highway = [[-1]*width]
	for i in range(0, width, frequency):
		Highway[0][i] = speed_start

	return Highway

def distance(Highway, i, j):
	d = 0
	Voit = Highway[i][j+1:]
	for a in range(len(Voit)):
		if Voit[a] != -1:
			return d
		else:
			d += 1
	d += distance(Highway, i, -1)
	return d

def maj(Highway, i, p=0.2, speed_max=5):
	width = len(Highway[0])
	Vit_suiv = [-1]*width

	for j in range(width):
		if Highway[i][j] != -1:
			Vit_suiv[j] = min(Highway[i][j]+1, speed_max)
			dn = distance(Highway, i, j) -1
			Vit_suiv[j] = min(Vit_suiv[j], dn)
			if random.random() < p:
				Vit_suiv[j] = max(Vit_suiv[j] -1, 0)
	return Vit_suiv

def move(Highway, height, p=0.2, speed_max=5):
	width = len(Highway[0])
	for i in range(height):
		Vit_s = maj(Highway, i, p, speed_max)
		Highway.append([-1]*width)

		for j in range(width):
			add = Vit_s[j]
			if add != -1:
				Highway[i+1][(j+add)%width] = add
	return Highway

def color(Highway, name=''):
	width, height = len(Highway[0]), len(Highway)
	image = Image.new('RGB', (width, height), (255, 255, 255))
	color_speed = [(255, 0, 0), (255, 128, 0), (255, 128, 0), (255, 255, 0), (255, 255, 0), (0, 255, 0), (255, 255, 255)]

	for i in range(height):
		for j in range(width):
			pix = Highway[i][j]
			try:
				col = color_speed[pix]
			except IndexError:
				col = (0, 0, 0)
			finally:
				image.putpixel((j, i), col)
	if name == '':
		return image
	else:
		image.save(name + '.png')
		return 'Done'

p = 0.1; speed_start = 2
freq_voit = 5; speed_max = 5
width = 256; height = 512

if __name__ == '__main__':
	Highway = construct(width, freq_voit, speed_start)
	Highway = move(Highway, height, p, speed_max)
	color(Highway, 'result')
  
