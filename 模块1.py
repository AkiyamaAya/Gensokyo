# coding:utf8
import pygame.constants
import sys

# ��ʼ��pygame
pygame.init()
# ��������
size = width, height = 600, 400
bg = (255, 255, 255)

# ����һ��ͼƬ����
img1 = pygame.image.load("123.jpg")
# ��ȡͼ���λ��
position = img1.get_rect()
# ����һ����Ϸ����
screen = pygame.display.set_mode(size)
# ��Ϸ����
pygame.display.set_caption("��Ϸtitle")
# ������Ҫ���ڴ��ڣ�����һ����ѭ��
while True:
    # �����¼������¼������˳�ʱ���������
    speed = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # ���̿���ͼƬ�˶� KEYDOWN �Ǽ��̰��µ��¼�
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed[1] -= 5
            if event.key == pygame.K_DOWN:
                speed[1] += 5
            if event.key == pygame.K_LEFT:
                speed[0] -= 5
            if event.key == pygame.K_RIGHT:
                speed[0] += 5
    # �ƶ�ͼ�񣬸����������ҵİ������ı�speed��Ȼ���ƶ�
    position = position.move(speed)
    # ��䱳��
    screen.fill(bg)
    # ����ͼƬ���ƶ����λ�ã����û���ƶ������ڳ�ʼλ�á�
    screen.blit(img1, position)
    # ���½���
    pygame.display.flip()
