from dialog import ActorBaseDialog


class JianJunDialog(ActorBaseDialog):
    def __init__(self, jian_jun,font):
        dialog_test_list = ["建军：同志，这里很危险！！;快撤离此地",
                            "小铁：我是来这里找蘑菇的。",
                            "建军：天王盖地虎。", "小铁:小鸡炖蘑菇。",
                            "建军： 小铁小同志;很高兴见到你;" +
                            "通知人名群众,撤离村庄。"]
        super(JianJunDialog, self).__init__(jian_jun, dialog_test_list,font)


class TieTouDialog(ActorBaseDialog):
    def __init__(self, tie_tou,font):
        dialog_test_list = ["铁头：同志，这里很危险！！;快撤离此地？",
                            "小铁：我是来这里找蘑菇的。",
                            "铁头：天王盖地虎。",
                            "小铁：小鸡炖蘑菇。。",
                            "铁头：小铁小同志;很高兴见到你，发生什么事了吗",
                            "小铁：建军同志要我转达;请通知大家尽快撤离，有危险。"]
        super(TieTouDialog, self).__init__(tie_tou, dialog_test_list,font)