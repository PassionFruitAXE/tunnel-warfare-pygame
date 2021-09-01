from dialog import SysBaseDialog


class TunnelTask1BeginDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("小铁：大家好，我是小铁，;" +
                         "我是红军小战士，;" +
                         "我会在在磨练中成长的;" +
                         "我已经时刻准备接收挑战了")

        text_list.append("红军：小铁，你准备好了吗？;" +
                         "我们需要你帮忙找到;" +
                         "一些制作地雷的原材料。;" +
                         "我们需要5种原材料喔。")

        text_list.append("小铁：时刻准备着，;" +
                         "保障完成组织交代的任务。")
        super(TunnelTask1BeginDialog, self).__init__(text_list, font)


class TunnelTask1EndDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：恭喜你，小铁同志，;" +
                         "你已经通过了第一关考核，;" +
                         "你已经收集好材料，;" +
                         "可以制作地雷。 ")

        super(TunnelTask1EndDialog, self).__init__(text_list, font)


class TunnelTask2BeginDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：小铁，;" +
                         "组织需要你上到地面去埋地雷了喔。;" +
                         "需要炸死2个日本鬼子喔。")

        text_list.append("小铁：我已经迫不及待了，;" +
                         "保障完成组织交代的任务。")
        super(TunnelTask2BeginDialog, self).__init__(text_list, font)


class TunnelTask2EndDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：恭喜你，小铁，;" +
                         "你非常勇敢，;" +
                         "并且你已经通过了第二关考核。 ")
        super(TunnelTask2EndDialog, self).__init__(text_list, font)


class TunnelTask3BeginDialog(SysBaseDialog):
    def __init__(self, font):
        text_list = []
        text_list.append("红军：小铁，你已经是个合格的小战士，;" +
                         "你需要找到一名叫建军的同志，;" +
                         "得到日军消息，并带给一个叫铁头的同志。")

        text_list.append("红军：接头暗号是，;" +
                         "他说：天王盖地虎，;" +
                         "你答：小鸡炖蘑菇。;")

        text_list.append("小铁：保证完成任务")
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
                         "继续努力!" )

        super(TunnelTaskFailDialog, self).__init__(text_list, font)