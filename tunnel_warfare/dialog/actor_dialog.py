from dialog import ActorBaseDialog


class JianJunDialog(ActorBaseDialog):
    def __init__(self, jian_jun, font):
        dialog_test_list = [" ;" +
                            "建军：;" +
                            "小朋友，这里很危险！;" +
                            "小铁：我是来学习数学的。",
                            " ;" +
                            "建军：奇变偶不变。;" +
                            "小铁: 符号看象限;",
                            " ;" +
                            "建军：小铁小同志;" +
                            "很高兴见到你;" +
                            "紧急告诉大家撤离。"]
        super(JianJunDialog, self).__init__(jian_jun, dialog_test_list, font)


class TieTouDialog(ActorBaseDialog):
    def __init__(self, tie_tou, font):
        dialog_test_list = [" ;" +
                            "铁头：;" +
                            "同志，这里很危险！;" +
                            "小铁：我是来学习数学的。",
                            " ;" +
                            "铁头：奇变偶不变。" +
                            "小铁：符号看象限。;",
                            " ;" +
                            "铁头：小铁小同志;很高兴见到你，;"
                            "发生什么事了吗？;" +
                            "小铁：建军同志要我转达;" +
                            "请通知大家尽快撤离，有危险。"]
        super(TieTouDialog, self).__init__(tie_tou, dialog_test_list, font)
