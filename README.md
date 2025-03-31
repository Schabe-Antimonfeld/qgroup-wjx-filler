# Q群问卷星助手
一个可以自动填写qq群中问卷星问卷的python脚本

目前支持单选与单项填空，并且需要对问卷的结构有预先了解

目前作者也不知道这个脚本会有什么用(?)，但是如果你有需要的话，可以尝试使用这个脚本

## 功能
这个脚本可以自动填写qq群中的问卷星问卷，目前支持的形式有：
- [x] 问卷星链接
- [x] 问卷星二维码
- [x] 以上两者与文字的组合
## 使用方法
1. 配置虚拟环境
    ```shell
    conda create -n qwf_venv python=3.13
    ```
2. 安装依赖
    ```shell
    pip install -r requirements.txt
    ```
3. 配置config
    ```yaml
    qqid: "1145141919810" # 你的QQ号
    group_id: [1145141919810] # 你要监听的群号
    ws_uri: ws://localhost:3001 #一般不用修改
    token: "napcat" #一般不用修改
    ```
4. 配置问卷样式与答案
    ```yaml
    q1:
      num: 1
      type: monoBlank #monoBlank, monoChoice
      ans: [细男] #可以有多个答案，开启随机只会随机选择一个填，否则选第一个
      random: None  #None, randint, uniform(虽然还没有实现)
    q2:
      num: 2
      type: monoChoice
      ans: [1]  #1：A，2：B，3：C，4：D以此类推，可以有多个答案，开启随机只会随机选择一个填，否则选第一个
      random: None
    q3:
      num: 3
      type: monoBlank
      ans: [下北泽书院]
      random: None
    q4:
      num: 4
      type: monoBlank
      ans: [1145141919810]
      random: None
    q5:
      num: 5
      type: monoBlank
      ans: [1898989889]
      random: None
    q6:
      num: 6
      type: monoChoice
      ans: [1]
      random: None
   ```
5. 运行
    ```shell
    python main.py
    ```
    第一次运行时会要求安装NapCat，按照提示安装即可
    
    之后会要求扫码登录qq，扫码后即可运行
