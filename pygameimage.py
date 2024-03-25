import pygame
import sys

pygame.init()

# 设置窗口大小和标题
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pygame Text Example')

# 定义文本内容和字体
text_content = "Hello, Pygame!"
font = pygame.font.SysFont(None, 36)  # 使用系统默认字体和字号，也可以指定字体文件路径和字号

# 渲染文本
text_surface = font.render(text_content, True, (255, 255, 255))  # 文本颜色为白色

# 文本位置
text_rect = text_surface.get_rect()
text_rect.center = (window_width // 2, window_height // 2)  # 将文本放置在窗口中心

# 主循环
while True:
    window.fill((0, 0, 0))  # 清空窗口，填充黑色背景
    window.blit(text_surface, text_rect)  # 将文本渲染到窗口
    pygame.display.update()  # 更新显示

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen = pygame.display.set_mode((800, 600))
pygame.display.flip()

# 截取整个屏幕并保存为文件
pygame.image.save(screen, 'screenshot_pygame.png')
