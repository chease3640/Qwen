
# coding: utf-8

# ****** 使用代码方式，利用modelscope下载qwen模型 ****** #

# 1）默认模型会下载到~/.cache/modelscope/hub目录下， 如果需要指定目标，可以设置cache_dir参数
# 2）revision为可选参数，不指定版本会取模型默认版本，默认版本，默认版本为ModelScope library发布前最后一个版本
from modelscope.hub.snapshot_download import snapshot_download
# model_dir = snapshot_download('Qwen/Qwen-7b-chat', 'v1.0.0')
# model_dir = snapshot_download(model_id='Qwen/Qwen-7b-chat', revision='v1.0.0', cache_dir="./model") # ok
# model_dir = snapshot_download(model_id='Qwen/Qwen-7B-chat', cache_dir="./model2") # ok
model_dir = snapshot_download('Qwen/Qwen-1_8B-Chat', cache_dir="./model2") # ok


# 参考 https://juejin.cn/post/7329772404644642835

