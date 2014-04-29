from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib as mpl
from .geom import geom
import numpy as np


class geom_pointrange(geom):
    DEFAULT_AES = {'alpha': 1, 'color': 'black', 'fill': None,
                   'shape': 'o', 'size': 20, 'linetype': 'solid'}
    REQUIRED_AES = {'x', 'y', 'ymin', 'ymax'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'identity', 'cmap': None, 'label': ''}

    _aes_renames = {'size': 's', 'shape': 'marker', 'fill': 'facecolor', 'linetype': 'linestyle'}
    _groups = {'alpha', 'marker', 'color'}

    def _plot_unit(self, pinfo, ax):
        pinfo['label'] = self.params['label']

        _abscent = {None: pinfo['color'], False: ''}
        try:
            if pinfo['facecolor'] in _abscent:
                pinfo['facecolor'] = _abscent[pinfo['facecolor']]
        except TypeError:
            pass

        # for some reason, scatter doesn't default to the same color styles
        # as the axes.color_cycle
        if "color" not in pinfo and self.params['cmap'] is None:
            pinfo["color"] = mpl.rcParams.get("axes.color_cycle", ["#333333"])[0]

        if self.params['position'] == 'jitter':
            pinfo['x'] *= np.random.uniform(.9, 1.1, len(pinfo['x']))
            pinfo['y'] *= np.random.uniform(.9, 1.1, len(pinfo['y']))

        ymin = pinfo.pop('ymin')
        ymax = pinfo.pop('ymax')

        x = pinfo.pop('x')
        y = pinfo.pop('y')

        ax.scatter(x, y, **pinfo)

        pinfo.pop('facecolor')
        pinfo.pop('s')
        pinfo.pop('marker')

        for l in zip(zip(x, x), zip(ymin, ymax)):
            ax.plot(*l, **pinfo)
