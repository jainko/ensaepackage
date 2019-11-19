import pandas as pd
from pyproj import Proj, transform
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np


def convert_long_lat(x, y, proj='mercator'):
    # Transformation des coordonnées
    p1 = Proj(init='epsg:4326')  # longitude / latitude

    if proj == 'lambert2e':
        epsg = 'epsg:27572'
    elif proj == 'mercator':
        epsg = 'epsg:3395'
    elif proj == 'plate':
        epsg = 'epsg:4326'
    else:
        epsg = 'epsg:3395'

    p2 = Proj(init=epsg)

    return transform(p1, p2, list(x), list(y))


def draw_subplot(ax, long, lat, values, year, y, hue):
    lim_metropole = [-5, 10, 41, 52]
    ax.clear()
    ax.set_extent(lim_metropole)
    ax.add_feature(cfeature.OCEAN.with_scale('50m'))
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
    ax.add_feature(cfeature.RIVERS.with_scale('50m'))
    ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')
    ax.scatter(long, lat, s=values[:, y] ** 0.5 / 5, alpha=0.5, color="red")
    if hue != '':
        ax.set_title('Production de ' + hue + '\nen France en ' + str(year[y]), fontsize=10)


def draw_plot(axs, long, lat, value, year, hue):
    if hue != '':
        plt.gcf().suptitle('Evolution de ' + hue + '\nen France de ' + str(min(year)) + ' à ' + str(max(year)),
                           fontsize=14)

    if np.shape(axs) == ():
        # Si on a juste 1 année
        draw_subplot(axs, long, lat, value, year, 0, hue)
    else:
        y = 0
        try:
            # Si les subplots sont une matrice
            a, b = np.shape(axs)
            for i in range(a):
                for j in range(b):
                    draw_subplot(axs[i][j], long, lat, value, year, y, hue)
                    y += 1
            return axs
        except ValueError:
            # Si les subplots sont un vecteur ligne ou colonne
            for i in range(len(axs)):
                draw_subplot(axs[i], long, lat, value, year, y, hue)
                y += 1
    return axs

def plot_geo_time_value(x, y, year, value, proj='mercator', axs=None, name=[], hue='', **kwargs):
    """
    Visualise l'évolution temporelle d'une donnée numérique
    géolocalisée.

    :param x: longitudes (vecteur)
    :param y: latitudes (vecteur)
    :param year: années (vecteur)
    :param value: valeurs numériques à représenter (DataFrame ou numpy array de taille n_observations * n_years)
    :param proj: méthode de projection (Mercator, PlateCarree,...) (string)
    :param axs: axes matplotlib sur lesquels tracer (vecteur ou numpay array)
    :param name: noms des lieux  (vecteur)
    :param hue: sens de la valeur numérique (:math:`CO_2`, Ammoniac, ...)
    :param kwargs: paramètres additionnels
    """

    # Conversion en array numpy pour un accès par indice
    if isinstance(value, pd.DataFrame):
        value = value.to_numpy()

    long, lat = convert_long_lat(x, y, proj)

    draw_plot(axs, long, lat, value, year, hue)

    plt.gcf().savefig("output.pdf")


# Pour la fonction bonus, complétez cette amorce
def plot_gif_geo_time_value(x, y, year, value, proj='mercator', method='gif', fig=None, ax=None,
                            name=[], hue='', **kwargs):
    """
    Visualise l'évolution temporelle d'une donnée numérique
    géolocalisée avec une animation

    :param x: longitudes (vecteur)
    :param y: latitudes (vecteur)
    :param year: années (vecteur)
    :param value: valeurs numériques à représenter (DataFrame ou numpy array de taille n_observations * n_years)
    :param proj: méthode de projection (Mercator, PlateCarree,...) (string)
    :param method: type d'animation (gif, mp4 ou webm) (string)
    :param axs: axes matplotlib sur lesquels tracer (vecteur ou numpay array)
    :param name: noms des lieux  (vecteur)
    :param hue: sens de la valeur numérique (:math:`CO_2`, Ammoniac, ...)
    :param kwargs: paramètres additionnels
    """

    # Conversion en array numpy pour un accès par indice
    if isinstance(value, pd.DataFrame):
        value = value.to_numpy()

    if fig == None:
        fig = plt.gcf()

    long, lat = convert_long_lat(x, y, proj)

    def animate(k):
        draw_subplot(ax, long, lat, value, year, k, hue)

    animation = anim.FuncAnimation(fig, animate, frames=len(year), blit=False, repeat=True)

    try:
        animation.save("output." + method, fps=1)
    except ValueError:
        animation.save("output.gif", fps=1)