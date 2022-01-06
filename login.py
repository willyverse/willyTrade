import sys
from PyQt5.QtWidgets import QApplication
from eFriendPy.API import *

app = QApplication(sys.argv)

api = HighLevelAPI()

print("eFriend expert 연결 여부: {0}".format(api.IsConnected()))
Accounts = api.GetAllAccounts()

print("보유 계좌들: {0}".format(Accounts))