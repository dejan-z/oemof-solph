# -*- coding: utf-8 -*-

"""Optional classes to be added to a network class.
This file is part of project oemof (github.com/oemof/oemof). It's copyrighted by
the contributors recorded in the version control history of the file, available
from its original location oemof/oemof/solph/options.py

SPDX-License-Identifier: GPL-3.0-or-later
"""


class Investment:
    """
    Parameters
    ----------
    maximum : float
        Maximum of the additional invested capacity
    minimum : float
        Minimum of the addtional invested capacity
    ep_costs : float
        Equivalent periodical costs for the investment, if period is one
        year these costs are equal to the equivalent annual costs.

    """
    def __init__(self, maximum=float('+inf'), minimum=0, ep_costs=0):
        self.maximum = maximum
        self.minimum = minimum
        self.ep_costs = ep_costs


class NonConvex:
    """
    Parameters
    ----------
    startup_costs : numeric
        Costs associated with a start of the flow (representing a unit).
    shutdown_costs : numeric
        Costs associated with the shutdown of the flow (representing a unit).
    minimum_uptime : numeric (1 or positive integer)
        Minimum time that a flow must be greater then its minimum flow after
        startup. Be aware that minimum up and downtimes can contradict each
        other and may lead to infeasible problems.
    minimum_downtime : numeric (1 or positive integer)
        Minimum time a flow is forced to zero after shutting down.
        Be aware that minimum up and downtimes can contradict each
        other and may to infeasible problems.
    initial_status : numeric (0 or 1)
        Integer value indicating the status of the flow in the first time step
        (0 = off, 1 = on). For minimum up and downtimes, the initial status
        is set for the respective values in the edge regions e.g. if a
        minimum uptime of four timesteps is defined, the initial status is
        fixed for the four first and last timesteps of the optimization period.
        If both, up and downtimes are defined, the initial status is set for
        the maximum of both e.g. for six timesteps if a minimum downtime of
        six timesteps is defined in addition to a four timestep minimum uptime.
    """
    def __init__(self, **kwargs):
        # super().__init__(self, **kwargs)
        self.startup_costs = kwargs.get('startup_costs')
        self.shutdown_costs = kwargs.get('shutdown_costs')
        self.minimum_uptime = kwargs.get('minimum_uptime')
        self.minimum_downtime = kwargs.get('minimum_downtime')
        self.initial_status = kwargs.get('initial_status', 0)
