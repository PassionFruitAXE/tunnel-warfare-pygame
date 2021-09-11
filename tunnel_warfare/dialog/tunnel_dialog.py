from dialog import SysBaseDialog


class TunnelTask1BeginDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("我叫小铁是一名红军小战士，;" +
                         "日本人来我们村子里扫荡了，;" +
                         "战士们都在地道之中走不开, ;" +
                         "我一定要帮战士们完成任务")

        text_list.append("红军：;" +
                         "小铁，我们没有地雷了;" +
                         "请帮我们找到5种地雷原材料;" +
                         "我们还有一个隐蔽的据点。;" +
                         "小心别被日本人抓到了。;")

        text_list.append("小铁：;" +
                         "我一定不负使命，;" +
                         "保障完成组织交代的任务。")
        super(TunnelTask1BeginDialog, self).__init__(text_list, font)


class TunnelTask1EndDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：;"+
                         "谢谢你，小铁同志，;" +
                         "我们离革命成功又近了一步，;" +
                         "你已经收集好材料了吧，;" +
                         "接下来就可以制作地雷了。 ")

        super(TunnelTask1EndDialog, self).__init__(text_list, font)


class TunnelTask2BeginDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：;"+
                         "小铁，;" +
                         "组织需要你上到地面去埋地雷了喔。;" +
                         "请消灭5个敌人")

        text_list.append("小铁：;" +
                         "保障完成组织交代的任务。")
        super(TunnelTask2BeginDialog, self).__init__(text_list, font)


class TunnelTask2EndDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：恭喜你，小铁，;" +
                         "你做的很好，;" +
                         "并且你已经通过了第二关考核。 ")
        super(TunnelTask2EndDialog, self).__init__(text_list, font)


class TunnelTask3BeginDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：;" +
                         "小铁，你已经是个红军战士了，;" +
                         "你需要找到建军同志，;" +
                         "他潜伏在日军时得到的重要情报，;" +
                         "把情报带给铁头同志。")

        text_list.append("红军：;"
                         "接头暗号是;" +
                         "他说：奇变偶不变，;" +
                         "你答：符号看象限。;")

        text_list.append("小铁：一定将消息带到！")
        super(TunnelTask3BeginDialog, self).__init__(text_list, font)


class TunnelTask3EndDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：小铁，你已经是个成熟的红军战士，;" +
                         "有你这样的中华儿女们加入;" +
                         "我们会迎来最终的胜利的！ ")
        super(TunnelTask3EndDialog, self).__init__(text_list, font)


class TunnelTaskFailDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：小铁同志，闯关失败;" +
                         "继续努力!")

        super(TunnelTaskFailDialog, self).__init__(text_list, font)
