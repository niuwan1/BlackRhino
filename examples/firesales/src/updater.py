#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

"""
black_rhino is a multi-agent simulator for financial network analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@keble.ox.ac.uk)
Pawel Fiedor (pawel@fiedor.eu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from abm_template.src.basemodel import BaseModel


# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------


class Updater(BaseModel):
    #
    #
    # VARIABLES
    #
    #

    identifier = ""

    model_parameters = {}

    sales_across_banks = {}
    #
    #
    # METHODS
    #

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Updater, self).set_identifier(value)

    def __str__(self):
        super(Updater, self).__str__(self)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, values):
        super(Updater, self).set_model_parameters(values)

    def get_interactions(self):
        return self.interactions

    def interactions(self):
        super(Updater, self).interactions(self)

    def set_interactions(self, values):
        super(Updater, self).set_interactions(values)

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment):
        self.environment = environment
        self.sales_across_banks = {}
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, current_step):

        for agent in environment.agents:

            agent.calc_total_asset()
            agent.calc_total_asset_sales(environment, current_step)

        for agent in environment.agents:

            for k in (s for s in agent.state_variables if s == 'm_1'):
                agent.temp = agent.state_variables[k] * agent.TAS
                agent.sale_of_k_assets[k] = agent.temp
                # print agent.sale_of_k_assets.items()
                asset_type = k
                self.sales_across_banks['m_1'] = agent.sum_assets(environment, current_step, asset_type)

        print self.sales_across_banks

        for agent in environment.agents:

            for k in (s for s in agent.state_variables if s == 'm_2'):
                agent.temp = agent.state_variables[k] * agent.TAS
                agent.sale_of_k_assets[k] = agent.temp
                print agent.sale_of_k_assets.items()
                asset_type = k
                self.sales_across_banks['m_2'] = agent.sum_assets(environment, current_step, asset_type)

        print self.sales_across_banks

        # for agent in environment.agents:

        #     for k in (s for s in agent.state_variables if s == 'm_2'):
        #         agent.temp = (agent.state_variables[k] * agent.TAS)
        #         agent.sale_of_k_assets[k] = agent.temp
        #         print agent.sale_of_k_assets.items()
        #         # print agent.temp

                # self.sales_across_banks['m_2'] = agent.sum_assets(environment, current_step)

        # print self.sales_across_banks.items()
            # for k in (s for s in self.state_variables if s != 'leverage'):
            #         temp = self.state_variables[k] * self.TAS

    # -----------------------------------------------------------------------
