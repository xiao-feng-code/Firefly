import os
import webp
from PIL import Image

def main(dir_path):
    if not os.path.isdir(dir_path):
        print("The directory doesn't exist")
        return

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        
        # 检查图片后缀
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                with Image.open(file_path) as im:
                    # --- 修改处：删除了 resize 相关的代码 ---
                    # 直接定义输出路径
                    webp_path = os.path.splitext(file_path)[0] + '.webp'
                    
                    # 保存图片 (保持原尺寸)
                    webp.save_image(im, webp_path, quality=85)
                    
                    # 更新了打印信息，不再显示调整后的尺寸
                    print(f"{filename} -> {webp_path} (Converted)")
                    
            except Exception as e:
                print(f"Error happened when processing {filename}: {e}")

if __name__ == "__main__":
    dir_input = input("directory: ").strip('"\'')
    main(dir_input)