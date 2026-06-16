# Luminance-Expanded-SpikeImg-Reconstruction
《极微光环境下 脉冲相机图象的精确重建》项目文件

#  目录
一、 dataset processing prog: 数据集处理程序

    (i) luminance_expansion_multi_thread.py
   
       
    (ii) spike_generator_multi_thread.py
   
        用数据集图片生成.dat脉冲流文件
   
    (iii) demo_luminance_expansion_multi_thread.py
   
        对路演demo用的原始图片进行光度扩充
   
    (iv) demo_spike_generator_multi_thread.py
   
       用路演demo图片生成.dat脉冲流文件
   
    (v) spike_reader.py
       可视化.dat脉冲流文件
       1. 功能
       可视化查看脉冲流文件
       2. 注意：
       (1) 一次只能看一个文件
       (2) 需要手动改文件名："# DAT 文件路径"下的DAT_PATH
       (3) "# 参数"下的HEIGHT、WIDTH、TIMESTEPS需要与脉冲流生成参数一致
