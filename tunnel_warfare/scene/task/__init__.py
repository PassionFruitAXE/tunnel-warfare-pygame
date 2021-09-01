import enum

class TaskStatus(enum.IntEnum):
    start_dialog = 0
    do_task= 1
    win_dialog = 2
    fail_dialog = 3
    win_over = 4
    fail_over = 5


class BaseTask:
    def __init__(self, start_dialog, win_dialog, fail_dialog):
        self.start_dialog = start_dialog
        self.win_dialog = win_dialog
        self.fail_dialog = fail_dialog
        self.task_status = TaskStatus.start_dialog


    def do_task(self, key_down, key_list):
        if key_down:
            if self.task_status == TaskStatus.start_dialog:
                self.start_dialog.next_text()
                if self.start_dialog.is_finish():
                    self.task_status = TaskStatus.do_task
            if self.task_status == TaskStatus.win_dialog:
                self.win_dialog.next_text()
                if self.win_dialog.is_finish():
                    self.task_status = TaskStatus.win_over
            if self.task_status == TaskStatus.fail_dialog:
                self.fail_dialog.next_text()
                if self.fail_dialog.is_finish():
                    self.task_status = TaskStatus.fail_over
        if self.task_status == TaskStatus.do_task:
            self.do_self_task(key_down, key_list)

    def do_self_task(self, key_down, key_list):
        """
        派生类会重写
        :param key_down:
        :param key_list:
        :return:
        """
        pass

    def get_status(self):
        return self.task_status

    def draw(self, surface, view_x, view_y):
        if self.task_status == TaskStatus.win_over or \
            self.task_status == TaskStatus.fail_over:
            return
        elif self.task_status == TaskStatus.start_dialog:
            self.start_dialog.draw(surface)
        elif self.task_status == TaskStatus.win_dialog:
            self.win_dialog.draw(surface)
        elif self.task_status == TaskStatus.fail_dialog:
            self.fail_dialog.draw(surface)

        self.draw_task(surface, view_x, view_y)

    def draw_task(self,surface, view_x, view_y):
        """
                派生类会重写
                :param key_down:
                :param key_list:
                :return:
                """
        pass