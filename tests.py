import unittest
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from package.ensae2019.main import convert_long_lat, draw_plot


class test_plot_geo_time_value(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    def setUp(self):
        """Initialisation des tests"""
        # Les données donnent des Longitudes et Latitudes, sous la projection initiale, comprises entre -119 et 38 (Lontitude),-46 et 52 (Latitude)
        # On prend donc, aléatoirement, des données dans ces deux intervalles

        # X=[rd.random()*(38+119)-119 for _ in range(5)]
        # Y=[rd.random()*(52+46)-52 for _ in range (5)]

        self.X = [-77.42195028762158, -7.947189234775863, -36.85078018385313, -103.37763547019526, 34.04165783328568]
        self.Y = [11.72396517936211, -26.288486596419695, 22.214339345435803, -0.5065952615786102, -26.11682941288223]
        self.p1 = 'mercator'


        # On test 3 cas : une seule carte, cartes en ligne, cartes en grille

        # les 3 pbjects Axes à modifier
        fig, self.axs1_1 = plt.subplots(1, 1, figsize=(20, 20), subplot_kw={'projection': ccrs.Mercator()})
        fig, self.axs4_1 = plt.subplots(4, 1, figsize=(20, 20), subplot_kw={'projection': ccrs.Mercator()})
        fig, self.axs2_2 = plt.subplots(2, 2, figsize=(20, 20), subplot_kw={'projection': ccrs.Mercator()})

        # Les 3 objects Axes de controle
        fig, self.axs1_1Raw = plt.subplots(1, 1, figsize=(20, 20), subplot_kw={'projection': ccrs.Mercator()})
        fig, self.axs4_1Raw = plt.subplots(4, 1, figsize=(20, 20), subplot_kw={'projection': ccrs.Mercator()})
        fig, self.axs2_2Raw = plt.subplots(2, 2, figsize=(20, 20), subplot_kw={'projection': ccrs.Mercator()})

        # 2 cas : une seul année ou plusieurs
        self.value1Year = np.random.randint(0,10,size=(5, 1))
        self.value4Years = np.random.randint(0,10,size=(5, 4))

        self.year1 = [2003]
        self.year2 = [2003, 2004, 2005, 2006]

        self.hue = "test"

    def test_long_lat(self):
        # Teste si la projection renvoie bien les valeurs attendues
        Xreal = [-8618572.082240175, -884677.0588530344, -4102210.0854013865, -11507945.739954792, 3789500.015760215]
        Yreal = [1305632.9897280498, -3015936.6391554433, 2521130.7920743427, 56017.14383234842, -2994754.202243703]

        Xpred, Ypred = convert_long_lat(self.X, self.Y, self.p1)

        self.assertAlmostEqual(Xreal[0], Xpred[0])
        self.assertAlmostEqual(Yreal[0], Ypred[0])

    def test_draw_plot(self):
        # Teste si les objects matplotlib.Axes ont été modifiés
        self.assertNotEquals(self.axs1_1Raw, draw_plot(self.axs1_1, self.X, self.Y, self.value1Year, self.year1, self.hue))
        self.assertNotEquals(self.axs4_1Raw.all(), draw_plot(self.axs4_1, self.X, self.Y, self.value4Years, self.year2, self.hue).all())
        self.assertNotEquals(self.axs2_2Raw.all(), draw_plot(self.axs2_2, self.X, self.Y, self.value4Years, self.year2, self.hue).all())