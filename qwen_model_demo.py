# coding: utf-8

from modelscope import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import time

# ****** qwen模型运行demo，以 Qwen-1_8B-Chat 为例 ****** #

# 可选的模型包括: "Qwen-1_8B-Chat'"，"Qwen/Qwen-7B-Chat", "Qwen/Qwen-14B-Chat" 等
model_dir = 'Qwen/Qwen-1_8B-Chat' # 如果当前路径的模型不存在,会自动下载
# model_dir = './model2/Qwen/Qwen-1_8B-Chat' # 如果当前路径的模型存在,会直接加载
# model_dir = './model2/Qwen/Qwen-7B-chat' # 如果当前路径的模型存在,会直接加载


# Note: The default behavior now has injection attack prevention off.
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)


# 打开bf16精度，A100、H100、RTX3060、RTX3070等显卡建议启用以节省显存
# model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", trust_remote_code=True, bf16=True).eval()
# 打开fp16精度，V100、P100、T4等显卡建议启用以节省显存
# model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", trust_remote_code=True, fp16=True).eval()
# 使用CPU进行推理，如果是7B及以上需要约32GB内存
model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="cpu", trust_remote_code=True).eval()
# 可指定不同的生成长度、top_p等相关超参 . But if you use transformers>=4.32.0, there is no need to do this.
# model = AutoModelForCausalLM.from_pretrained(model_dir device_map="auto", trust_remote_code=True).eval()


# infer demo
for i in range(10000000):
    time.sleep(0.1)
    print("************** i=" + str(i) + " *************")
    # 第一轮对话 1st dialogue turn
    response, history = model.chat(tokenizer, "你好", history=None)
    print(response)
    # 你好！很高兴为你提供帮助。

    # 第二轮对话 2nd dialogue turn
    response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
    print(response)
    # 这是一个关于一个年轻人奋斗创业最终取得成功的故事。
    # 故事的主人公叫李明，他来自一个普通的家庭，父母都是普通的工人。从小，李明就立下了一个目标：要成为一名成功的企业家。
    # 为了实现这个目标，李明勤奋学习，考上了大学。在大学期间，他积极参加各种创业比赛，获得了不少奖项。他还利用课余时间去实习，积累了宝贵的经验。
    # 毕业后，李明决定开始自己的创业之路。他开始寻找投资机会，但多次都被拒绝了。然而，他并没有放弃。他继续努力，不断改进自己的创业计划，并寻找新的投资机会。
    # 最终，李明成功地获得了一笔投资，开始了自己的创业之路。他成立了一家科技公司，专注于开发新型软件。在他的领导下，公司迅速发展起来，成为了一家成功的科技企业。
    # 李明的成功并不是偶然的。他勤奋、坚韧、勇于冒险，不断学习和改进自己。他的成功也证明了，只要努力奋斗，任何人都有可能取得成功。

    # 第三轮对话 3rd dialogue turn
    response, history = model.chat(tokenizer, "给这个故事起一个标题", history=history)
    print(response)
    # 《奋斗创业：一个年轻人的成功之路》
