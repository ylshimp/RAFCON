# Copyright (C) 2014-2017 DLR
#
# All rights reserved. This program and the accompanying materials are made
# available under the terms of the Eclipse Public License v1.0 which
# accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
# Franz Steinmetz <franz.steinmetz@dlr.de>
# Rico Belder <rico.belder@dlr.de>
# Sebastian Brunner <sebastian.brunner@dlr.de>

from copy import copy, deepcopy
from gtkmvc import ModelMT

from rafcon.gui.models.state_element import StateElementModel
from rafcon.core.state_elements.outcome import Outcome
from rafcon.utils import log
logger = log.get_logger(__name__)


class OutcomeModel(StateElementModel):
    """This model class manages a Outcome

    :param rafcon.core.outcome.Outcome outcome: The outcome to be wrapped
    :param rafcon.gui.models.abstract_state.AbstractStateModel parent: The state model of the state element
    :param rafcon.utils.vividict.Vividict meta: The meta data of the state element model
     """

    outcome = None

    __observables__ = ("outcome",)

    def __init__(self, outcome, parent, meta=None):
        """Constructor
        """
        super(OutcomeModel, self).__init__(parent, meta)

        assert isinstance(outcome, Outcome)
        self.outcome = outcome

    def __str__(self):
        return "Model of Outcome: {0}".format(self.outcome)

    def __copy__(self):
        outcome = copy(self.outcome)
        outcome_m = self.__class__(outcome, parent=None, meta=None)
        outcome_m.meta = deepcopy(self.meta)
        return outcome_m

    def __deepcopy__(self, memo=None, _nil=[]):
        return self.__copy__()

    @property
    def core_element(self):
        return self.outcome

    @ModelMT.observe("outcome", before=True, after=True)
    def model_changed(self, model, prop_name, info):
        super(OutcomeModel, self).model_changed(model, prop_name, info)

    def prepare_destruction(self):
        super(OutcomeModel, self).prepare_destruction()
        self.outcome = None

    def _meta_data_editor_gaphas2opengl(self, vividict):
        if 'rel_pos' in vividict:
            del vividict['rel_pos']
        return vividict

    def _meta_data_editor_opengl2gaphas(self, vividict):
        from rafcon.gui.helpers.meta_data import contains_geometric_info
        if self.parent:
            state_size = self.parent.get_meta_data_editor()['size']
            if contains_geometric_info(state_size):
                step = min(state_size) / 10.
                if self.outcome.outcome_id == -1:  # aborted
                    vividict["rel_pos"] = (state_size[0] - step, 0)
                elif self.outcome.outcome_id == -2:  # preempted
                    vividict["rel_pos"] = (state_size[0] - step * 3, 0)
                else:  # user defined outcome
                    num_outcomes = len(self.parent.outcomes) - 2
                    # count user defined outcomes with smaller id than the current outcome
                    outcome_num = sum(1 for outcome_id in self.parent.state.outcomes if
                                      0 <= outcome_id < self.outcome.outcome_id)
                    vividict["rel_pos"] = (state_size[0], state_size[1] / (num_outcomes + 1) * (outcome_num + 1))
        return vividict
