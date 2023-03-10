from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, ValidationError
from typing import Literal
import joblib
import pandas as pd
import datetime as dt
import os
import numpy as np
from fastapi import HTTPException

class ModelInput(PydanticBaseModel):
    '''
    Clase que define las entradas del modelo
    '''
        
    IDENTIFICACION: int = Field(description = 'Identificacion de la persona', ge = 10 , le= 1000000000)    
    TIMECREATED: int = Field(description = 'Altura de la persona', ge = 10 , le= 10000000000)
    HOUR: int = Field(description = "Hora de acceso promedio", ge=0 , le=23)
    ORIGIN: Literal["web","cli"]
    PROGRAMA: Literal['INGENIERIA AMBIENTAL', 'LICENCIATURA EN EDUCACION INFANTIL',
        'INGENIERIA MECANICA', 'QUIMICA', 'ADMINISTRACION EN SALUD','ACUICULTURA', 'DPTO DE INGENIERIA AMBIENTAL',
        'LIC EN LITERATURA Y LENGUA CASTELLANA', 'INGENIERIA DE ALIMENTOS','MEDICINA VETERINARIA Y ZOOTECNIA', 'INGENIERIA DE SISTEMAS',
        'DEPARTAMENTO DE INGENIERIA DE ALIMENTOS', 'MATEMATICAS','DEPARTAMENTO DE QUIMICA',
        'ADMINIS. EN FINANZAS Y NEGOCIOS INTERNAC','FISICA', 'GEOGRAFIA',
        'INGENIERIA INDUSTRIAL', 'DPTO CIENCIAS ADMINISTRATIVAS',
        'INGENIERIA AGRONOMICA', 'DEPARTAMENTO DE CIENCIAS PECUARIAS',
        'DEPARTAMENTO DE GEOGRAFIA Y MEDIO AMBIEN',
        'LIC EN LENGUAS EXTRAN CON ENFA EN INGLES',
        'DEPARTAMENTO DE IDIOMAS EXTRANJEROS',
        'DEPARTAMENTO DE INFORMATICA EDUCATIVA',
        'LICENCIATURA EN EDUCACION INFANTIL', 'ENFERMERIA',
        'DPTO DE ING DE SISTEMAS Y TELECOMUNICACI', 'DERECHO',
        'LICENCIATURA EN INFORMATICA','TECNOLOGIA EN REGENCIA DE FARMACIA',
        'DEPARTAMENTO DE MATEMATICAS Y ESTADISTIC',
        'LIC. EDUCACION FISICA RECREACION Y DEPOR', 'ESTADISTICA',
        'LIC EN CIENCIAS NATURALES Y EDU AMBIENTA', 'BACTERIOLOGIA',
        'CINTIA', 'DEPARTAMENTO DE SALUD PUBLICA', 'BIOLOGIA',
        'DEPARTAMENTO DE BIOLOGIA', 'DIPLOMADO ETHICAL HACKING',
        'DEPARTAMENTO DE REGENCIA Y FARMACIA',
        'DEPARTAMENTO DE INGENIERIA MECANICA', 'LIC EN CIENCIAS SOCIALES',
        'LIC EN INFORMATICA', 'DEPARTAMENTO DE PSICOPEDAGOGIA',
        'BACTERIOLOGIA', 'LIC EN EDUC BASICA CON ENF HUM LENG CAST',
        'LIC EN EDUCACION ARTISTICA',
        'LICENCIATURA EN INFORMATICA Y MEDIOS AUD',
        'DPTO DE ING AGRONOMICA Y DESARROLL RURAL',
        'DPTO INGENIERIA INDUSTRIAL', 'ING SISTEMAS',
        'DEPARTAMENTO DE FISICA Y ELECTRONICA',
        'DEPARTAMENTO DE CIENCIAS JURIDICAS',
        'DEPARTAMENTO DE INGENIERIA INDUSTRIAL',
        'DEPARTAMENTO DE ENFERMERIA', 'DEPARTAMENTO DE BACTERIOLOGIA',
        'DPTO DE ING. AMBIENTAL', 'DPTO DE CIENCIAS NATURALES',
        'LIC EN EDUC BASICA CON ENF EN HUMAN INGL',
        'ADMINISTRACION EN FINANZAS Y NEGOCIOS INTERNACIONALES',
        'DPTO DE CULTURA FISICA, RECREAC Y DEPORT', 'ENFERMERIA',
        'DEPARTAMENTO DE ARTES', 'FUNCIONARIOS TEMPORALES',
        'DEPARTAMENTO DE CIENCIAS ACUICOLAS',
        'DEPARTAMENTO DE ESPA??OL Y LITERATURA', 'DPTO PSICOPEDAGOGIA',
        'REGENCIA DE FARMACIA', 'REGENCIA Y FARMACIA', 'QUIMICA',
        'DEPARTAMENTO DE MATEMATICAS Y ESTADISTICAS',
        'DEPARTAMENTO DE INFORMATICA',
        'DEPARTAMENTO DE MATEMATICAS Y ESTADIS',
        'DEPARTAMENTO DE CIENCIAS SOCIALES', 'CIENCIAS',
        'LICENCIATURA EN EDUCACI??N INFANTIL ', 'DPTO DE BIOLOGIA',
        'INGENIERIA AGRONOMICA', 'LIC. EN INFORMATICA ',
        'MEDICINA VETERINARIA', 'LIC. EN INFORMATICA',
        'LICENCIATURA EN INGLES',
        'DPTO DE ING DE SISTEMAS Y TELECOMUNICACIONES', 'ESTADI\xadSTICA',
        'LIC. EN INFORMATICA Y MEDIOS AUDIOVISUALES',
        'INGENIERIA AGRONOMICA', 'DPTO BACTEROLOG??A',
        'INGENIERIA AMBIENTAL',
        'ADMINIS. EN FINANZAS Y NEGOCIOS INTERNACIONALES',
        'ADMON FINANZAS Y NEGOCIOS INTERNACIONALES',
        'TEC PROF EN MANEJO Y CONSERV DE PROD AGR', 'ACUICULURA',
        'BIOLOGIA', 'DPTO DE CULTURA FISICA, RECREAC Y DEPORTES', 'FISICA',
        'LIC EN EDUC BASICA CON ENF EN CIEN SOCIA',
        'LIC EN CIENCIAS NATURALES Y EDU AMBIENTAL',
        'ADMINISTRACION EN SALUD',
        'OFICINA DE BIBLIOTECAS Y RECURSOS EDUCATIVOS',
        'IDIOMAS EXTRANJEROS CON ENFASIS EN INGLES', 'LIC. EN INFORMATICA',
        'PRUEBAS', 'INGENIERIA DE ALIMENTO', 'QUI\xadMICA',
        'INGENIERIA AGRONOMICA ', 'CIENCIAS ADMINISTRATIVAS',
        'DIVISION DE BIBLIOTECAS Y RECURSOS EDUCATIVOS BIBLIOTECA CENTRAL "MISAEL DIAZ URZOLA"',
        'QUIMICA ', 'DECANATURA/GESTOR DE CALIDAD',
        'DPTO MEDICINA VETERINARIA Y ZOOTECNIA',
        'DPTO INGENIERIA AMBIENTAL', 'GEOGRAFIA', 'INGENIERIA AGRONOMIA',
        'LIC. EDUCACION BASICA ENFASIS ARTISTICA', 'VETERINARIA',
        'ADMINISTRACION EN FINANZAS Y NEGOCIOS INTERNACIONALES ',
        'DIVISION DE POSTGRADOS Y EDUCACION CONTINUADA',
        'FUNCIONARIOS ADM. PLANTA', 'INGENIERIA AMBIENTAL ',
        'DEPARTAMENTO DE INGENIERIA AMBIENTAL',
        'DPTO DE GEOGRAFIA Y MEDIO AMBIENTE', 'ING AMBIENTAL']
    
    
    class Config:
        schema_extra = {
            "Example": {
                'IDENTIFICACION':50521243 ,
                'TIMECREATED': 1659331482,
                'HOUR':12,
                'ORIGIN': "web",
                'PROGRAMA':'ING AMBIENTAL'
            }
        }
class ModelOutput(PydanticBaseModel):
    '''
    Clase que define la salida del modelo
    '''
    
    DAY: Literal['LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO','DOMINGO']
    
    class Config:
        schema_extra = {
            "Example": {
                'DAY': 'MARTES'
            }
        }
        
class APIModelBackEnd():
    '''
    Esta clase maneja el back end de nuestro modelo de Machine Learning para la API en FastAPI
    '''
    
    def __init__(self,IDENTIFICACION,TIMECREATED,HOUR,ORIGIN,PROGRAMA):
        
        '''
        Este m??todo se usa al instanciar las clases

        Aqu??, hacemos que pida los mismos par??metros que tenemos en ModelInput.

        Para m??s informaci??n del __init__ method, pueden leer en l??nea en sitios c??mo 

        https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html

        '''
        
        
        self.IDENTIFICACION = IDENTIFICACION
        self.TIMECREATED = TIMECREATED
        self.HOUR = HOUR
        self.ORIGIN = ORIGIN
        self.PROGRAMA = PROGRAMA
        
    def _load_model(self, model_name:str = "ModelRF.pkl"):
            self.model = joblib.load(model_name)
        
    def _prepare_data(self):
            '''
            Clase de preparar lo datos.
            Este m??todo convierte las entradas en los datos que ten??an en X_train y X_test.

            Miren el orden de las columnas de los datos antes de su modelo.
            Tienen que recrear ese orden, en un dataframe de una fila.

            '''
            col=[
                "IDENTIFICACION",
                "TIMECREATED",
                "HOUR",
                'ORIGIN_cli',
                 'ORIGIN_web',
                 'PROGRAMA_ACUICULTURA',
                 'PROGRAMA_ACUICULURA',
                 'PROGRAMA_ADMINIS. EN FINANZAS Y NEGOCIOS INTERNAC',
                 'PROGRAMA_ADMINIS. EN FINANZAS Y NEGOCIOS INTERNACIONALES',
                 'PROGRAMA_ADMINISTRACION EN SALUD',
                 'PROGRAMA_ADMINISTRACI??N EN FINANZAS Y NEGOCIOS INTERNACIONALES',
                 'PROGRAMA_ADMINISTRACI??N EN FINANZAS Y NEGOCIOS INTERNACIONALES ',
                 'PROGRAMA_ADMINISTRACI??N EN SALUD',
                 'PROGRAMA_ADMON FINANZAS Y NEGOCIOS INTERNACIONALES',
                 'PROGRAMA_BACTERIOLOGIA',
                 'PROGRAMA_BACTERIOLOG??A',
                 'PROGRAMA_BIOLOGIA',
                 'PROGRAMA_BIOLOG??A',
                 'PROGRAMA_CIENCIAS',
                 'PROGRAMA_CIENCIAS ADMINISTRATIVAS',
                 'PROGRAMA_CINTIA',
                 'PROGRAMA_DECANATURA/GESTOR DE CALIDAD',
                 'PROGRAMA_DEPARTAMENTO DE ARTES',
                 'PROGRAMA_DEPARTAMENTO DE BACTERIOLOG??A',
                 'PROGRAMA_DEPARTAMENTO DE BIOLOG??A',
                 'PROGRAMA_DEPARTAMENTO DE CIENCIAS ACU??COLAS',
                 'PROGRAMA_DEPARTAMENTO DE CIENCIAS JUR??DICAS',
                 'PROGRAMA_DEPARTAMENTO DE CIENCIAS PECUAR??AS',
                 'PROGRAMA_DEPARTAMENTO DE CIENCIAS SOCIALES',
                 'PROGRAMA_DEPARTAMENTO DE ENFERMER??A',
                 'PROGRAMA_DEPARTAMENTO DE ESPA??OL Y LITERATURA',
                 'PROGRAMA_DEPARTAMENTO DE F??SICA Y ELECTR??NICA',
                 'PROGRAMA_DEPARTAMENTO DE GEOGRAF??A Y MEDIO AMBIEN',
                 'PROGRAMA_DEPARTAMENTO DE IDIOMAS EXTRANJEROS',
                 'PROGRAMA_DEPARTAMENTO DE INFORMATICA',
                 'PROGRAMA_DEPARTAMENTO DE INFORM??TICA EDUCATIVA',
                 'PROGRAMA_DEPARTAMENTO DE INGENIERIA AMBIENTAL',
                 'PROGRAMA_DEPARTAMENTO DE INGENIERIA DE ALIMENTOS',
                 'PROGRAMA_DEPARTAMENTO DE INGENIER??A INDUSTRIAL',
                 'PROGRAMA_DEPARTAMENTO DE INGENIER??A MEC??NICA',
                 'PROGRAMA_DEPARTAMENTO DE MATEMATICAS Y ESTADISTICAS',
                 'PROGRAMA_DEPARTAMENTO DE MATEM??TICAS Y ESTAD??S',
                 'PROGRAMA_DEPARTAMENTO DE MATEM??TICAS Y ESTAD??STIC',
                 'PROGRAMA_DEPARTAMENTO DE PSICOPEDAGOG??A',
                 'PROGRAMA_DEPARTAMENTO DE QU??MICA',
                 'PROGRAMA_DEPARTAMENTO DE REGENC??A Y FARMACIA',
                 'PROGRAMA_DEPARTAMENTO DE SALUD P??BLICA',
                 'PROGRAMA_DERECHO',
                 'PROGRAMA_DIPLOMADO ETHICAL HACKING',
                 'PROGRAMA_DIVISION DE BIBLIOTECAS Y RECURSOS EDUCATIVOS BIBLIOTECA CENTRAL "MISAEL DIAZ URZOLA"',
                 'PROGRAMA_DIVISION DE POSTGRADOS Y EDUCACION CONTINUADA',
                 'PROGRAMA_DPTO BACTEROLOG??A',
                 'PROGRAMA_DPTO CIENCIAS ADMINISTRATIVAS',
                 'PROGRAMA_DPTO DE BIOLOG??A',
                 'PROGRAMA_DPTO DE CIENCIAS NATURALES',
                 'PROGRAMA_DPTO DE CULTURA F??SICA, RECREAC Y DEPORT',
                 'PROGRAMA_DPTO DE CULTURA F??SICA, RECREAC Y DEPORTES',
                 'PROGRAMA_DPTO DE GEOGRAFIA Y MEDIO AMBIENTE',
                 'PROGRAMA_DPTO DE ING AGRON??MICA Y DESARROLL RURAL',
                 'PROGRAMA_DPTO DE ING DE SISTEMAS Y TELECOMUNICACI',
                 'PROGRAMA_DPTO DE ING DE SISTEMAS Y TELECOMUNICACIONES',
                 'PROGRAMA_DPTO DE ING. AMBIENTAL',
                 'PROGRAMA_DPTO DE INGENIER??A AMBIENTAL',
                 'PROGRAMA_DPTO INGENIER??A AMBIENTAL',
                 'PROGRAMA_DPTO INGENIER??A INDUSTRIAL',
                 'PROGRAMA_DPTO MEDICINA VETERINARIA Y ZOOTECNIA',
                 'PROGRAMA_DPTO PSICOPEDAGOG??A',
                 'PROGRAMA_ENFERMERIA',
                 'PROGRAMA_ENFERMER??A',
                 'PROGRAMA_ESTAD??STICA',
                 'PROGRAMA_ESTAD??\xadSTICA',
                 'PROGRAMA_FISICA',
                 'PROGRAMA_FUNCIONARIOS ADM. PLANTA',
                 'PROGRAMA_FUNCIONARIOS TEMPORALES',
                 'PROGRAMA_F??SICA',
                 'PROGRAMA_GEOGRAFIA',
                 'PROGRAMA_GEOGRAF??A',
                 'PROGRAMA_IDIOMAS EXTRANJEROS CON ENFASIS EN INGLES',
                 'PROGRAMA_ING AMBIENTAL',
                 'PROGRAMA_ING SISTEMAS',
                 'PROGRAMA_INGENIERIA AGRONOMICA',
                 'PROGRAMA_INGENIERIA AMBIENTAL',
                 'PROGRAMA_INGENIERIA AMBIENTAL ',
                 'PROGRAMA_INGENIER??A AGRONOMIA',
                 'PROGRAMA_INGENIER??A AGRONOMICA',
                 'PROGRAMA_INGENIER??A AGRONOMICA ',
                 'PROGRAMA_INGENIER??A AGRON??MICA',
                 'PROGRAMA_INGENIER??A AMBIENTAL',
                 'PROGRAMA_INGENIER??A DE ALIMENTO',
                 'PROGRAMA_INGENIER??A DE ALIMENTOS',
                 'PROGRAMA_INGENIER??A DE SISTEMAS',
                 'PROGRAMA_INGENIER??A INDUSTRIAL',
                 'PROGRAMA_INGENIER??A MEC??NICA',
                 'PROGRAMA_LIC EN CIENCIAS NATURALES Y EDU AMBIENTA',
                 'PROGRAMA_LIC EN CIENCIAS NATURALES Y EDU AMBIENTAL',
                 'PROGRAMA_LIC EN CIENCIAS SOCIALES',
                 'PROGRAMA_LIC EN EDUC B??SICA CON ENF EN CIEN SOCIA',
                 'PROGRAMA_LIC EN EDUC B??SICA CON ENF EN HUMAN INGL',
                 'PROGRAMA_LIC EN EDUC B??SICA CON ENF HUM LENG CAST',
                 'PROGRAMA_LIC EN EDUCACION ARTISTICA',
                 'PROGRAMA_LIC EN INFORM??TICA',
                 'PROGRAMA_LIC EN LENGUAS EXTRAN CON ENFA EN INGLES',
                 'PROGRAMA_LIC EN LITERATURA Y LENGUA CASTELLANA',
                 'PROGRAMA_LIC. EDUCACI??N B??SICA ??NFASIS ART??STICA',
                 'PROGRAMA_LIC. EDUCACI??N F??SICA RECREACI??N Y DEPOR',
                 'PROGRAMA_LIC. EN INFORMATICA',
                 'PROGRAMA_LIC. EN INFORMATICA Y MEDIOS AUDIOVISUALES',
                 'PROGRAMA_LIC. EN INFORM??TICA',
                 'PROGRAMA_LIC. EN INFORM??TICA ',
                 'PROGRAMA_LICENCIATURA EN EDUCACION INFANTIL',
                 'PROGRAMA_LICENCIATURA EN EDUCACI??N INFANTIL',
                 'PROGRAMA_LICENCIATURA EN EDUCACI??N INFANTIL ',
                 'PROGRAMA_LICENCIATURA EN INFORMATICA',
                 'PROGRAMA_LICENCIATURA EN INFORM??TICA Y MEDIOS AUD',
                 'PROGRAMA_LICENCIATURA EN INGLES',
                 'PROGRAMA_MATEM??TICAS',
                 'PROGRAMA_MEDICINA VETERINARIA',
                 'PROGRAMA_MEDICINA VETERINARIA Y ZOOTECNIA',
                 'PROGRAMA_OFICINA DE BIBLIOTECAS Y RECURSOS EDUCATIVOS',
                 'PROGRAMA_PRUEBAS',
                 'PROGRAMA_QUIMICA',
                 'PROGRAMA_QUIMICA ',
                 'PROGRAMA_QU??MICA',
                 'PROGRAMA_QU??\xadMICA',
                 'PROGRAMA_REGENCIA DE FARMACIA',
                 'PROGRAMA_REGENCIA Y FARMACIA',
                 'PROGRAMA_TEC PROF EN MANEJO Y CONSERV DE PROD AGR',
                 'PROGRAMA_TECNOLOG??A EN REGENCIA DE FARMACIA',
                 'PROGRAMA_VETERINARIA']
            df2 = pd.DataFrame(columns=col,data=[[*[0]*len(col)]])
            df2['IDENTIFICACION'] = self.IDENTIFICACION
            df2['TIMECREATED'] = self.TIMECREATED
            df2['HOUR'] = self.HOUR

            columO = [x for x in df2.columns if "ORIGIN_" in x and str(self.ORIGIN) == x.split('_')[-1]]
            df2[columO] = 1
            columP = [x for x in df2.columns if "PROGRAMA_" in x and str(self.PROGRAMA) == x.split('_')[-1]]
            df2[columP] = 1
            return df2
    
    def predict(self, y_name: str = 'DAY'):
            '''
            Clase para predecir.
            Carga el modelo, prepara los datos y predice.

            prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0:y_name})

            '''

            self._load_model()
            X = self._prepare_data()
            prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0: y_name})
            return prediction.to_dict(orient='records')
