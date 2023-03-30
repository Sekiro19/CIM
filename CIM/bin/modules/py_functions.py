from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import *
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.dates
plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['savefig.dpi'] = 500
import seaborn as sns
sns.set();

DRIVER = "ODBC Driver 17 for SQL Server"
DATABASE = 'DDA'

MONTH_NAMES = {1: "Janv.", 2: "Févr.", 3: "Mars", 4: "Avr.", 5: "Mai", 6: "Juin",
               7: "Juil.", 8: "Août", 9: "Sept.", 10: "Oct.", 11: "Nov.", 12: "Déc."}
WEEKDAY_NAMES = {0: "Lun", 1: "Mar", 2: "Mer", 3: "Jeu", 4: "Ven", 5: "Sam", 6: "Dim"}

class Functions:
    def __init__(self) -> None:
        self.connString = ''
        self.db = QSqlDatabase.addDatabase("QODBC")
        self.signals = msgSignals()
        
        self.data = {'Commande': None, 'Livraison': None, 'Facture': None} # dataFrames

        self.plots = {
            'Commande': ['Total commandes', 'Total commandes par client'], 
            'Livraison': ['Quantité totale vendue par produit'], 
            'Facture': ['Montant total dépensé par client', 
                        'Revenu total généré par chaque produit', 
                        'Revenu total généré par chaque mode de paiement',
                        'Tendance des ventes', 'Saisonnalité des ventes']
                      }
    
    def setConnectionString(self, server: str, user: str, password: str):
        self.connString = f"Driver={DRIVER};Server={server};Database={DATABASE};UID={user};PWD={password};"
        self.db.setDatabaseName(self.connString)
        return self.db.open()
        
    def getConnectionString(self):
        return self.connString

    def _checkConnection(func):
        def wrapper(self, *args, **kwargs):
            if self.db.isOpen():
                return func(self, *args, **kwargs)
            else:
                if self.db.open():
                    return func(self, *args, **kwargs)
                else:
                    self.signals.error.emit('Pas de connexion aux serveur\n\nvérifier votre chaîne de connexion.')
        return wrapper
    
    @_checkConnection
    def execProcedure(self, procedureName: str, values: list) -> str:
        query = f"EXEC {procedureName} {('?,' * len(values)).strip(',')}"
        queryObj = QSqlQuery(self.db)
        queryObj.prepare(query)
        # print(query, values)
        for val in values:
            queryObj.addBindValue(val)
        
        if queryObj.exec():
            while queryObj.next():
                return queryObj.value(0)
        else:
            if queryObj.lastError().isValid():
                print('Error {Functions: execProcedure}:', queryObj.lastError().text())
                return queryObj.lastError().text()

    @_checkConnection
    def loadQuery(self, query: str) -> QSortFilterProxyModel:
        model = QSqlQueryModel()
        model.setQuery(query)
        if model.lastError().isValid():
            self.signals.error.emit(model.lastError().text())
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(model)
        return proxyModel
    
    @_checkConnection
    def select(self, query: str) -> QSqlQuery:
        queryObj = QSqlQuery(self.db)
        queryObj.prepare(query)
        if queryObj.exec():
            return queryObj
        else:
            if queryObj.lastError().isValid():
                print('Error {Functions: select}:', queryObj.lastError().text())
                self.signals.error.emit(queryObj.lastError().text())

    def queryToDf(self, query: str, dtypes: list, indexCol: str) -> pd.DataFrame:
        queryObj = self.select(query)
        if not queryObj:
            return
        record = queryObj.record()
        column_names = [record.fieldName(i) for i in range(record.count())]
        data = list()
        while queryObj.next():
            row = [queryObj.value(i) for i in range(record.count())]
            data.append(row)
        
        df = pd.DataFrame(data, columns=column_names)
        for i in range(len(column_names)):
            df[column_names[i]] = df.iloc[:, i].astype(dtypes[i])
        
        return df.set_index(indexCol)
    
    def setDataFrame(self, d1: str, d2: str):
        self.data['Commande'] = self.queryToDf(f"SELECT * FROM AllCommande WHERE DateCommande BETWEEN '{d1}' AND '{d2}'", 
                                               ['datetime64', 'str', 'str', 'str', 'int', 'float', 'str'], 
                                               'DateCommande')
        self.data['Livraison'] = self.queryToDf(f"SELECT * FROM AllLivraison WHERE DateLivraison BETWEEN '{d1}' AND '{d2}'", 
                                        ['datetime64', 'str', 'str', 'str', 'str', 'int', 'int', 'int', 'str'], 
                                        'DateLivraison')
        self.data['Facture'] = self.queryToDf(f"SELECT * FROM AllFacture WHERE DateFacture BETWEEN '{d1}' AND '{d2}'", 
                                ['datetime64', 'str', 'str', 'str', 'str', 'int', 'float', 'str', 'str'], 
                                'DateFacture')
        return all(value is not None for value in self.data.values())
    
    def countGrp(self, plotName: str, datePartition: str, extraArg: list=None, func: str='mean'):
        tableName = next((table for table, plotLst in self.plots.items() for plot in plotLst if plot == plotName), None)
        df = self.data.get(tableName)
        if df is not None:
            if plotName == 'Total commandes':
                dateIndex, names = self.mapDateIndex(df, datePartition)
                grp = df.groupby(dateIndex)['CodeCommande'].nunique().sort_index()
                if names:
                    grp.rename(index=names, inplace=True)
                title = f"Nombre total de commandes par {datePartition}."
                
            elif plotName == 'Total commandes par client':
                df = df[np.isin(df['CodeClient'], extraArg)]
                dateIndex, names = self.mapDateIndex(df, datePartition)
                grp = df.groupby([dateIndex, 'CodeClient'])['CodeCommande'].nunique().unstack(-1).sort_index()
                if names:
                    grp.rename(index=names, inplace=True)
                title = f"Nombre total de commandes par client ({','.join(grp.columns.to_numpy().astype(str))}) et par {datePartition}."

            elif plotName == 'Montant total dépensé par client':
                df = df[np.isin(df['CodeClient'], extraArg)]
                dateIndex, names = self.mapDateIndex(df, datePartition)
                grp = df.groupby([dateIndex, 'CodeClient'])['MontantHT'].agg(func).unstack(-1).sort_index()
                if names:
                    grp.rename(index=names, inplace=True)
                title = f"Montant total dépensé par client({','.join(grp.columns.to_numpy().astype(str))}) et par {datePartition}."
                
            elif plotName == 'Quantité totale vendue par produit':
                df = df[np.isin(df['CodeProduit'], extraArg)]
                dateIndex, names = self.mapDateIndex(df, datePartition)
                grp = df.groupby([dateIndex, 'CodeProduit'])['TotalQuantiteUniteRecue'].agg(func).unstack(-1).sort_index()
                if names:
                    grp.rename(index=names, inplace=True)
                title = f"Quantité totale vendue par produit({','.join(grp.columns.to_numpy().astype(str))}) et par {datePartition}."
                
            elif plotName == 'Revenu total généré par chaque produit':
                df = df[np.isin(df['CodeProduit'], extraArg)]
                dateIndex, names = self.mapDateIndex(df, datePartition)
                grp = df.groupby([dateIndex, 'CodeProduit'])['MontantHT'].agg(func).unstack(-1).sort_index()
                if names:
                    grp.rename(index=names, inplace=True)
                title = f"Revenu total généré par chaque produit({','.join(grp.columns.to_numpy().astype(str))}) et par {datePartition}."
            
            elif plotName == 'Revenu total généré par chaque mode de paiement':
                dateIndex, names = self.mapDateIndex(df, datePartition)
                grp = df.groupby([dateIndex, 'ModePaiement'])['MontantHT'].agg(func).unstack(-1).sort_index()
                if names:
                    grp.rename(index=names, inplace=True)
                title = f"Revenu total généré par chaque mode de paiement et par {datePartition}."
            else:
                return None, None

            return grp, title
        else:
            self.signals.info.emit("Aucune donnée disponible.\nVous devez charger les données en cliquant sur le bouton ci-dessus.")
            return None, None

    def ts(self, plotName: str):
        tableName = next((table for table, plotLst in self.plots.items() for plot in plotLst if plot == plotName), None)
        df = self.data.get(tableName)
        if df is not None:
            if plotName == 'Saisonnalité des ventes':
                series = df['MontantHT']
                series = series.groupby([series.index.year, series.index.month]).agg('sum').unstack().T.sort_index() # reset 
                series.rename(index=MONTH_NAMES, inplace=True)
                title = "Saisonnalité des ventes (MontantHT)."
                
            elif plotName == 'Tendance des ventes':
                series, title = df['MontantHT'], "Tendance des ventes (MontantHT)."
            else:
                return None, None
            
            return series, title
        else:
            self.signals.info.emit("Aucune donnée disponible.\nVous devez charger les données en cliquant sur le bouton ci-dessus.")
            return None, None
        
    @staticmethod
    def queryObjToJinja(queryObj: QSqlQuery, tableCols: list=[], listVar: list=[]):
        variables = {var: [] for var in listVar}
        table = list()
        record = queryObj.record()
        while queryObj.next():
            row = dict()
            for iCol in range(record.count()):
                value = queryObj.value(iCol)
                col = record.fieldName(iCol)
                if col in tableCols:
                    row[col] = value
                elif (col in listVar) and (value not in variables[col]):
                    variables[col].append(value)
                else:
                    if variables.get(col):
                        pass
                    else:
                        variables[col] = value
            if row:
                table.append(row)
                
        for col in listVar:
            variables[col] = ','.join(variables[col])
        
        return variables, table
    
    @staticmethod
    def mapDateIndex(df: pd.DataFrame, datePartition: str):
        if datePartition == "Année":
            return df.index.year, None
        elif datePartition == "Mois":
            return df.index.month, MONTH_NAMES
        elif datePartition == "Jour":
            return df.index.day, None
        elif datePartition == "Jour de la semaine":
            return df.index.dayofweek, WEEKDAY_NAMES


class msgSignals(QObject):
    error = Signal(str)
    info = Signal(str)

class Canvas(FigureCanvas):
    def __init__(self, parent=None, layout=None, width=6.4, height=4.8, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.fig.set_tight_layout(True)
        
        super().__init__(self.fig)
        self.setParent(parent)
        
        self.toolbar = NavigationToolbar(self, parent)
        
        if layout:
            layout.addWidget(self.toolbar)
            layout.addWidget(self)
            layout.setStretchFactor(self, 1)

                            
    def _setFigureCanvas(func):
        def wrapper(self, *args, **kwargs):
            self.clearFig()
            result = func(self, *args, **kwargs)
            self.draw()
            return result
        return wrapper
    
    
    def setCoorFloatFormat(self, axList: list=None):         
        axs = axList or self.fig.axes 
        for ax in axs:
            ax.format_coord = lambda x,y: f"x={x:.2f}, y={y:.2f}"

    
    def clearFig(self):
        self.fig.clf()
        self.fig.suptitle('')
    
    @_setFigureCanvas
    def countPlot(self, df: pd.DataFrame, kind: str='bar', title: str=''):
        if not df.empty:
            ax = self.fig.add_subplot(111)
            df.plot(kind=kind, title=title, ax=ax)
            self.setCoorFloatFormat()
            
    @_setFigureCanvas
    def seasonalPlot(self, seasons: pd.Series, yLabel: str, figTitle: str):
        axPlot = self.fig.add_subplot(211)
        axBox = self.fig.add_subplot(212)
        
        axPlot.plot(seasons)
        axPlot.set_ylabel(yLabel)
        axPlot.set_xticks([])
        for line, col in zip(axPlot.lines, seasons.columns):
            xyData = seasons[col].dropna()
            y = xyData.iloc[-1]
            axPlot.annotate(col, 
                        xy=(1, y), 
                        xytext=(6, 0), 
                        color=line.get_color(), 
                        xycoords=axPlot.get_yaxis_transform(), 
                        textcoords='offset points', 
                        va='center')

        seasons.T.boxplot(ax=axBox)
        axBox.set_ylabel(yLabel)
        axBox.tick_params(axis='x', rotation=45)
        self.fig.suptitle(figTitle)
        self.setCoorFloatFormat()
        
    @_setFigureCanvas
    def trendPlot(self, series: pd.Series, figTitle: str):
        grid = plt.GridSpec(3, 3)
        
        axL = self.fig.add_subplot(grid[0:, :2])
        axR1 = self.fig.add_subplot(grid[0, 2])
        axR2 = self.fig.add_subplot(grid[1, 2])
        axR3 = self.fig.add_subplot(grid[2, 2])

        axR1.set_yticks([])
        axR2.set_yticks([])
        axR3.set_yticks([])
        axR2.tick_params(axis='x', rotation=90)
        
        axL.plot(series.resample('D').mean(), label='Jour', color='k', alpha=.3)
        axL.plot(series.resample('BM').mean(), label="Fin de mois", color='r')
        axL.plot(series.resample('BA').mean(), label="Fin de l'année", color='b')
        axL.legend()
        axR1.plot(series.groupby(series.index.year).mean().sort_index(), color='b')
        axR1.set_xlabel('année')
        grpM = series.groupby(series.index.month).mean().sort_index()
        grpM.rename(index=MONTH_NAMES, inplace=True)
        axR2.plot(grpM, color='r')
        axR2.set_xlabel('mois')
        axR3.plot(series.groupby(series.index.day).mean().sort_index(), color='k')
        axR3.set_xlabel('jour')
        self.fig.suptitle(figTitle)
        dateFmt = matplotlib.dates.DateFormatter('%Y-%m-%d')
        axL.format_coord = lambda x,y: f"x={dateFmt(x)}, y={y:.2f}"
        self.setCoorFloatFormat([axR1, axR2, axR3])


class StockColorPalette(QStyledItemDelegate):
    def __init__(self, derniereInventaireIndex, quantitePaletteIndex):
        super().__init__()
        self.derniereInventaireIndex = derniereInventaireIndex
        self.quantitePaletteIndex = quantitePaletteIndex
        
    def paint(self, painter, option, index):
        if index.column() == self.derniereInventaireIndex:
            data = index.data()
            painter.save()
            if 'False' in data:
                painter.fillRect(option.rect, QBrush(QColor(255, 44, 83)))
            elif 'True' in data:
                painter.fillRect(option.rect, QBrush(QColor(189, 255, 0)))
            painter.restore()
            option.backgroundBrush = QBrush(Qt.NoBrush)
        
        if index.column() == self.quantitePaletteIndex:
            data = index.data()
            painter.save()
            if data == 0:
                painter.fillRect(option.rect, QBrush(QColor(255, 44, 83)))
            elif 1 <= data <= 10:
                painter.fillRect(option.rect, QBrush(QColor(255, 164, 0)))
            elif data > 10:
                painter.fillRect(option.rect, QBrush(QColor(189, 255, 0)))

            painter.restore()
            option.backgroundBrush = QBrush(Qt.NoBrush)
            
        super().paint(painter, option, index)

class FactureColorPalette(QStyledItemDelegate):
    def __init__(self, EtatIndex):
        super().__init__()
        self.EtatIndex = EtatIndex
        
    def paint(self, painter, option, index):
        if index.column() == self.EtatIndex:
            data = index.data()
            painter.save()
            if data == 'Paye':
                painter.fillRect(option.rect, QBrush(QColor(189, 255, 0)))
            elif ': 0j' in data:
                painter.fillRect(option.rect, QBrush(QColor(255, 44, 83)))
            else:
                painter.fillRect(option.rect, QBrush(QColor(255, 164, 0)))
                
            painter.restore()
            option.backgroundBrush = QBrush(Qt.NoBrush)
            
        super().paint(painter, option, index)

class viewBtn(QPushButton):
    def __init__(self, style: str, toolTip: str):
        super().__init__()
        self.setMaximumSize(20, 20)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(style)
        self.setToolTip(toolTip)
        self.id = list()
