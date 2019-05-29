#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目：
#   （平均速度）假设一个人在 45 分 30 秒内跑了 14 公里，
# 编写程序显示每小时的平均速度是多少英里。（1 英里是 1.6 公里）
#++++++++++++++++++++++++++++++++++++++++++++++++

class Exe_1_10():
    def __init__(self):
        pass

    def _convert_time(self, minutes, seconds):
        return (minutes * 60 + seconds) / (60 * 60)
    
    def _convert_mile(self, kilometers):
        return kilometers / 1.6

    def _get_mph(self, minutes, seconds, kilometers):
        time = self._convert_time(minutes, seconds)
        dist = self._convert_mile(kilometers)
        return dist / time
    
    def execute(self, minutes=45, seconds=30, kilometers=14):
        return self._get_mph(minutes, seconds, kilometers)

if __name__ == "__main__":
    e = Exe_1_10()
    print("mph is", e.execute())