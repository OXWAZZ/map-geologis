# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Mantab3
                                 A QGIS plugin
 Map Geologis
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-02-23
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Map Geologis
        email                : MapGeologis@ma.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from pathlib import Path
import re
from qgis.core import *
import qgis.utils


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .Map_Geologis_dialog import Mantab3Dialog
import os.path


class Mantab3:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Mantab3_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Map Geologis')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Mantab3', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        icon_path = ':/plugins/Map_Geologis/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Map Geologis 1'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Map Geologis'),
                action)
            self.iface.removeToolBarIcon(action)

    def daftarDaerah(self): #fungsi untuk mereturn nama kota dan kabupaten berdasarkan nama provinsi
        Sumatra = [
            "BANDA ACEH",
            "LHOKSEUMAWE",
            "CALANG",
            "TAKEGON",
            "LANGSA",
            "TAPAKTUAN",
            "MEDAN",
            "TEBING TINGGI",
            "SINABANG",
            "SIDIKALANG",
            "PEMATANG SIANTAR",
            "NIAS",
            "PADANG SIDEMPUAN & SIBOLGA",
            "DUMAI & BAGANSIAPIAPI",
            "BENGKALIS",
            "LUBUKSIKAPING",
            "PEKANBARU",
            "SIAKSRI INDRAPURA & TANJUNG PINANG",
            "TANJUNG PINANG",
            "TELO",
            "PADANG",
            "SOLOK",
            "RENGAT",
            "DABO",
            "SIBERUT",
            "PAINAN & TIMUR LAUT MUARA SIBERUT",
            "MUARABUNGO",
            "JAMBI",
            "BANGKA UTARA",
            "PAGAI & SIPORA",
            "SUNGAI PENUH & KETAUN",
            "SAROLANGUN",
            "PALEMBANG",
            "BANGKA SELATAN",
            "BELITUNG",
            "BENGKULU",
            "LAHAT",
            "TULUNG SELAPAN",
            "MANNA & ENGGANO",
            "BATURAJA",
            "MENGGALA",
            "KOTA AGUNG",
            "TANJUNG KARANG"
            ]
        
        Sulawesi = [
            "TALAUD",
            "SANGIHE SIAU",
            "MANADO",
            "KOTAMUBAGU",
            "TILAMUTA",
            "TOLI TOLI",
            "PALU TINJAU",
            "LUWUK",
            "PASANGKAYU",
            "POSO",
            "BATUI",
            "MAMUJU",
            "MALILI",
            "BUNGKU",
            "MAJENE PALOPO",
            "LASUSUA KENDARI",
            "PAMGKAJENE WATAMPONE",
            "KOLAKA",
            "UJUNG PANDANG",
            "BUTON",
            "TUKANGBESI",
            "BONERATE",
            ]

        Nusatenggara = [
            "BALI",
            "LOMBOK",
            "SUMBAWA",
            "KOMODO",
            "RUTENG",
            "ENDE",
            "LOMBLEN",
            "WETARBARAT",
            "WETARTIMUR",
            "DILI",
            "BAUCAU",
            "WAIKA BUPAK DAN BUPAK",
            "KUPANG",
            "ATAMBUA",
            ]
            
        Maluku = [
            "MOROTAI",
            "TERNATE",
            "BACAN",
            "BANGGAI",
            "SANANA",
            "OBI",
            "BURU",
            "AMBON",
            "MASOHI",
            "BULA WATUBELA",
            "KAI TAYANDU",
            "ARU",
            "MOA DAMAR",
            "BABAR",
            "TANIMBAR",
            ]

        Irianjaya = [
            "WAIGEO",
            "MAR",
            "MANOKRAWI",
            "BIAK",
            "SORONG",
            "TAMINABUAN",
            "RANSIKI",
            "YAPEN",
            "MISOOL",
            "FAK FAK",
            "STEEN KOL",
            "WARREN",
            "SAWAI",
            "DOOM",
            "SARMI BUFAREH",
            "JAYAPURA",
            "PULAU KARAS",
            "KAIMANA",
            "ENAROTALI",
            "BEOGA",
            "ROTANBURG",
            "TARITATU",
            "OMBA",
            "WAGHETE YAPEKORA",
            "TIMIKA",
            "WAMENA",
            "PEGUNUNGAN JAYAWIJAYA",
            "BIRUFU DAN YAPERO",
            "OKSIBIL",
            "SARABIH",
            "TANAH MERAH",
            "MAPI",
            "MUTING",
            "KOMOLOM",
            "MERAUKE",
            ]

        Kalimantan = [
            "LUMBIS",
            "APOBAYAN",
            "MALINAU",
            "TARAKAN DAN SEBATIK",
            "SAWAH",
            "LONGBIA",
            "TANJUNG REDEB",
            "SAMBAS SILUAS",
            "NANGAOBAT",
            "PEGUNUNGAN KAPUAS",
            "LONG NAWAN",
            "TANJUNG MANGKALIAT",
            "SINGKAWANG",
            "SANGGAU",
            "SINTANG",
            "PUTUSSIBAU",
            "LONG PAHANGAI",
            "SANGATTA",
            "PONTIANAK DAN NANGATAMAN",
            "NANGAPINOH",
            "TUMBANG HIRAM",
            "MUARA TEWE",
            "LONGIRAM",
            "SAMARINDA",
            "TUMBANG",
            "TEWAH",
            "BUNTOK",
            "BALIKPAPAN",
            "PANGKALAN",
            "PALANGKARYA",
            "SAMPANAHAN",
            "MUARADUA",
            "KUALA PEMBUANG",
            "KOTA BARU",
            "TEPIAN BALAI",
            "TAREMPA DAN JEMAJA RIAU",
            "BUTUN RANAI NATUNA",
            "KEPULAUAN NATUNA",
            "TAMBELAN RIAU",
            ]

        Jawa = [
            "ANYER",
            "CIKARANG",
            "SERANG",
            "LEUWIDAMAR",
            "JAKARTA DAN KEPULAUAN SERIBU",
            "BOGOR",
            "JAMPANG DAN BALEKAMBANG",
            "KARAWANG",
            "CIANJUR",
            "SINDANG BARANG DAN BANDAR WARU",
            "PAMANUKAN",
            "BANDUNG",
            "INDRAMAYU",
            "ARJAWINANGUN",
            "TASIKMALAYA",
            "KARANGNUNGG",
            "CIREBON",
            "MAJENANG",
            "PANGANDARAN",
            "PURWOKERTO",
            "BANYUMAS",
            "MAGELANG-SEMARANG",
            "YOGYAKARTA",
            "KUDUS",
            "SURAKARTA GIRITONTRO",
            "REMBANG",
            "PONOROGO",
            "PACITAN",
            "JATIROGO",
            "BOJONEGORO",
            "MADIUN",
            "TULUNGAGUNG",
            "TUBAN",
            "MOJOKERTO",
            "KEDIRI",
            "BLITAR",
            "SURABAYA",
            "MALANG",
            "TUREN",
            "TANJUNG BUMI DAN PAMEKASAN",
            "PROBOLONGGO",
            "LUMAJANG",
            "WARU DAN SUMENEP",
            "BESUKI",
            "JEMBER",
            "SITUBONDO",
            "BANYUWANGI",
            "BLAMBANGAN",
            "KARIMUNJAWA",
            "BAWEAN DAN MASALEMBO",
            "KANGEAN DAN SAPUTI",
            "BANJARNEGARA PEKALONGAN",
            "GARUT PAMEUNGPEUK",
            "KEBUMEN",
            "NGAWI",
            "SALATIGA",
            "UJUNGKULON",
            ]
        return Sumatra, Sulawesi, Nusatenggara, Maluku, Irianjaya, Kalimantan, Jawa

    def returnKotaKab(self): #funsi untuk mengganti kolom kota dan kabupaten jika provinsi diganti
        provinsi = self.dlg.comboBox.currentText()
        Sumatra, Sulawesi, Nusatenggara, Maluku, Irianjaya, Kalimantan, Jawa = self.daftarDaerah()

        if provinsi == "-pilih provinsi-": #merubah nilai kota/kabupaten
            self.dlg.comboBox_2.clear()
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])
        if provinsi == "SUMATRA": #merubah nilai kota/kabupaten
            self.dlg.comboBox_2.clear()
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])
            self.dlg.comboBox_2.addItems(Sumatra)
        if provinsi == "SULAWESI": #merubah nilai kota/kabupaten
            self.dlg.comboBox_2.clear()
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])
            self.dlg.comboBox_2.addItems(Sulawesi)
        if provinsi == "NUSATENGGARA": #merubah nilai kota/kabupaten
            self.dlg.comboBox_2.clear()
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])
            self.dlg.comboBox_2.addItems(Nusatenggara)
        if provinsi == "MALUKU": #merubah nilai kota/kabupaten
            self.dlg.comboBox_2.clear()
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])
            self.dlg.comboBox_2.addItems(Maluku)
        if provinsi == "IRIANJAYA": #merubah nilai kota/kabupaten
            self.dlg.comboBox_2.clear()
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])
            self.dlg.comboBox_2.addItems(Irianjaya)
        if provinsi == "KALIMANTAN": #merubah nilai kota/kabupaten
            self.dlg.comboBox_2.clear()
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])
            self.dlg.comboBox_2.addItems(Kalimantan)
        if provinsi == "JAWA": #merubah nilai kota/kabupaten
            self.dlg.comboBox_2.clear()
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])
            self.dlg.comboBox_2.addItems(Jawa)

    def tabSelect(self): #fungsi untuk tab select
        if self.dlg.comboBox.currentText() == "-pilih provinsi-": #pesan error ketika nilai provinsi belom diganti
            msg = QMessageBox()
            msg.setText("pilih provinsi terlebih dahulu")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        elif self.dlg.comboBox_2.currentText() == "-pilih kota/kabupaten-": #pesan error muncul ketika kota/kabupaten belom diganti
            msg = QMessageBox()
            msg.setText("pilih kota/kabupaten terlebih dahulu")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        else: #jika nilai provinsi dan kota/kabupaten sudah diganti maka akan melanjutkan dengan mengkonekkan ke database postgis
            #konek database postgis
            self.mantab = self.dlg.comboBox_2.currentText().replace(" ", "_").lower()
            connString = "PG: dbname=sdb_course host=localhost user=postgres password=793179 port=5432 mode=2 schema=public table=" + str(self.mantab)
            layer = QgsRasterLayer( connString, str(self.dlg.comboBox_2.currentText().upper())) 

            if layer.isValid(): #jika data dalam postgis ada maka akan menampilkan data tif yang diinginkan
                finish = 0
                while finish < 100:
                    finish += 0.001
                    self.dlg.progressBar.setValue(finish)
                QgsProject.instance().addMapLayer(layer)
                self.dlg.progressBar.setValue(0)
            else: #jika data tidak ada dalam database maka akan muncul pesan error
                msg = QMessageBox()
                msg.setText("file belum tersedia di database")
                msg.setIcon(QMessageBox.Warning)
                msg.exec()

            self.dlg.progressBar.setValue(0)     

    def tabInput(self): #fungsi  untuk tab input
        layer = self.dlg.mQgsFileWidget.filePath()

        if not layer: #muncul error ketika tidak memasukkan nilai / kosong
            msg = QMessageBox()
            msg.setText("kosong")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        elif not os.path.exists(Path(layer).parent): #muncul error ketika memasukkan direktori yang salah
            msg = QMessageBox()
            msg.setText("direktori salah")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        elif not os.path.exists(layer): #muncul error ketika nama file yang diinputkan salah
            msg = QMessageBox()
            msg.setText("nama file salah")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        elif Path(str(layer)).suffix != '.shp' and Path(str(layer)).suffix != '.SHP': #muncul error ketika file yang diinputkan bukan berekstensi shp
            msg = QMessageBox()
            msg.setText("file harus .shp")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        elif os.path.exists(Path(layer).parent): #jika bukan semuanya maka akan menampilkan data shp kedalam aplikasi qgis
            finish = 0
            while finish < 100:
                finish += 0.001
                self.dlg.progressBar.setValue(finish)
            layer2 = QgsVectorLayer(layer, os.path.splitext(os.path.basename(layer))[0], "ogr")
            QgsProject.instance().addMapLayer(layer2)
            self.dlg.progressBar.setValue(0)

    def tabSearch(self): #fungsi  untuk tab search bar
        file = self.plugin_dir + '\\map'
        layer = file + '\\' + self.dlg.lineEdit.text() + '.tif'
        Sumatra, Sulawesi, Nusatenggara, Maluku, Irianjaya, Kalimantan, Jawa = self.daftarDaerah()
       
        if self.dlg.lineEdit.text().upper() in Sumatra + Sulawesi + Nusatenggara + Maluku + Irianjaya + Kalimantan + Jawa: #benar jika data terdapat pada aplikasi
            #konek database postgis
            self.mantab = self.dlg.lineEdit.text().replace(" ", "_").lower()
            connString = "PG: dbname=sdb_course host=localhost user=postgres password=793179 port=5432 mode=2 schema=public table=" + str(self.mantab)
            layer = QgsRasterLayer( connString, str(self.dlg.lineEdit.text().upper()))
            if layer.isValid(): #benar - akan memunculkan data tif yang didapatkan dari database postgis
                finish = 0
                while finish < 100:
                    finish += 0.001
                    self.dlg.progressBar.setValue(finish)
                QgsProject.instance().addMapLayer(layer)
                self.dlg.progressBar.setValue(0)
            else: #salah - akan memunculkan pesan error jika data tif tidak terdapat pada database
                msg = QMessageBox()
                msg.setText("file belum tersedia di database")
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
        
        elif self.dlg.lineEdit.text() == "": #salah - muncul pesan error jika tidak menginputkan nilai / kosong
            msg = QMessageBox()
            msg.setText("Tidak boleh kosong")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        else: #salah - muncul pesan error jika data tidak terdapat pada list yang telah didata pada aplikasi
            msg = QMessageBox()
            msg.setText("file .tif tidak tersedia")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
            self.dlg.label_6.setText("")
           
    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = Mantab3Dialog()

            self.provinsi = ["-pilih provinsi-", "SUMATRA", "SULAWESI", "NUSATENGGARA", "MALUKU", "IRIANJAYA", "KALIMANTAN", "JAWA"]
            self.dlg.comboBox.addItems(self.provinsi)
            self.dlg.comboBox.currentIndexChanged[str].connect(self.returnKotaKab)
            self.dlg.comboBox_2.addItems(["-pilih kota/kabupaten-"])

            Sumatra, Sulawesi, Nusatenggara, Maluku, Irianjaya, Kalimantan, Jawa = self.daftarDaerah()
            model = QStringListModel()
            model.setStringList(Sumatra + Sulawesi + Nusatenggara + Maluku + Irianjaya + Kalimantan + Jawa)
            completer = QCompleter()
            completer.setFilterMode(Qt.MatchContains)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            completer.setModel(model)
            self.dlg.lineEdit.setCompleter(completer)

            self.dlg.label_6.setText("")

            #tab select
            self.dlg.pushButton.clicked.connect(self.tabSelect)
            self.dlg.pushButton_2.clicked.connect(lambda: self.dlg.close())
            # self.dlg.pushButton_3.clicked.connect()

            #tab input
            self.dlg.pushButton_4.clicked.connect(self.tabInput)
            self.dlg.pushButton_5.clicked.connect(lambda: self.dlg.close())
            # self.dlg.pushButton_6.clicked.connect()

            self.dlg.mQgsFileWidget.setFilter("Shapefile (*.shp *.SHP)")

            #tab search
            self.dlg.pushButton_10.clicked.connect(self.tabSearch)
            self.dlg.pushButton_11.clicked.connect(lambda: self.dlg.close())
            # self.dlg.pushButton_12.clicked.connect()


        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
