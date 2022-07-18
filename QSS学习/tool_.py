class QSSTool:
    @staticmethod
    def setQssToObj(file_pass, obj):
        with open(file_pass, "r", encoding="utf-8") as f:
            content = f.read()
            obj.setStyleSheet(content)