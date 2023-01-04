import random

from django.test import TestCase

from .models import Wireline
from .functions import Ampacity

class WirelineTestCase(TestCase): 
    """
    It generates a database with a wide diversity of combinations according to the iterations entered
    Modify the values according to the materials, diameters and thicknesses. ¡Before running the text!
    """
    while True:
        try:
            TestSteps = int(input("Iterations:"))
            break
        except:
            print("¡Invalid Value!")
    
    """The current value is taken by default between 0 and 1000"""
    ListCurrent = [random.randint(0,1000) for x in range(TestSteps)]
            
    def setUp(self):
        
        AllMaterials = ["Aluminio","Cobre","Niquel","Hierro","Bronce","Laton"]
        ListThickness = [1,2,4,5]
        ListDiameter = [1.0,1.5,2.0,2.5,3.0]
        ListwCurrentNew = [25,50]
        
        for i in range(self.TestSteps):
            wMaterial = str(random.choice(AllMaterials))
            wAmpacity = float(Ampacity(self.ListCurrent[i-1]))
            wVoltageNew = float(self.ListCurrent[i-1])
            wThicknessNew = float(random.choice(ListThickness))
            wDiameterNew = float(random.choice(ListDiameter))
            wCurrentNew = float(random.choice(ListwCurrentNew))

            Wireline.objects.create(
                cod_wireline = i,
                material = wMaterial,
                ampacity = wAmpacity,
                new_voltage = wVoltageNew,
                new_thickness = wThicknessNew,
                new_diameter = wDiameterNew,
                new_current = wCurrentNew
                )

    def test_wireline_is_correct_new_ampacity(self):
        """
        Verify that for all cases of currents entered and get the expected value of Ampacity.
        """
        for i in range(self.TestSteps):
            TestQuery = Wireline.objects.get(cod_wireline=i).ampacity
            self.assertEqual(Ampacity(self.ListCurrent[i-1]), TestQuery)
