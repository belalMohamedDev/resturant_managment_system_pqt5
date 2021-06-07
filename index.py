from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtCore import QCoreApplication





  
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

        self.pushButton4.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton3.clicked.connect(lambda: self.clear_())
        self.pushButton.clicked.connect(lambda: self.total_())
        self.pushButton2.clicked.connect(lambda: self.text_())



        

    

   
    def clear_(self):
        self.lineEdit0.clear()
        self.lineEdit1.clear()
        self.lineEdit2.clear()
        self.lineEdit3.clear()
        self.lineEdit4.clear()
        self.lineEdit5.clear()
        self.lineEdit6.clear()
        self.lineEdit7.clear()
        self.lineEdit8.clear()
        self.lineEdit9.clear()
        self.lineEdit10.clear()
        self.lineEdit11.clear()
        self.lineEdit12.clear()
        self.lineEdit13.clear()
        self.lineEdit14.clear()
        self.lineEdit15.clear()
        self.textEdit.clear()


    def input_data(self):
        self.Filet_O_Fish=int(self.lineEdit0.text())
        self.Chicken_Burger=int(self.lineEdit1.text())
        self.Chicken_Legend=int(self.lineEdit2.text())
        self.Chicken_Burger_Meal=int(self.lineEdit3.text())
        self.Bacon_and_Cheese_Burger=int(self.lineEdit4.text())

        self.Milk_Shake=int(self.lineEdit5.text())
        self.Vanilla_Cone=int(self.lineEdit6.text())
        self.Classic_Vanilla=int(self.lineEdit7.text())
        self.Vanilla_Milk_Shake=int(self.lineEdit8.text())
        self.Chocolate_Milk_Shake =int(self.lineEdit9.text())
       

      



    def get_amount(self):
        self.total()

        self.meale =  self.pFilet_O_Fish +self.pChicken_Burger +self.pChicken_Legend +self.pChicken_Burger_Meal+self.pBacon_and_Cheese_Burger
        self.drinks=self.pMilk_Shake+self.pVanilla_Cone +self.pClassic_Vanilla+self.pVanilla_Milk_Shake+self.pChocolate_Milk_Shake 
        self.totalfwd=self.meale+self.drinks
        self.alltotalofwd=self.totalfwd
        return self.alltotalofwd



    def total(self):
        self.input_data()
        self.pFilet_O_Fish= self.Filet_O_Fish*2.5
        self.pChicken_Burger=self.Chicken_Burger*2.7
        self.pChicken_Legend= self.Chicken_Legend*2.9
        self.pChicken_Burger_Meal=self.Chicken_Burger_Meal*15
        self.pBacon_and_Cheese_Burger= self.Bacon_and_Cheese_Burger*7

        self.pMilk_Shake=self.Milk_Shake*20
        self.pVanilla_Cone=self.Vanilla_Cone*4
        self.pClassic_Vanilla=self.Classic_Vanilla*6
        self.pVanilla_Milk_Shake=self.Vanilla_Milk_Shake*7
        self.pChocolate_Milk_Shake=self.Chocolate_Milk_Shake*3


    def itax(self):
        camount=self.get_amount()
        self.tax=(camount-(camount*0.9))/100
        self.itotal=camount+self.tax



    def total_(self):
        self.get_amount()
        self.itax()
        self.lineEdit13.setText(str(self.tax))
        self.lineEdit15.setText(str(self.itotal))
        self.lineEdit14.setText(str(self.alltotalofwd))

        self.lineEdit12.setText(str(self.alltotalofwd))
        self.lineEdit11.setText(str(self.drinks))
        self.lineEdit10.setText(str(self.meale))

    
    def text_(self):
        self.get_amount()
        self.itax()
        self.textEdit.setText(("   resturant manage system \n            tax{0} /n itotal{1} /n  alltotalofwd{2}").format(self.tax,self.itotal,self.alltotalofwd))
       








   







app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

 

