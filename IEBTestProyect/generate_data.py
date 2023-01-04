
import os
import time
import django

from tqdm import tqdm

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IEBTestProyect.settings')
django.setup()

from Interface.models import Wireline, Proyect, UserIEB

def UserIEBCreateDatabase():
    """Creates UserIEB Database with the information from the Technical-Test
    """
    
    ListUsername = ["ieb","juan.cobo","Esmeralda.gutierrez","Jake.grajales"]
    ListPassword = ["uUET2m19!mC&","Jun@","Es*45","Jak180"]
    ListFristName = ["Administrador","Juan","Esmeralda","Jake"]
    ListLastName = ["IEB","Cobos","Gutierrez","Grajales"]
    ListEmail = ["ieb@ieb.com","juncobos@gmail.com","Esmeraldita45@gmail.com","jgrajales@gmail.com"]
    
    DATAIEB = range(1,len(ListUsername))
    db = UserIEB._meta.verbose_name

    if UserIEB.objects.exists():
        print(f'{db} database currently has information! ¿do you want to delete it?')
        
        while True:
            try:
                Select = str(input("Select: [Y]Yes/[N]No -->"))
                if Select == "Y" or Select == "N":
                    break
            except:
                print("¡Invalid Value!")

        if Select != "Y":
            return
        
        UserIEB.objects.all().delete()
    
    UserIEB.objects.create_superuser(
            id =1,
            username = str(ListUsername[0]),
            password = str(ListPassword[0]),
            first_name = str(ListFristName[0]),
            last_name = str(ListLastName[0]),
            email = str(ListEmail[0])
        )
    
    print(f'Creating information for {db} --> Wait a moment!')
    for i in tqdm(DATAIEB, bar_format='{desc:<5.5}{percentage:3.0f}%|\033[32m{bar:10}\033[0m{r_bar}'):
        time.sleep(0.5)
        
        wUser = str(ListUsername[i])
        wPassword = str(ListPassword[i])
        wFirstName = str(ListFristName[i])
        wLastName = str(ListLastName[i])
        wEmail = str(ListEmail[i])

        UserIEB.objects.create_user(
            id = i+1,
            username = wUser,
            password = wPassword,
            first_name = wFirstName,
            last_name = wLastName,
            email = wEmail
        )


def ProyectCreateDatabase():
    """Creates Proyect Database with the information from the Technical-Test
    """
    
    ListUser = ["juan.cobo", "Jake.grajales"]
    ListNmproy = ["Cuestesitas1","Cuestesitas2"]
    ListTyproy = ["Conceptual","Ingeniería Detalle"]
    
    DATAIEB = range(1,len(ListUser)+1)
    db = Proyect._meta.verbose_name

    if Proyect.objects.exists():
        print(f'{db} database currently PROYECTO has information! do you want to delete it?')
        
        while True:
            try:
                Select = str(input("Select: [Y]Yes/[N]No -->"))
                if Select == "Y" or Select == "N":
                    break
            except:
                print("¡Invalid Value!")

        if Select != "Y":
            return
        
        Proyect.objects.all().delete()
    
    for cUser in ListUser:
        if not UserIEB.objects.filter(username=str(cUser)).exists():
            print(f'The user {cUser} does not exist, before authorizing the project it must be created')
            return

    print(f'Creating information for {db} --> Wait a moment!')   
    for i in tqdm(DATAIEB, bar_format='{desc:<5.5}{percentage:3.0f}%|\033[32m{bar:10}\033[0m{r_bar}'):
        time.sleep(0.5)
        
        user = UserIEB.objects.get(username=str(ListUser[i-1]))
        nmproy = str(ListNmproy[i-1])
        typroy = str(ListTyproy[i-1])

        Proyect.objects.create(
            id = i,
            user = user,
            nmproy = nmproy,
            typroy = typroy
        )

def WirelneCreateDatabase():
    """Creates Wirelne Database with the information from the Technical-Test
    """
    
    ListMaterials = ["Aluminio","Aluminio","Cobre","Cobre"]
    ListAmpacity = [2.5, 1.26, 2.5, 1.26]
    ListCurrent = [130, 20, 110, 13]
    ListThickness = [2, 1, 2, 1]
    ListDiameter = [5, 3, 5, 3]
    ListwCurrentNew = [50, 25, 50, 25]

    DATAIEB = range(1,len(ListMaterials)+1)
    db = Wireline._meta.verbose_name

    if Wireline.objects.exists():
        print(f'{db} database currently has information! do you want to delete it?')
        
        while True:
            try:
                Select = str(input("Select: [Y]Yes/[N]No -->"))
                if Select == "Y" or Select == "N":
                    break
            except:
                print("¡Invalid Value!")

        if Select != "Y":
            return
        
        Wireline.objects.all().delete()

    print(f'Creating information for {db} --> Wait a moment!')
    for i in tqdm(DATAIEB, bar_format='{desc:<5.5}{percentage:3.0f}%|\033[32m{bar:10}\033[0m{r_bar}'):
        time.sleep(0.5)
        
        wMaterial = str(ListMaterials[i-1])
        wAmpacity = float(ListAmpacity[i-1])
        wVoltageNew = float(ListCurrent[i-1])
        wThicknessNew = float(ListThickness[i-1])
        wDiameterNew = float(ListDiameter[i-1])
        wCurrentNew = float(ListwCurrentNew[i-1])

        Wireline.objects.create(
            cod_wireline = i,
            material = wMaterial,
            ampacity = wAmpacity,
            new_voltage = wVoltageNew,
            new_thickness = wThicknessNew,
            new_diameter = wDiameterNew,
            new_current = wCurrentNew
        )

def main():
    while True:
        try:
            Select = str(input("¿Create a generic DB?: [Y]Yes/[N]No -->"))
            if Select == "Y" or Select == "N":
                break
        except:
            print("¡Invalid Value!")

    if Select != "Y":
        return
    
    UserIEBCreateDatabase()
    ProyectCreateDatabase()
    WirelneCreateDatabase()

if __name__ == '__main__':
    main()

