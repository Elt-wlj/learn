from PIL import Image
import os
root_path = os.path.dirname(os.path.abspath(__file__))
old_img_path = os.path.join(root_path,'old_img')
new_img_path = os.path.join(root_path,'new_img')
img_dir = os.listdir(old_img_path)
print(img_dir)

for i in img_dir[0::]:
    # print('11111',i)
    im = Image.open(old_img_path+'/'+i)
    w, h = im.size
    print('original size : {}'.format(w, h))
    im.thumbnail((w//2,h//2))
    print('resize size : {}'.format(w,h))
    im.save(new_img_path+'/'+i,'jpeg')

