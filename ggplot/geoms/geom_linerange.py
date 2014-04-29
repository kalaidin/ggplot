from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib as mpl
from .geom import geom


class geom_linerange(geom):
    DEFAULT_AES = {'alpha': None, 'color': 'black', 'size': 1.0, 'linetype': 'solid'}
    REQUIRED_AES = {'x', 'ymin', 'ymax'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity', 'label': ''}

    _aes_renames = {'size': 'linewidth', 'linetype': 'linestyle'}
    _groups = {'alpha', 'color', 'linestyle'}

    def _plot_unit(self, pinfo, ax):
        pinfo['label'] = self.params['label']

        x = pinfo.pop('x')
        ymin = pinfo.pop('ymin')
        ymax = pinfo.pop('ymax')

        for l in zip(zip(x, x), zip(ymin, ymax)):
            ax.plot(*l, **pinfo)
