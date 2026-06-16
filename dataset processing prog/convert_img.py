import numpy as np


def img_to_spike(img, gain_amp=0.5, v_th=1.0, n_timestep=100):
    '''
    脉冲模拟器：图片转脉冲

    :param img: 图片 numpy.ndarray size：h x w
    :param gain_amp: 增益系数
    :param v_th: 阈值
    :param n_timestep: 时间步
    :return: 脉冲数据 numpy.ndarray
    '''

    h, w = img.shape
    if img.max() > 1:
        img = img / 255.
    assert img.max() <= 1.0 and img.min() >= 0.0

    # mem = np.zeros_like(img)
    # spks = np.zeros((n_timestep, h, w))
    
    # float32 更省内存 
    mem = np.zeros_like(
        img, 
        dtype=np.float32 
    ) 
    # uint8 节省巨大内存 
    spks = np.zeros(
        (n_timestep, h, w), 
        dtype=np.uint8 
    )
    
    for t in range(n_timestep):
        mem += img * gain_amp
        spk = (mem >= v_th)
        mem = mem * (1 - spk)
        spks[t, :, :] = spk
    return spks#.astype(np.float32)

'''
2026.6.6 Sat by:Shadowindows_017
这里为了方便多线程加速，对原本的代码做了修改：

将
mem = np.zeros_like(img)
spks = np.zeros((n_timestep, h, w))
改为
# float32 更省内存 
mem = np.zeros_like(
    img, 
    dtype=np.float32 
) 
# uint8 节省巨大内存 
spks = np.zeros(
    (n_timestep, h, w), 
    dtype=np.uint8 
)

以及将
return spks.astype(np.float32)
的后面注释掉。

完成任务后改回即可。
'''
